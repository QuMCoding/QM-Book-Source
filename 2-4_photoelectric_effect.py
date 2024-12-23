import numpy as np
import matplotlib.pyplot as plt

# 定義常數
h = 6.626e-34  # 普朗克常數 (J·s)
e = 1.602e-19  # 電子電量 (C)
c = 3.0e8      # 光速 (m/s)
# 模擬的金屬逸出功 (電子伏特)
metal_work_functions = {
    "Sodium": 2.3,  # eV
    "Copper": 4.7,  # eV
    "Platinum": 5.6  # eV
}
# 光的頻率範圍 (Hz)
frequencies = np.linspace(1e14, 4e15, 500)
# 計算動能的函數
def calculate_kinetic_energy(frequency, work_function):
    photon_energy = h * frequency / e  # 光子能量 (eV)
    kinetic_energy = np.maximum(photon_energy - work_function, 0)  # 動能 (eV)
    return kinetic_energy
# 可視化
plt.figure(figsize=(10, 6))
for metal, work_function in metal_work_functions.items():
    kinetic_energies = calculate_kinetic_energy(frequencies, work_function)
    plt.plot(frequencies, kinetic_energies, label=f"{metal} (W = {work_function} eV)")

plt.title("Photoelectric Effect: Kinetic Energy vs Frequency")
plt.xlabel("Frequency of Light (Hz)")
plt.ylabel("Kinetic Energy of Electrons (eV)")
plt.legend()
plt.grid(True)
plt.show()
