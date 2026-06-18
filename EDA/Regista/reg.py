import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# serial,player_name,club,position,pass_accuracy,pass_attempted,pass_completed,
# cross_accuracy,cross_attempted,cross_completed,freekicks_taken,match_played
df=pd.read_csv("Midfield_Playmaking.csv")

def high_volume():
    final=df[(df["pass_accuracy"]>85)&(df["pass_attempted"]>200)]
    print(final.sort_values(by='pass_accuracy', ascending=False)[["player_name", "club", "position", "pass_accuracy", "pass_attempted", "pass_completed", "match_played"]].to_string())

def freekick_master():
    final=df.sort_values(by='freekicks_taken', ascending=False)
    print(final.head()[["player_name", "club", "freekicks_taken"]].to_string())

def unused():
    final=df[(df["match_played"]>=3)&((df["position"]=="Midfielder")|(df["position"]=="Forward"))&(df["cross_attempted"]==0)]
    print(final.sort_values(by='match_played', ascending=False)[["player_name", "club", "position", "match_played"]].to_string())

def cross_audit():
    final=df[(df["cross_completed"]!=0)&(df["cross_attempted"]!=0)]
    final["calculated"]=final["cross_completed"]*100/final["cross_attempted"]
    jf=final[(final["calculated"]-final["cross_accuracy"])>0.8]
    print(jf[["player_name", "club", "calculated", "cross_accuracy"]])

def pass_per_match():
    final=df[(df["pass_completed"]!=0)&(df["match_played"]!=0)]
    final["calculated"]=final["pass_completed"]/final["match_played"]
    final=final.sort_values(by='calculated', ascending=False)[final["match_played"]>=5]
    print(final[0:3][["player_name", "club", "calculated", "pass_completed", "match_played"]])

def blind_crosser():
    final=df[(df["pass_attempted"]!=0)&(df["cross_attempted"]!=0)]
    final=final[final["cross_attempted"]>0.2*final["pass_attempted"]]
    print(final[["player_name", "club", "cross_attempted", "pass_attempted", "match_played"]])

def team_pass():
    final=df.groupby("club")
    jf=final[["pass_attempted", "pass_completed"]].sum(numeric_only=True)
    jf["calculated"]=jf["pass_completed"]*100/jf["pass_attempted"]
    print(jf.sort_values(by='calculated', ascending=False))

def position_pass():
    final=df.groupby("position").agg({
    'pass_accuracy':'mean',        
    'pass_attempted':'max',        
    })
    print(final)

def outlier_check():
    print(df[df["pass_completed"]>df["pass_attempted"]]) #results in empty dataframe

def final_boss():
    final=df[(df["match_played"]>=5)&((df["pass_completed"]/df["match_played"])>50)&(df["pass_accuracy"]>88)&(df["cross_attempted"]<5)]
    print(final.sort_values(by="match_played", ascending=False)[["player_name", "club", "position", "pass_accuracy", "match_played"]])

# grouped consistency index
def gci():
    df["mean"]=df.groupby("position")["pass_completed"].transform("mean")
    df["STD"]=df.groupby("position")["pass_completed"].transform("std")
    df["zs"]=(df["pass_completed"]-df["mean"])/df["STD"]
    print(df.sort_values(by="zs", ascending=False)[["player_name", "position", "pass_completed", "zs"]].to_string())

def club_perc():
    df['rank']=df.groupby("club")['pass_completed'].rank(pct=True)
    jf=df[df["rank"]>0.85]
    print(jf.sort_values(by="position", ascending=False)[["player_name", "club", "position", "pass_completed", "rank"]])

'''
high_volume()
freekick_master()
unused()
cross_audit()
pass_per_match
blind_crosser()
team_pass()
position_pass()
outlier_check()
final_boss()
gci()
club_perc()
'''

def custom_theme():
    plt.rcParams['figure.facecolor'] = '#0b0c10'
    plt.rcParams['axes.facecolor'] = '#0b0c10'
    plt.rcParams['text.color'] = '#ffffff'
    plt.rcParams['axes.labelcolor'] = '#ffffff'
    plt.rcParams['xtick.color'] = '#c5c5c5'
    plt.rcParams['ytick.color'] = '#c5c5c5'
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.color'] = '#1f2833'
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.alpha'] = 0.5
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    sns.set_context("talk")

def plot_final_boss():
    custom_theme()
    df["GROUP_MEAN"] = df.groupby("position")["pass_completed"].transform("mean")
    df["GROUP_STD"] = df.groupby("position")["pass_completed"].transform("std")
    df["Z_SCORE"] = (df["pass_completed"] - df["GROUP_MEAN"]) / df["GROUP_STD"]
    plt.figure(figsize=(12, 7))
    custom_palette = {"Midfielder": "#00f5ff", "Forward": "#ff007f", "Defender": "#39ff14", "Goalkeeper": "#f0db51"}
    ax = sns.scatterplot(
        data=df,
        x='pass_attempted',
        y='pass_completed',
        hue='position',
        size='Z_SCORE',
        sizes=(20, 300),        
        palette=custom_palette,
        alpha=0.85
    )
    elites=df[df['Z_SCORE']>4.0]
    for _, player in elites.iterrows():
        plt.text(
            x=player['pass_attempted']+12,
            y=player['pass_completed']-5,
            s=f"{player['player_name']} (Z: {player['Z_SCORE']:.2f})",
            color='#39ff14',      
            fontweight='semibold',
            fontsize=8
        ) 
    plt.title("UCL PLAYMAKERS", fontsize=16, fontweight='bold', pad=20, color='#00f5ff')
    plt.xlabel("Passes Attempted", fontsize=12, fontweight='semibold')
    plt.ylabel("Passes Completed", fontsize=12, fontweight='semibold')
    legend=plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True)
    legend.get_frame().set_facecolor('#121212')
    legend.get_frame().set_edgecolor('#1f2833')
    for text in legend.get_texts():
        text.set_color('#ffffff')
    plt.tight_layout()
    plt.savefig("final_boss.png", dpi=300)
    plt.show()

def inner_view():
    sns.violinplot(data=df, x="position", y="pass_completed", hue="position", inner='sticks')
    plt.savefig("violinplot.png", dpi=300)
    plt.show()

def club_master():
    final=df.groupby(["club", "position"])["pass_completed"].mean().astype(int).unstack()
    top=final.loc[df.groupby("club")["pass_completed"].sum().nlargest(10).index]
    sns.heatmap(data=top, annot=True, cmap='rocket', fmt='d')
    plt.tight_layout()
    plt.show()

plot_final_boss()
inner_view()
club_master()