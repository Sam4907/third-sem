import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")

rounds=['Round of 32', 'Round of 16', 'Quarter-Finals', 'Semi-Finals', 'Finals']
initial_acc=[35.535, 18.792, 58.625, 66.783, 78.406]
corrected_acc=[13.365, 23.976, 80.107, 66.783, 78.406]
df_melted=pd.DataFrame({
    'Round':rounds*2,
    'Accuracy (%)':initial_acc+corrected_acc,
    'Type':['Predicted Bracket']*5+['Corrected Bracket']*5
})

df_melted['Round']=pd.Categorical(df_melted['Round'], categories=rounds, ordered=True)

plt.figure(figsize=(10, 6))
ax=sns.barplot(
    data=df_melted, 
    x='Round', 
    y='Accuracy (%)', 
    hue='Type', 
    palette='deep'
)

plt.title('Tournament Bracket Prediction Accuracy Across Rounds', fontsize=14, pad=15, weight='bold')
plt.xlabel('Tournament Round', fontsize=11, labelpad=10)
plt.ylabel('Probability / Accuracy (%)', fontsize=11, labelpad=10)
plt.ylim(0, 100)

for p in ax.patches:
    height=p.get_height()
    if not np.isnan(height) and height>0:
        ax.annotate(
            f'{height:.2f}%',
            xy=(p.get_x()+p.get_width()/2, height),
            xytext=(0, 4),  
            textcoords="offset points",
            ha='center', va='bottom', fontsize=9, weight='semibold'
        )

plt.legend(title='Bracket State', frameon=True, facecolor='white', framealpha=0.9)
sns.despine(left=True)
plt.tight_layout()
plt.show()