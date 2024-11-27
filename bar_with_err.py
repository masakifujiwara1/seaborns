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
fig, axes = plt.subplots(1, 3, figsize=(7, 4))

categories = ['Execution Time', 'Path Length', 'Min. Dist. Person 1']
ylabels = ['[s]', '[m]', '[m]']
edgecolors = ['blue', 'red']  # 縁の色を定義
errorbar_colors = ['blue', 'red'] # エラーバーの色を定義

for i, category in enumerate(categories):
    ax = axes[i]

    # linewidthとedgecolorを追加
    barplot = sns.barplot(x='Group', y='Value', hue='Group', data=df[df['Category'] == category], ax=ax, 
                           palette=['blue', 'red'], alpha=1, linewidth=2, edgecolor='k', err_kws={'linewidth': 1}, capsize=0.1, legend=False)


    # patchesを使って個別に縁の色を設定
    for j, patch in enumerate(barplot.patches):
        patch.set_edgecolor(edgecolors[j % len(edgecolors)]) # jをedgecolorsの長さで割った余りで色を決定
        patch.set_alpha(0.3)

        patch.set_facecolor(patch.get_facecolor()) # 色を再設定することでalphaが適用される
        patch.set_alpha(0.3) # 塗りつぶしのalpha値

    # エラーバーを手動で追加
    for j, group in enumerate(['A','B']):
      value = df[(df['Category'] == category) & (df['Group'] == group)]['Value'].values[0]
      error = df[(df['Category'] == category) & (df['Group'] == group)]['Error'].values[0]
      ax.errorbar(x=j, y=value, yerr=error, color=errorbar_colors[j], capsize=5, capthick=1)

    ax.set_xlabel(category.replace(' ', '\n'), fontsize=12)
    ax.set_ylabel(ylabels[i], fontsize=12)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['A', 'B'])  # x軸の目盛りラベルを修正


plt.tight_layout()
plt.show()