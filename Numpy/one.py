import numpy as np

### 0Track,1Pos,2No,3Driver,4Team,5Starting Pos,6Laps,7Time/Retired,8Points,9Set Fastest Lap,Fastest Lap Time

data=np.genfromtxt("F1_2025_RaceResults.csv", delimiter= ',',dtype= str,skip_header=1)

def driver_mask(driver):
    return data[:, 3]==driver ###will return booleans; use data[mask] to get complete results

def team_mask(team):
    return data[:, 4]==team

def out_of_pos_recov(driver):
    req=data[driver_mask(driver)]
    pos=req[(req[:, 1]!='DNF')&(req[:, 1]!='DQ')&(req[:, 1]!='NC')&(req[:, 8].astype(int)>0)&(req[:, 5]!='DNF')&(req[:, 5]!='DQ')] ###tackle dnf and dq
    print(pos[(pos[:, 5].astype(int)>10)])

def team_clean_sweep(team):
    req=data[team_mask(team)]
    req=req[(req[:, 1]!='NC')&(req[:, 1]!='DNF')&(req[:, 1]!='DQ')]
    req=req[(req[:, 1].astype(int)<=3)]
    vals, inv, cts=np.unique(req[:, 0], return_inverse=True, return_counts=True)
    req=req[(cts == 2)[inv]]
    print(req)

def racer_dnf(driver):
    req=data[driver_mask(driver)]
    count=np.size(req[:, 1]!='DQ')
    dnf=np.size(req[req[:, 7]=='DNF'])/11
    print(np.ceil(100-(dnf/count)*100), "%", sep="")

def fastest_lap_pointless():
    req=data[(data[:, 9]=="Yes")&(data[:, 8]==0)]
    print(req)

def masterclass():
    req=data[(data[:, 1]=="1")&(data[:, 5]=="1")&(data[:, 9]=="Yes")]
    print(req)

def dropoff():
    req=data[(data[:, 5].astype(int)<=5)&(data[:, 8]=="0")]
    print(req)

def track_mask(track):
    return data[:, 0]==track

def overtaker():
    ls=np.unique(data[:, 0])
    for i in ls:
        req=data[track_mask(i)]
        ans=req[(req[:, 1]!='DQ')&(req[:, 1]!='NC')]
        fin=ans[ans[:, 5].astype(int)-ans[:, 1].astype(int)==np.max(ans[:, 5].astype(int)-ans[:, 1].astype(int))]
        print(i, fin[:, 3])

def mvp():
    '''
    ls=np.unique(data[:, 0])
    for i in ls: 
        req=data[track_mask(i)]
        val, inv=np.unique(req[:, 4], return_inverse=True)
        totals=np.bincount(inv, weights=req[:, 8].astype(int))
        val=totals[inv]
        print(req[((req[:, 8].astype(int)/val)*100)>60])
    '''
    comb=np.char.add(data[:, 0], data[:, 4])
    val, inv=np.unique(comb, return_inverse=True)
    totals=np.bincount(inv, weights=data[:, 8].astype(int))
    val=totals[inv]
    print(data[((data[:, 8].astype(int)/val)*100)>60])
    
def strong_team():
    lst=np.unique(data[:, 4])
    req=np.unique(data[(data[:, 7]=='DNF')|(data[:, 7]=='DSQ')])
    print(np.setdiff1d(lst, req))

def strong_racer():
    val, inv=np.unique(data[:, 3], return_inverse=True)
    totals=np.bincount(inv, weights=data[:, 8].astype(int))
    avg=np.bincount(inv, weights=data[:, 5].astype(int))
    counts=np.bincount(inv)
    '''ans=totals[inv]/(avg[inv]/counts[inv])
    print(data[np.argmax(ans), 3])'''
    ans=totals/(avg/counts)
    print(val[np.argmax(ans)])
'''   
out_of_pos_recov("Oliver Bearman")
team_clean_sweep("McLaren Mercedes")
racer_dnf("Gabriel Bortoleto")
fastest_lap_pointless()
masterclass()
dropoff()
overtaker()
mvp()
strong_team()
'''
strong_racer()