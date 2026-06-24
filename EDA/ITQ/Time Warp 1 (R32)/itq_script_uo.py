import pandas as pd
import itertools
import numpy as np

df=pd.read_csv("standings.csv")
odds=pd.read_csv("odds.csv")

odds[['home', 'draw', 'away']]=odds[['home', 'draw', 'away']].map(pd.eval)
odds[['home', 'draw', 'away']]=1/odds[['home', 'draw', 'away']]
odds[['home', 'draw', 'away']]=odds[['home', 'draw', 'away']].div(odds[['home', 'draw', 'away']].sum(axis=1), axis=0)

groups=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

def draw(jf, home, away):
    jf.loc[jf['team']==home, ['pts', 'd']]+=1
    jf.loc[jf['team']==away, ['pts', 'd']]+=1

def win(jf, winner, loser):
    jf.loc[jf['team']==winner, 'pts']+=3
    jf.loc[jf['team']==winner, ['w', 'gf', 'gd']]+=1
    jf.loc[jf['team']==loser, ['l', 'ga']]+=1
    jf.loc[jf['team']==loser, 'gd']-=1

ans=[]
r32=[]

for g in groups:
    pu=0
    curr=df[df['group']==g]
    odd=odds[odds['group']==g]
    odd['d']='tie'
    result=list(itertools.product(odd.iloc[0][['teama', 'teamb', 'd']], odd.iloc[1][['teama', 'teamb', 'd']]))
    match1_probs={odd.iloc[0]['teama']:odd.iloc[0]['home'], odd.iloc[0]['teamb']:odd.iloc[0]['away'], odd.iloc[0]['d']:odd.iloc[0]['draw']}
    match2_probs={odd.iloc[1]['teama']:odd.iloc[1]['home'], odd.iloc[1]['teamb']:odd.iloc[1]['away'], odd.iloc[1]['d']:odd.iloc[1]['draw']}
    for i in result:
        wel=curr.copy()
        universe_probs=match1_probs[i[0]]*match2_probs[i[1]]
        pu=max(pu, universe_probs)
        wel['mp']+=1
        if(i[0]=='tie'):
            draw(wel, odd.iloc[0]['teama'], odd.iloc[0]['teamb'])
        elif(i[0]==odd.iloc[0]['teama']):
            win(wel, odd.iloc[0]['teama'], odd.iloc[0]['teamb'])
        else:
            win(wel, odd.iloc[0]['teamb'], odd.iloc[0]['teama'])
        if(i[1]=='tie'):
            draw(wel, odd.iloc[1]['teama'], odd.iloc[1]['teamb'])
        elif(i[1]==odd.iloc[1]['teama']):
            win(wel, odd.iloc[1]['teama'], odd.iloc[1]['teamb'])
        else:
            win(wel, odd.iloc[1]['teamb'], odd.iloc[1]['teama'])
        if universe_probs>=pu: 
            pu=universe_probs
            save=wel.copy()
    ans.append(save.sort_values(by=['pts', 'gd', 'gf'], ascending=False))
    r32.append(save.sort_values(by=['pts', 'gd', 'gf'], ascending=False).head(2))

itq=pd.concat(r32, ignore_index=True)
third=pd.concat([a.iloc[[2]] for a in ans], ignore_index=True)
eight=third.sort_values(by=['pts', 'gd', 'gf'], ascending=False)
r32=pd.concat([itq, eight.head(8)], ignore_index=True)
print(r32)