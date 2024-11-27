import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# データの準備
data = {
    'Category': ['Execution Time', 'Execution Time', 'Path Length', 'Path Length', 'Min. Dist. Person 1', 'Min. Dist. Person 1'],
    'Group': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [21, 18, 7, 6, 1, 0.8],
    'Error': [2, 2, 1, 0.5, 0.2, 0.2]
}
df = pd.DataFrame(data)

# グラフの作成
fig, axes = plt.subplots(1, 3, figsize=(7, 4))  # 1行3列のサブプロットを作成

categories = ['Execution Time', 'Path Length', 'Min. Dist. Person 1']
ylabels = ['[s]', '[m]', '[m]']

for i, category in enumerate(categories):
    ax = axes[i]
    sns.barplot(x='Group', y='Value', hue='Group', data=df[df['Category'] == category], ax=ax, palette=['blue', 'red'], alpha=0.5, err_kws={'linewidth': 1}, capsize=0.1, legend=False)

    # エラーバーを手動で追加
    for j, group in enumerate(['A','B']):
      value = df[(df['Category'] == category) & (df['Group'] == group)]['Value'].values[0]
      error = df[(df['Category'] == category) & (df['Group'] == group)]['Error'].values[0]
      ax.errorbar(x=j, y=value, yerr=error, color='black', capsize=5, capthick=1)


    ax.set_xlabel(category.replace(' ', '\n'), fontsize=12)  # x軸ラベルを複数行に
    ax.set_ylabel(ylabels[i], fontsize=12)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['A', 'B'])  # x軸の目盛りラベルを修正


plt.tight_layout()  # グラフ間の余白を調整
plt.show()