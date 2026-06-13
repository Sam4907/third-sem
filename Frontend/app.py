import numpy as np
from itertools import zip_longest
from flask import Flask, jsonify
from flask_cors import CORS
import requests

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
            "track":wel[i, 0], 
            "driver":wel[i, 3],
            "pos":wel[i, 1],
            "starting_pos":wel[i, 5],
            "team":wel[i, 4],
            "pos_gained":int(wel[i, 5])-int(wel[i, 1])
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
            "rank": count,
            "driver":data[i, 3],
            "team":data[i, 4],
            "std":int(std[i])
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
            "rank": count,
            "driver":data[i, 3],
            "team":data[i, 4],
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
            "team":i,
            "dnf":0
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
            "team":i[4],
            "driver":i[3],
            "pos":i[1],
            "starting_pos":i[5],
            "points":i[8]
        }
        out.append(rec)
    return jsonify(out)

if __name__=='__main__':
    app.run(port=5000, debug=True)
