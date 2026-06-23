import pandas as pd
import itertools
import numpy as np

df=pd.read_csv("groupb.csv")

odds1=np.array([11/10, 5/2, 11/4])
odds2=np.array([1.44, 4.60, 7.00])
odds1=1/odds1
odds1=odds1/np.sum(odds1)
odds2=1/odds2
odds2=odds2/np.sum(odds2)

match1_probs={'can':odds1[0], 'sui':odds1[1], 'tie':odds1[2]}
match2_probs={'bih':odds2[0], 'qat':odds2[1], 'tie':odds2[2]}

rem=[[df.iloc[0, 0], df.iloc[1, 0]], [df.iloc[2, 0], df.iloc[3, 0]]]
rea1=list(next(zip(*itertools.permutations(rem[0]))))
rea1.append('tie')
rea2=list(next(zip(*itertools.permutations(rem[1]))))
rea2.append('tie')
result=list(itertools.product(rea1, rea2))

def win(curr, winner, loser):
        curr.loc[curr['team']==winner, 'pts']+=3
        curr.loc[curr['team']==winner, ['w', 'gf', 'gd']]+=1
        curr.loc[curr['team']==loser, ['l', 'ga']]+=1
        curr.loc[curr['team']==loser, 'gd']-=1

def draw(curr, on):
    curr.loc[curr['team']==on[0], ['pts', 'd']]+=1
    curr.loc[curr['team']==on[1], ['pts', 'd']]+=1


for i in result:
    curr=df.copy()
    universe_probs=match1_probs[i[0]]*match2_probs[i[1]]
    curr['mp']+=1
    if(i[0]=='tie'):
        draw(curr, rem[0])
    elif(i[0]==rem[0][0]):
        win(curr, rem[0][0], rem[0][1])
    else:
        win(curr, rem[0][1], rem[0][0])
    if(i[1]=='tie'):
        draw(curr, rem[1])
    elif(i[1]==rem[1][0]):
        win(curr, rem[1][0], rem[1][1])
    else:
        win(curr, rem[1][1], rem[1][0])
    print(curr.sort_values(by=['pts', 'gd'], ascending=False))
    print(f"\n{universe_probs}\n")

