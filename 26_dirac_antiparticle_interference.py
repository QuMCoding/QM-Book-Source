import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 常數
hbar = 1.0  # 簡化普朗克常數
m = 1.0     # 粒子質量
c = 1.0     # 光速
# 空間和時間參數
x = np.linspace(-10, 10, 1000)  # 空間範圍
t = np.linspace(0, 20, 500)    # 時間範圍
# 粒子與反粒子波包參數
k_p = 1.0  # 正能量波數
k_n = -1.0 # 負能量波數
omega_p = np.sqrt((k_p * c)**2 + (m * c**2)**2) / hbar  # 正能量頻率
omega_n = -np.sqrt((k_n * c)**2 + (m * c**2)**2) / hbar # 負能量頻率
# 初始波包形狀
def wave_packet(x, k):
    return np.exp(-x**2) * np.exp(1j * k * x)
psi_p = wave_packet(x, k_p)  # 正能量波包
psi_n = wave_packet(x, k_n)  # 負能量波包
# 動畫函數
def update(frame):
    global line_real, line_imag, line_abs
    t_val = t[frame]
    # 正能量解和負能量解隨時間的演化
    psi_p_t = psi_p * np.exp(-1j * omega_p * t_val)
    psi_n_t = psi_n * np.exp(-1j * omega_n * t_val)
    # 總波函數
    psi_total = psi_p_t + psi_n_t
    # 更新數據
    line_real.set_ydata(np.real(psi_total))
    line_imag.set_ydata(np.imag(psi_total))
    line_abs.set_ydata(np.abs(psi_total))
    return line_real, line_imag, line_abs

# 初始化圖形
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-2, 2)
ax.set_title("Particle-Antiparticle Interference")
ax.set_xlabel("x")
ax.set_ylabel("Wavefunction")
line_real, = ax.plot(x, np.zeros_like(x), label="Real Part", color="blue")
line_imag, = ax.plot(x, np.zeros_like(x), label="Imaginary Part", color="red")
line_abs, = ax.plot(x, np.zeros_like(x), label="Magnitude", color="green")
ax.legend()
# 動畫
ani = FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)
# 顯示動畫
plt.show()
