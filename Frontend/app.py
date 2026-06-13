import numpy as np
from itertools import zip_longest
from flask import Flask, jsonify
from flask_cors import CORS
import requests
import math

app=Flask(__name__)
CORS(app)

### 0Track,1Pos,2No,3Driver,4Team,5Starting Pos,6Laps,7Time/Retired,8Points,9Set Fastest Lap,Fastest Lap Time
data=np.genfromtxt("F1_2025_RaceResults.csv", delimiter= ',',dtype= str,skip_header=1)

### Querying

###Masks
def driver_mask(driver):
    return data[:, 3]==driver ###will return booleans; use data[mask] to get complete results

def team_mask(team):
    return data[:, 4]==team

def track_mask(track):
    return data[:, 0]==track

### starting below 10 but winning points
@app.route('/overtaker')
def gr_overtaker():
    wel=data[~np.isin(data[:, 1], ['DQ', 'NC', 'DNF'])]
    gain=wel[:, 5].astype(int)-(wel[:, 1].astype(int))
    wel=wel[np.lexsort((gain, wel[:, 0]))]
    tr, inv=np.unique(wel[:, 0], return_index=True)  
    ind=np.append(inv[1:]-1, len(wel)-1)
    out=[]
    for i in ind:
        rec={
            "col_1":wel[i, 0],
            "col_2":wel[i, 4], 
            "col_3":wel[i, 3],
            "col_4":wel[i, 1],
            "col_5":wel[i, 5],
            "col_6":int(wel[i, 5])-int(wel[i, 1])
        }
        out.append(rec)
    return jsonify(out)

@app.route('/eff')
def gr_eff_index():
    wel=data[~np.isin(data[:, 1], ['DQ', 'NC', 'DNF'])]
    jf, inve=np.unique(wel[:, 3], return_inverse=True)
    counts=np.bincount(inve)
    xx=(np.bincount(inve, weights=wel[:, 1].astype(int)))**2
    xsq=np.bincount(inve, weights=(wel[:, 1].astype(int)**2))
    std=np.sqrt((xsq/counts)-(xx/(counts**2)))
    ind=np.argsort(std)
    out=[]
    count=1
    for i in ind:
        rec={
            "col_1": count,
            "col_2":data[i, 4],
            "col_3":data[i, 3],
            "col_4":math.ceil(std[i])
        }
        count+=1
        out.append(rec)
    return jsonify(out)

@app.route('/lwma')
def gr_lwma():
    wel=data[~np.isin(data[:, 1], ['DQ', 'NC', 'DNF'])] 
    to=np.arange(np.size(wel[:, 3]))
    wel=wel[np.lexsort((to, wel[:, 3]))]    
    jf, inv=np.unique(wel[:, 3], return_inverse=True)
    counts=np.bincount(inv)
    ends=np.cumsum(counts)
    ends=ends[:-1]
    ones=np.ones(np.size(wel[:, 3]), dtype=int)
    ones[ends]-=counts[:-1]
    ones=np.cumsum(ones)
    val=np.bincount(inv, weights=(ones*wel[:, 1].astype(int)))/np.bincount(inv, weights=ones)
    ind=np.argsort(val)
    out=[]
    count=1
    for i in ind:
        rec={
            "col_1": count,
            "col_3":data[i, 4],
            "col_2":data[i, 3]
        }
        count+=1
        out.append(rec)
    return jsonify(out)

@app.route('/constructor')
def strong_team():
    lst=np.unique(data[:, 4])
    req=np.unique(data[(data[:, 7]=='DNF')|(data[:, 7]=='DSQ')])
    out=[]
    ls=(np.setdiff1d(lst, req)).tolist()
    for i in ls:
        rec={
            "col_1":i,
            "col_2":0
        }
        out.append(rec)
    return jsonify(out)    

@app.route('/recovery/<driver>')
def out_of_pos_recov(driver):
    req=data[driver_mask(driver)]
    pos=req[(req[:, 1]!='DNF')&(req[:, 1]!='DQ')&(req[:, 1]!='NC')&(req[:, 8].astype(int)>0)&(req[:, 5]!='DNF')&(req[:, 5]!='DQ')] ###tackle dnf and dq
    res=pos[(pos[:, 5].astype(int)>10)]
    out=[]
    for i in res:
        rec={
            "track":i[0],
            "driver":i[4],
            "team":i[3],
            "pos":i[1],
            "starting_pos":i[5],
            "points":i[8]
        }
        out.append(rec)
    return jsonify(out)

