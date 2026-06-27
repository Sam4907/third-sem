import pandas as pd
import numpy as np
import itertools
from scipy.stats import poisson

df=pd.read_csv("../Data/F.csv")
stats=pd.read_csv("../Data/xg.csv", index_col="country")

fixt={97: 98, 99: 100}

sf_to_f_mapping={
    97: 101, 98: 101,  
    99: 102, 100: 102
}

outcomes=[[teama, teamb] for teama, teamb in fixt.items()]
results=list(itertools.product(*outcomes))

#assinging universe probabilities
stats['xg_per_game']=stats['xg']/2
stats['ga_per_game']=stats['ga']/2
avg_tournament_xg=stats['xg_per_game'].mean()
stats['att_strength']=stats['xg_per_game']/avg_tournament_xg
stats['defe_weakness']=stats['ga_per_game']/avg_tournament_xg

def compute_match_odds(team_a, team_b, elo_a, elo_b):
    att_a=stats.loc[team_a, 'att_strength'] if team_a in stats.index else 1.0
    defe_a=stats.loc[team_a, 'defe_weakness'] if team_a in stats.index else 1.0
    att_b=stats.loc[team_b, 'att_strength'] if team_b in stats.index else 1.0
    defe_b=stats.loc[team_b, 'defe_weakness'] if team_b in stats.index else 1.0
    elo_diff=elo_a-elo_b
    elo_multiplier=10**(elo_diff/400)
    dampened_modifier=np.sqrt(elo_multiplier)
    lambda_a=att_a*defe_b*avg_tournament_xg*dampened_modifier
    lambda_b=att_b*defe_a*avg_tournament_xg/dampened_modifier
    max_goals=6
    grid=np.zeros((max_goals, max_goals))
    for a in range(max_goals):
        for b in range(max_goals):
            grid[a, b]=poisson.pmf(a, lambda_a)*poisson.pmf(b, lambda_b)
    win_a=np.sum(np.tril(grid, -1).T)
    win_b=np.sum(np.triu(grid, 1).T)
    total=win_a + win_b
    return win_a/total, win_b/total

match_probs={}
for teama, teamb in fixt.items():
    team_a_name=df.loc[df['num']==teama, 'team'].item()
    team_a_elo=df.loc[df['num']==teama, 'elo'].item()
    team_b_name=df.loc[df['num']==teamb, 'team'].item()
    team_b_elo=df.loc[df['num']==teamb, 'elo'].item()
    prob_a, prob_b=compute_match_odds(team_a_name, team_b_name, team_a_elo, team_b_elo)
    match_probs[teama]=prob_a
    match_probs[teamb]=prob_b

universe_weights=[]
for r in results:
    universe_prob=1.0
    for winner in r:
        universe_prob*=match_probs[winner]
    universe_weights.append((r, universe_prob))

most_probable_universe=max(universe_weights, key=lambda x: x[1])
best_bracket=most_probable_universe[0]
best_prob=most_probable_universe[1]

print(f"{best_prob:.3%}")
winners_rows=[]
for teama, teamb in fixt.items():
    team_a_name=df.loc[df['num']==teama, 'team'].item()
    team_b_name=df.loc[df['num']==teamb, 'team'].item()
    winner_name=team_a_name if teama in best_bracket else team_b_name
    print(f"{team_a_name} vs {team_b_name}::WINNER: {winner_name}")
    winner_row=df[df['team']==winner_name].copy()
    winner_row['num']=sf_to_f_mapping.get(teama)
    winners_rows.append(winner_row)

sf_df=pd.concat(winners_rows, ignore_index=True)
sf_df.to_csv('../Data/W.csv', index=False)
print(f"\n2 finalists exported to '../Data/W.csv'")