import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 模擬參數(可自由調整)
size_x, size_y = 200, 100  # 畫布大小
time_steps = 500  # 要模擬幾步
slit_gap = 40  # 縫的寬度

# 常數
c = 1  # 光速
dx = 1.0  # 空間步進
dt = dx / (2 * c)  # 時間步進
# 初始化電磁場
Ez = np.zeros((size_y, size_x))  # 電場z分量
Hy = np.zeros((size_y, size_x))  # 磁場y分量
Hx = np.zeros((size_y, size_x))  # 磁場x分量

# 建構縫
slit_center = size_y // 2
slit_start = size_x // 3
slits = np.ones((size_y,), dtype=bool)
slits[:slit_center - slit_gap // 2] = False
slits[slit_center + slit_gap // 2:] = False

# 主程式
fig, ax = plt.subplots()
ims = []

for t in range(time_steps):
    # 更新磁場
    Hx[:, :-1] -= dt / dx * (Ez[:, 1:] - Ez[:, :-1])
    Hy[:-1, :] += dt / dx * (Ez[1:, :] - Ez[:-1, :])
    # 更新電場
    Ez[1:-1, 1:-1] += dt / dx * (
        (Hy[1:-1, 1:-1] - Hy[:-2, 1:-1]) - (Hx[1:-1, 1:-1] - Hx[1:-1, :-2])
    )
    # 加上狹縫
    Ez[:, slit_start] *= slits
    # 光源(高斯振波)
    Ez[size_y // 2, slit_start - 25] += np.exp(-((t - 30) / 10) ** 2)

    # 視覺化
    img = np.copy(Ez)
    img[:slit_center - slit_gap // 2, slit_start] = 10
    img[slit_center + slit_gap // 2:, slit_start] = 10
    im = ax.imshow(img, cmap="RdBu", vmin=-0.1, vmax=0.1, animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)
plt.colorbar(im, ax=ax, label="Ez Field")
plt.title("FDTD Simulation")
plt.show()
