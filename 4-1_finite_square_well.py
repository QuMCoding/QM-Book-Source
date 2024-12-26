import matplotlib.pyplot as plt
import numpy as np

def potential(x):
    global V0, well_start, well_end
    return 0. if well_start <= x <= well_end else V0

def wave_function(a, b, num_points, energy, psi_start, psi_next, potential_func):
    h = (b - a) / num_points
    h2 = h ** 2
    psi_0 = psi_start
    psi_1 = psi_next
    for i in range(num_points):
        x = a + h * i
        k_squared = 2. * (energy - potential_func(x))
        psi_2 = 2. * psi_1 - psi_0 - k_squared * psi_1 * h2
        psi_0 = psi_1
        psi_1 = psi_2
    return psi_1

def shoot(a, b, num_points, energy_low, energy_high, psi_start, psi_next, potential_func):
    E1, E2 = energy_low, energy_high
    for _ in range(120):
        psi1 = wave_function(a, b, num_points, E1, psi_start, psi_next, potential_func)
        psi2 = wave_function(a, b, num_points, E2, psi_start, psi_next, potential_func)
        if (psi1 - psi_start) * (psi2 - psi_start) > 0.:
            return E1, E2
        else:
            E_mid = (E1 + E2) / 2.
            psi_mid = wave_function(a, b, num_points, E_mid, psi_start, psi_next, potential_func)
            if (psi_mid - psi_start) * (psi1 - psi_start) < 0.:
                E2 = E_mid
            else:
                E1 = E_mid
    return E1, E2

def compute_wave_function(a, b, num_points, energy, psi_start, psi_next, potential_func):
    h = (b - a) / num_points
    h2 = h ** 2
    psi_0 = psi_start
    psi_1 = psi_next
    wave_func = [psi_0, psi_1]
    x_values = [a, a + h]
    for i in range(num_points):
        x = a + h * i
        k_squared = 2. * (energy - potential_func(x))
        psi_2 = 2. * psi_1 - psi_0 - k_squared * psi_1 * h2
        psi_0 = psi_1
        psi_1 = psi_2
        wave_func.append(psi_2)
        x_values.append(x + h)
    norm = np.sqrt(np.sum(np.array(wave_func) ** 2) * h)
    wave_func = np.array(wave_func) / norm
    return wave_func, x_values

###############################----main---------------

V0 = 250  # Potential well depth
well_start, well_end = 0., 1.  # Well boundaries
a, b = well_start - 1.00, well_end + 1.00  # Integration boundaries
num_points = 1000  # Number of points for integration
h = (b - a) / num_points
psi_start, psi_next = 1.E-10 * np.exp(-(a) ** 2), 1.E-10 * np.exp(-(a + h) ** 2)

# ======shoot eigen-energies====
energies = np.linspace(0, 600, 1200)
eigen_energies = []
num_eigenvalues = 8
accuracy = 1.e-3
previous_energy = 0
for i in range(len(energies) - 1):
    if len(eigen_energies) == num_eigenvalues:
        break
    E1, E2 = shoot(a, b, num_points, energies[i], energies[i + 1], psi_start, psi_next, potential)
    if (previous_energy == 0) and (abs((E1 - E2) / E2) < accuracy):
        eigen_energies.append((E1 + E2) / 2.)
        previous_energy = (E1 + E2) / 2.
        continue
    if abs((E1 - E2) / E2) < accuracy and (E1 + E2) / 2. - previous_energy > 0.1:
        eigen_energies.append((E1 + E2) / 2.)
        previous_energy = (E1 + E2) / 2.

# 指定要畫出的波函數的量子數 n
n = 1  # 例如，畫出 n=1 的波函數

# 計算波函數
wave_func, x_values = compute_wave_function(a, b, num_points, eigen_energies[n-1], psi_start, psi_next, potential)

# 畫圖
plt.figure()
plt.plot(x_values, wave_func, label=f'n={n}')
plt.title(f'$\Psi_{n}(x)$ 1D finite square well V0=' + str(V0))
plt.legend()
plt.show()
