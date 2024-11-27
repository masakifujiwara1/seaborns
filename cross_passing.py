import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# データの準備
data = {
    'Category': ['Execution Time', 'Execution Time', 'Execution Dist', 'Execution Dist', 'Min. Dist. Person 1', 'Min. Dist. Person 1', 'TTC', 'TTC'],
    'Group': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [15.10, 23.18, 7.46, 7.52, 0.11, 1.16, 0.18, 3.13],
    'Error': [0.058, 10.4, 0.017, 0.1, 0.018, 0.5, 0.031, 1.5]
}
df = pd.DataFrame(data)

# グラフの作成
fig, axes = plt.subplots(1, 4, figsize=(7, 4))

categories = ['Execution Time', 'Execution Dist', 'Min. Dist. Person 1', 'TTC']
ylabels = ['[s]', '[m]', '[m]', '[s]']
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