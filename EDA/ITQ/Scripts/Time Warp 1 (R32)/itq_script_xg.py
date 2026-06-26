import pandas as pd
import itertools
import numpy as np
from scipy.stats import poisson

df=pd.read_csv("../../Data/standings.csv")
odds=pd.read_csv("../../Data/odds.csv") 
stats=pd.read_csv("../../Data/xg.csv", index_col="country")

stats['xg_per_game']=stats['xg']/2
stats['ga_per_game']=stats['ga']/2
avg_tournament_xg=stats['xg_per_game'].mean()
stats['att_strength']=stats['xg_per_game']/avg_tournament_xg
stats['defe_weakness']=stats['ga_per_game']/avg_tournament_xg

def compute_match_odds(team_a, team_b):
    att_a=stats.loc[team_a, 'att_strength'] if team_a in stats.index else 1.0
    defe_a=stats.loc[team_a, 'defe_weakness'] if team_a in stats.index else 1.0
    att_b=stats.loc[team_b, 'att_strength'] if team_b in stats.index else 1.0
    defe_b=stats.loc[team_b, 'defe_weakness'] if team_b in stats.index else 1.0
    lambda_a=att_a*defe_b*avg_tournament_xg
    lambda_b=att_b*defe_a*avg_tournament_xg
    max_goals=6
    grid=np.zeros((max_goals, max_goals))
    for a in range(max_goals):
        for b in range(max_goals):
            grid[a, b]=poisson.pmf(a, lambda_a)*poisson.pmf(b, lambda_b)
    win_a=np.sum(np.tril(grid, -1).T)
    draw=np.sum(np.diag(grid))
    win_b=np.sum(np.triu(grid, 1).T)
    total=win_a+draw+win_b
    return win_a/total, draw/total, win_b/total

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
    odd=odds[odds['group']==g].copy()
    p_h1, p_d1, p_a1=compute_match_odds(odd.iloc[0]['teama'], odd.iloc[0]['teamb'])
    p_h2, p_d2, p_a2=compute_match_odds(odd.iloc[1]['teama'], odd.iloc[1]['teamb'])
    odd['d']='tie'
    result=list(itertools.product(odd.iloc[0][['teama', 'teamb', 'd']], odd.iloc[1][['teama', 'teamb', 'd']]))
    match1_probs={odd.iloc[0]['teama']: p_h1, odd.iloc[0]['teamb']: p_a1, odd.iloc[0]['d']: p_d1}
    match2_probs={odd.iloc[1]['teama']: p_h2, odd.iloc[1]['teamb']: p_a2, odd.iloc[1]['d']: p_d2}
    for i in result:
        wel=curr.copy()
        universe_probs=match1_probs[i[0]]*match2_probs[i[1]]
        pu=max(pu, universe_probs)
        wel['mp']+=1
        if i[0]=='tie':
            draw(wel, odd.iloc[0]['teama'], odd.iloc[0]['teamb'])
        elif i[0]==odd.iloc[0]['teama']:
            win(wel, odd.iloc[0]['teama'], odd.iloc[0]['teamb'])
        else:
            win(wel, odd.iloc[0]['teamb'], odd.iloc[0]['teama'])    
        if i[1]=='tie':
            draw(wel, odd.iloc[1]['teama'], odd.iloc[1]['teamb'])
        elif i[1]==odd.iloc[1]['teama']:
            win(wel, odd.iloc[1]['teama'], odd.iloc[1]['teamb'])
        else:
            win(wel, odd.iloc[1]['teamb'], odd.iloc[1]['teama'])      
        if universe_probs>=pu: 
            pu = universe_probs
            save = wel.copy() 
    ans.append(save.sort_values(by=['pts', 'gd', 'gf'], ascending=False))
    r32.append(save.sort_values(by=['pts', 'gd', 'gf'], ascending=False).head(2))

itq=pd.concat(r32, ignore_index=True)
third=pd.concat([a.sort_values(by=['pts', 'gd', 'gf'], ascending=False).iloc[[2]] for a in ans], ignore_index=True)
eight=third.sort_values(by=['pts', 'gd', 'gf'], ascending=False)
r32=pd.concat([itq, eight.head(8)], ignore_index=True)

print(r32)