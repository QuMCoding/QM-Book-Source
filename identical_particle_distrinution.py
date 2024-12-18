from math import comb

n = int(input("盒子數量:"))
m = int(input("粒子數量:"))

normal = n ** m
quantum = comb(n + m - 1, m - 1)

print(f"古典機率: 1/{normal}; 全同粒子機率: 1/{quantum}")
