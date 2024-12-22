from math import gcd
from random import randint

def pollards_rho(N):
    if N % 2 == 0:
        return 2
    x = randint(2, N - 1)
    y = x
    c = randint(1, N - 1)
    d = 1
    def f(x):
        return (x**2 + c) % N
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), N)
        if d == N:
            return None  # 失敗
    return d

if __name__ == "__main__":
    N = 48684872256281844078953879  # 要質因數分解的數
    print(f"正在用Pollard's rho算法分解{N}的質因數...")
    factor = pollards_rho(N)
    if factor:
        print(f"找到質因數: {factor}, {N // factor}")
    else:
        print("沒有質因數")
