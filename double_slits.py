# 雙狹縫干涉實驗模擬
from matplotlib import pyplot as plt  # 可以繪製統計圖
import numpy as np  # 用於向量與矩陣運算

# 常數定義
lim_top = 1e-16  # 定義模擬圖的左邊界
lim_bottom = -lim_top  # 定義模擬圖的右邊界
hbar = 6.62607015e-34  # 普朗克常數


def new_shot_wave(dots=1000):
    """多射dots顆電子"""
    # a = lim_top - lim_bottom
    # p = xes
    # psi_p ** 2 = (a/(2*pi*hbar)) * (1+cos(p*a/hbar))
    plt.xlim((lim_top, lim_bottom))
    xes = np.linspace(lim_bottom, lim_top, 1000)  # 定義可以射到的x軸位置，為lim_bottom~lim_top之間平分1000個點
    a = lim_top - lim_bottom  # 計算可射處總長度
    prob = (a / (2 * np.pi * hbar)) * (1. + np.cos(xes * a / hbar))  # 計算射到每個點的機率
    _x = np.random.choice(xes, dots, p=prob / np.sum(prob))  # 計算射到的點
    # 畫上去，並將y軸座標隨機選擇
    plt.scatter(_x, np.random.uniform(lim_bottom, lim_top, _x.shape), s=0.1, c=np.zeros((len(_x),)))
    return _x


def new_shot_observed(dots=1000):
    """多射dots顆電子"""
    slit_pos = [0.2, 0.4]  # +/- 0.2~0.3 是可以射到的地方
    plt.xlim((lim_top, lim_bottom))
    xes = np.linspace(lim_bottom, lim_top, 1000)  # 定義可以射到的x軸位置，為lim_bottom~lim_top之間平分1000個點
    prob = (xes > slit_pos[0] * lim_top) & (xes < slit_pos[1] * lim_top) | \
           (xes < -slit_pos[0] * lim_top) & (xes > -slit_pos[1] * lim_top)  # 計算射到每個點的機率
    _x = np.random.choice(xes, dots, p=prob / np.sum(prob))  # 計算射到的點
    # 畫上去，並將y軸座標隨機選擇
    plt.scatter(_x, np.random.uniform(lim_bottom, lim_top, _x.shape), s=0.1, c=np.zeros((len(_x),)))
    return _x


def get_random_number(bits=1000, show_plot=True):
    plt.figure(1111)
    waved = new_shot_wave(bits)

    plt.figure(1122)
    observed = new_shot_observed(bits)

    if show_plot:
        plt.show()

    return (waved > 0) ^ (observed > 0)


rand = get_random_number(1000000, show_plot=False)
np.packbits(rand).tofile("arr")
print("".join(rand.astype(np.uint8).astype(str)))
'''
new_shot_wave(10)  # 射10個電子
plt.show()  # 畫出結果
new_shot_wave(100)  # 射100個電子
plt.show()  # 畫出結果，並清除上次的圖
new_shot_wave(1000)  # 射1000個電子
plt.show()  # 畫出結果，並清除上次的圖
new_shot_wave(10000)  # 射10000個電子
plt.show()  # 畫出結果，並清除上次的圖


new_shot_observed(10)  # 射10個電子
plt.show()  # 畫出結果
new_shot_observed(100)  # 射100個電子
plt.show()  # 畫出結果，並清除上次的圖
new_shot_observed(1000)  # 射1000個電子
plt.show()  # 畫出結果，並清除上次的圖
new_shot_observed(10000)  # 射10000個電子
plt.show()  # 畫出結果，並清除上次的圖
'''
