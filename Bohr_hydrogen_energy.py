import numpy as np
import matplotlib.pyplot as plt

# 定義氫原子能量公式
def hydrogen_energy(n):
    return -13.6 / (n ** 2)
# 設定n的範圍
n_values = np.arange(1, 10)  # 計算n=1到n=6的能級
# 計算每個能階的能量
energy_values = [hydrogen_energy(n) for n in n_values]
# 用戶輸入主量子數n1和n2
n1 = int(input("輸入初始主量子數(n1):"))
n2 = int(input("輸入躍遷到的主量子數(n2):"))
# 計算能量變化
delta_E = hydrogen_energy(n2) - hydrogen_energy(n1)
# 畫出能階圖
plt.figure(figsize=(8, 6))
# 畫能階線
for n, energy in zip(n_values, energy_values):
    plt.plot([0, 1], [energy, energy], label=f"n={n}", color='black')
    plt.text(1.025, energy, f"n={n}", color='black')
# 畫箭頭表示電子躍遷
plt.arrow(0.5, hydrogen_energy(n1), 0, hydrogen_energy(n2) - hydrogen_energy(n1)-0.3,
          head_width=0.02, head_length=0.3, fc='blue', ec='blue')
# 標註箭頭和能量差
plt.text(0.7, (hydrogen_energy(n1) + hydrogen_energy(n2)) / 2, f"ΔE = {delta_E:.2f} eV", color='blue')
plt.xticks([])
# 設置標籤
plt.xlim(0, 1)
plt.ylim(min(energy_values) - 1, max(energy_values) + 1)
plt.xlabel('Energy Level (n)')
plt.ylabel('Energy (eV)')
plt.title('Hydrogen Atom Energy Levels and Transition')
# 顯示圖形
plt.grid(True)
plt.show()
