import matplotlib.pyplot as plt
import numpy as np

# 此處為可以修改的參數
NEIG = 4  # 要計算的能量狀態數
# V0 是方形阱的深度，sqa 和 sqb 是方形阱的左右邊界
V0, sqa, sqb = 250, 0., 1.
# 以下為計算的函數

def V_pot(x):
    return 0. if sqa <= x <= sqb else V0

def psi_r(a, b, Nh, E, psi_00, psi_01, V):
    h = (b - a) / Nh
    h2 = h ** 2
    psi_0 = psi_00
    psi_1 = psi_01
    for i in range(Nh):
        x = a + h * i
        ksq = 2. * (E - V(x))
        psi_2 = 2. * psi_1 - psi_0 - ksq * psi_1 * h2
        psi_0 = psi_1
        psi_1 = psi_2
    return psi_1
def Shoot(a, b, Nh, Ea, Eb, psi_00, psi_01, V):
    E1, E2 = Ea, Eb
    for _ in range(120):
        ps1 = psi_r(a, b, Nh, E1, psi_00, psi_01, V)
        ps2 = psi_r(a, b, Nh, E2, psi_00, psi_01, V)
        if (ps1 - psi_00) * (ps2 - psi_00) > 0.:
            return E1, E2
        else:
            E_mid = (E1 + E2) / 2.
            pst = psi_r(a, b, Nh, E_mid, psi_00, psi_01, V)
            if (pst - psi_00) * (ps1 - psi_00) < 0.:
                E2 = E_mid
            else:
                E1 = E_mid
    return E1, E2
def PsiE(a, b, Nh, E, psi_00, psi_01, V):
    h = (b - a) / Nh
    h2 = h ** 2
    psi_0 = psi_00
    psi_1 = psi_01
    Psi = [psi_0, psi_1]
    xa = [a, a + h]
    for i in range(Nh):
        x = a + h * i
        ksq = 2. * (E - V(x))
        psi_2 = 2. * psi_1 - psi_0 - ksq * psi_1 * h2
        psi_0 = psi_1
        psi_1 = psi_2
        Psi.append(psi_2)
        xa.append(x + h)
    norm = np.sqrt(np.sum(np.array(Psi) ** 2) * h)
    Psi = np.array(Psi) / norm
    return Psi, xa

a, b = sqa - 1.00, sqb + 1.00
Nh = 1000
h = (b - a) / Nh
psi_00, psi_01 = 1.E-10 * np.exp(-(a) ** 2), 1.E-10 * np.exp(-(a + h) ** 2)
ENERGY_LEVELS = np.linspace(0, 600, 1200)
Energy_list = []
accuracy = 1.e-3
KK = 0
for i in range(len(ENERGY_LEVELS) - 1):
    if len(Energy_list) == NEIG:
        break
    E1, E2 = Shoot(a, b, Nh, ENERGY_LEVELS[i], ENERGY_LEVELS[i + 1], psi_00, psi_01, V_pot)
    if (KK == 0) and (abs((E1 - E2) / E2) < accuracy):
        Energy_list.append((E1 + E2) / 2.)
        Ep = (E1 + E2) / 2.
        KK = 1
        continue
    if abs((E1 - E2) / E2) < accuracy and (E1 + E2) / 2. - Ep > 0.1:
        Energy_list.append((E1 + E2) / 2.)
        Ep = (E1 + E2) / 2.
# 計算波函數
Psi = []
xa = []
for E in Energy_list:
    psi, x = PsiE(a, b, Nh, E, psi_00, psi_01, V_pot)
    Psi.append(psi)
    xa.append(x)

# 畫圖
plt.figure()
for i in range(len(Psi)):
    plt.plot(xa[i], Psi[i] + i * 3.5, label=f'n={i+1}')
plt.axvline(sqa, color='k', linestyle='-')  # 畫出方形阱的左邊界
plt.axvline(sqb, color='k', linestyle='-')  # 畫出方形阱的右邊界
plt.title('$\Psi_n(x)$ 1D finite square well $V_0$=' + str(V0))
plt.legend()
plt.show()
