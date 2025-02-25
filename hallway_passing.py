import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# データの準備
data = {
    'Category': ['Execution Time', 'Execution Time', 'Execution Dist', 'Execution Dist', 'Min.Dist. Person1', 'Min.Dist. Person1', 'Min.Dist. Person2', 'Min.Dist. Person2', 'Min.TTC Person1', 'Min.TTC Person1', 'Min.TTC Person2', 'Min.TTC Person2'],
    'Group': ['Normal', 'Prediction', 'Normal', 'Prediction', 'Normal', 'Prediction', 'Normal', 'Prediction', 'Normal', 'Prediction', 'Normal', 'Prediction'],
    'Value': [16.50, 24.39, 6.66, 6.75, 0.38, 0.70, 1.02, 0.90, 1.16, 1.56, 1.76, 1.90],
    'Error': [0.687, 3.88, 0.054, 0.08, 0.018, 0.22, 0.021, 0.26, 0.126, 0.29, 0.031, 0.46]
}
df = pd.DataFrame(data)

# グラフの作成
fig, axes = plt.subplots(1, 6, figsize=(12, 6))

categories = ['Execution Time', 'Execution Dist', 'Min.Dist. Person1', 'Min.Dist. Person2', 'Min.TTC Person1', 'Min.TTC Person2']
ylabels = ['[s]', '[m]', '[m]', '[m]', '[s]', '[s]']
edgecolors = ['blue', 'red']  # 縁の色を定義
errorbar_colors = ['blue', 'red'] # エラーバーの色を定義
ylim_values = [(0, 42), (0, 8), (0, 2.8), (0, 2.8), (0, 5.0), (0, 5.0)] 

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
    for j, group in enumerate(['Normal','Prediction']):
      value = df[(df['Category'] == category) & (df['Group'] == group)]['Value'].values[0]
      error = df[(df['Category'] == category) & (df['Group'] == group)]['Error'].values[0]
      ax.errorbar(x=j, y=value, yerr=error, color=errorbar_colors[j], capsize=5, capthick=1)

    ax.set_xlabel(category.replace(' ', '\n'), fontsize=12)
    ax.set_ylabel(ylabels[i], fontsize=12)
    if not(ylim_values[i] == None):
        ax.set_ylim(ylim_values[i])
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Normal', 'Prediction'])  # x軸の目盛りラベルを修正


plt.tight_layout()
plt.show()
