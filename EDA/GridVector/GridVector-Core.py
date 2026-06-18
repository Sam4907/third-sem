import numpy as np
from itertools import zip_longest

#functions prefixed with gr print grid reports
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
def out_of_pos_recov(driver):
    req=data[driver_mask(driver)]
    pos=req[(req[:, 1]!='DNF')&(req[:, 1]!='DQ')&(req[:, 1]!='NC')&(req[:, 8].astype(int)>0)&(req[:, 5]!='DNF')&(req[:, 5]!='DQ')] ###tackle dnf and dq
    print(pos[(pos[:, 5].astype(int)>10)])

### both drivers on podium
def team_clean_sweep(team):
    req=data[team_mask(team)]
    req=req[(req[:, 1]!='NC')&(req[:, 1]!='DNF')&(req[:, 1]!='DQ')]
    req=req[(req[:, 1].astype(int)<=3)]
    vals, inv, cts=np.unique(req[:, 0], return_inverse=True, return_counts=True)
    req=req[(cts==2)[inv]]
    print(req)

### percentage of finishes
def racer_dnf(driver):
    req=data[driver_mask(driver)]
    count=np.size(req[:, 1]!='DQ')
    dnf=np.size(req[req[:, 7]=='DNF'])/11
    print(np.ceil(100-(dnf/count)*100), "%", sep="")

### unrewarded speedster
def fastest_lap_pointless():
    req=data[(data[:, 9]=="Yes")&(data[:, 8]==0)]
    print(req)

### perfect weekend for driver (trifecta)
def masterclass():
    req=data[(data[:, 1]=="1")&(data[:, 5]=="1")&(data[:, 9]=="Yes")]
    print(req)

### started in top 5 but finished out of points
def dropoff():
    req=data[(data[:, 5].astype(int)<=5)&(data[:, 8]=="0")]
    print(req)

### gained max positions in a track
def gr_overtaker():
    '''
    ls=np.unique(data[:, 0])
    for i in ls:
        req=data[track_mask(i)]
        ans=req[(req[:, 1]!='DQ')&(req[:, 1]!='NC')]
        fin=ans[ans[:, 5].astype(int)-ans[:, 1].astype(int)==np.max(ans[:, 5].astype(int)-ans[:, 1].astype(int))]
        print(i, fin[:, 3])
    '''
    wel=data[~np.isin(data[:, 1], ['DQ', 'NC', 'DNF'])]
    gain=wel[:, 5].astype(int)-(wel[:, 1].astype(int))
    wel=wel[np.lexsort((gain, wel[:, 0]))]
    tr, inv=np.unique(wel[:, 0], return_index=True)  
    ind=np.append(inv[1:]-1, len(wel)-1)
    final=wel[ind, 5].astype(int)-wel[ind, 1].astype(int)   
    jf=np.char.ljust(wel[ind, 0], 15)+" : "+np.char.ljust(wel[ind, 3], 20)+" : +" +np.char.rjust(np.char.mod("%d", final), 2)+" pos"
    print(f"Grid Report: Overtaker of the race: \n"+"\n".join(jf))

### scored greater than 60% of points for team
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
    
### good constructor
def strong_team():
    lst=np.unique(data[:, 4])
    req=np.unique(data[(data[:, 7]=='DNF')|(data[:, 7]=='DSQ')])
    print(np.setdiff1d(lst, req))

### metric for calculating efficiency: total points/average position 
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
gr_overtaker()
mvp()
strong_team()
strong_racer()
'''

### Mathematics
### 0Track,1Pos,2No,3Driver,4Team,5Starting Pos,6Laps,7Time/Retired,8Points,9Set Fastest Lap,Fastest Lap Time

### self-implemented standard deviation
def gr_eff_index():
    wel=data[~np.isin(data[:, 1], ['DQ', 'NC', 'DNF'])]
    jf, inve=np.unique(wel[:, 3], return_inverse=True)
    counts=np.bincount(inve)
    xx=(np.bincount(inve, weights=wel[:, 1].astype(int)))**2
    xsq=np.bincount(inve, weights=(wel[:, 1].astype(int)**2))
    std=np.sqrt((xsq/counts)-(xx/(counts**2)))
    ind=np.argsort(std)
    final=np.char.ljust(jf[ind], 25)+": "+np.char.mod("%.2f", std[ind])
    ranks=np.arange(1, len(final)+1)
    final=np.char.ljust(np.char.mod("%d", ranks), 3)+final
    print("Grid report: Standard Deviation\n"+"\n".join(final))

### using linear decay
def lwma(driver):
    req=data[driver_mask(driver)]
    filt=req[(req[:, 1]!='NC')&(req[:, 1]!='DQ')]
    ws=np.arange(1, np.size(filt[:, 1])+1)
    avg=ws*filt[:, 1].astype(int)
    print(np.sum(avg)/np.sum(ws))

### oscar had the most stable recent races, max improved dramatically in the end, kimi stabilised towards the end of the season
def gr_lwma():
    wel=data[~np.isin(data[:, 1], ['DQ', 'NC', 'DNF'])] ### contains finished races by all drivers
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
    final=np.char.ljust(jf[ind], 25)+": "+np.char.mod("%.2f", val[ind])
    ranks=np.arange(1, len(final)+1)
    final=np.char.ljust(np.char.mod("%d", ranks), 3)+final
    print("Grid report: Linear Weighted Moving Averages\n"+"\n".join(final))
    

def float_conv():
    req=data[data[:, 10]!=""]
    vals=np.char.split(req[:, 10], sep=".")
    vals=np.array(list(zip_longest(*vals, fillvalue=0))).T
    seconds=vals[:, 0].astype(int)*60+vals[:, 1].astype(int)+(vals[:, 2].astype(int)/1000)
    print(seconds)

'''
float_conv()
gr_eff_index()
lwma("Lando Norris")
gr_lwma()
'''
