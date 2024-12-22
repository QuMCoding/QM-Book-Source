import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def bloch_sphere(theta, phi):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')    
    # 創建球體網格
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    # 畫出球體
    ax.plot_surface(x, y, z, color='b', alpha=0.1)
    # 畫出量子態向量
    ax.quiver(0, 0, 0, np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta), color='r', linewidth=2)
    # 使用虛線標示座標軸
    ax.plot([0, 1], [0, 0], [0, 0], color='g', linestyle='--', linewidth=2)  # X軸
    ax.plot([0, 0], [0, 1], [0, 0], color='y', linestyle='--', linewidth=2)  # Y軸
    ax.plot([0, 0], [0, 0], [0, 1], color='b', linestyle='--', linewidth=2)  # Z軸
    # 設置座標軸範圍
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    # 設置座標軸標籤
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def main():
    # 使用者輸入量子態 |0> 和 |1> 的實部和虛部
    real_0 = float(input("請輸入 |0> 的實部: "))
    imag_0 = float(input("請輸入 |0> 的虛部: "))
    real_1 = float(input("請輸入 |1> 的實部: "))
    imag_1 = float(input("請輸入 |1> 的虛部: "))
    # 計算量子態的 theta 和 phi 參數
    # 量子態為 |ψ> = α|0> + β|1>, α = real_0 + i*imag_0, β = real_1 + i*imag_1
    alpha = complex(real_0, imag_0)
    beta = complex(real_1, imag_1)
    # 計算 theta 和 phi
    theta = 2 * np.arccos(abs(alpha))  # theta = 2 * acos(|α|)
    phi = np.angle(beta) - np.angle(alpha)  # phi = angle(β) - angle(α)
    # 顯示Bloch球
    bloch_sphere(theta, phi)

if __name__ == "__main__":
    main()