@app.route('/clean/<team>')
def team_clean_sweep(team):
    req=data[team_mask(team)]
    req=req[(req[:, 1]!='NC')&(req[:, 1]!='DNF')&(req[:, 1]!='DQ')]
    req=req[(req[:, 1].astype(int)<=3)]
    vals, inv, cts=np.unique(req[:, 0], return_inverse=True, return_counts=True)
    req=req[(cts==2)[inv]]
    out=[]
    for i in range(0, len(req), 2):
        d1=req[i]
        d2=req[i+1]
        total=int(d1[8])+int(d2[8])
        rec={
            "col_1": d1[0],
            "col_2": d1[4],
            "col_3": d1[3],
            "col_4": d1[1],
            "col_5": d2[3],
            "col_6": d2[1],
            "col_7": total
        }
        out.append(rec)
    return jsonify(out)

@app.route('/dnf')
def racer_dnf():
    unique_pairs, starts=np.unique(data[:, [4, 3]], axis=0, return_counts=True)
    teams=unique_pairs[:, 0]
    drivers=unique_pairs[:, 1]
    req=(data[:, 7]=='DNF')|(data[:, 7]=='DSQ')
    dridnf, counts=np.unique(data[req, 3], return_counts=True)
    dnfs=np.zeros(drivers.shape, dtype=int)
    vals, ind, dnf=np.intersect1d(drivers, dridnf, return_indices=True)
    dnfs[ind]=counts[dnf]
    perc=np.round(((starts-dnfs)/starts)*100, 1)
    out=[
        {
            "col_1": te,
            "col_2": d,
            "col_3": int(ts),
            "col_4": int(dc),
            "col_5": f"{fr}%"
        }
        for d, te, ts, dc, fr in zip(drivers, teams, starts, dnfs, perc)
    ]
    out=sorted(
        out, 
        key=lambda x: (float(x["col_5"].replace('%', '')), int(x["col_3"])), 
        reverse=True
    )
    return jsonify(out)

@app.route('/trifecta')
def masterclass():
    req=data[(data[:, 1]=="1")&(data[:, 5]=="1")&(data[:, 9]=="Yes")]
    out=[]
    for i in req:
        rec={
            "col_1":i[0],
            "col_2":i[4],
            "col_3":i[3],
            "col_4":i[1],
            "col_5":i[5],
            "col_6":i[10],
            "col_7":i[8]
        }
        out.append(rec)
    return jsonify(out)

@app.route('/dropoff')
def dropoff():
    req=data[(data[:, 5].astype(int)<=5)&(data[:, 8]=="0")]
    out=[]
    for i in req:
        rec={
            "col_1":i[0],
            "col_2":i[4],
            "col_3":i[3],
            "col_4":i[1],
            "col_5":i[5],
        }
        out.append(rec)
    return jsonify(out)

@app.route('/mvp/<track>')
def mvp_per_track(track):
    tr=data[track_mask(track)]
    drivers=tr[:, 3]
    positions=tr[:, 1]
    teams=tr[:, 4]
    points=tr[:, 8].astype(int)
    u_drivers, dr_inv=np.unique(drivers, return_inverse=True)
    dr_totals=np.bincount(dr_inv, weights=points)[dr_inv]
    u_teams, tm_inv=np.unique(teams, return_inverse=True)
    tm_totals=np.bincount(tm_inv, weights=points)[tm_inv]
    perc=np.round((dr_totals/tm_totals)*100, 1)
    mask=perc>60.0
    vals, i=np.unique(drivers[mask], return_index=True)
    out=[
        {
            "col_1": track,
            "col_2": t,
            "col_3": d,
            "col_5": int(dt),
            "col_7": int(tt),
            "col_6": f"{sp}%",
            "col_4": po
        }
        for t, d, dt, tt, sp, po in zip(
            teams[mask][i], 
            drivers[mask][i], 
            dr_totals[mask][i], 
            tm_totals[mask][i], 
            perc[mask][i],
            positions[mask][i]
        )
    ]
    return jsonify(sorted(out, key=lambda x: float(x["col_6"].replace('%', '')), reverse=True))

if __name__=='__main__':
    app.run(port=5000, debug=True)
