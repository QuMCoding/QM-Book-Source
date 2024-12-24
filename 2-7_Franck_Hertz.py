import matplotlib.pyplot as plt
import numpy as np

# 定義氖原子的能級
energy_levels = [0, 16.6, 33.2, 49.8]  # 單位：電子伏特（eV）
# 畫出能級圖
fig, ax = plt.subplots(figsize=(6, 4))
# 繪製能級線
for energy in energy_levels:
    ax.plot([0, 1], [energy, energy], color='b', lw=2)
    ax.text(1.05, energy, f'{energy} eV', verticalalignment='center', fontsize=12)
# 標示電子加速能量範圍
ax.plot([0, 1], [10, 10], color='r', lw=2, linestyle='--')  # 假設的加速能量（如10 eV）
ax.text(1.05, 10, 'Accelerated Electron Energy', verticalalignment='center', fontsize=12, color='r')
# 標示能量損失與激發
ax.arrow(0.5, 16.6, 0, 4, head_width=0.1, head_length=1, fc='g', ec='g')  # 能量損失，從電子到原子
ax.text(1.05, 18.8, 'Energy Transfer to Atom', verticalalignment='center', fontsize=12, color='g')
# 設定圖形屬性
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 60)
ax.set_xticks([])
ax.set_yticks(energy_levels)
# 圖表標題與描述
ax.set_title("Franck-Hertz Experiment: Energy Levels", fontsize=14)
ax.set_xlabel("Position", fontsize=12)
ax.set_ylabel("Energy (eV)", fontsize=12)
# 顯示圖形
plt.tight_layout()
plt.show()
