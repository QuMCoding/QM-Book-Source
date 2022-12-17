from matplotlib import pyplot as plt
import numpy as np

lim_top = 1e-16
lim_bottom = -1e-16
lim_total = 1000
hbar = 6.62607015e-34


def new_shot(xes):
    # a = lim_top - lim_bottom
    # p = xes
    # psi_p ** 2 = (a/(2*pi*hbar)) * (1+cos(p*a/hbar))
    a = lim_top - lim_bottom
    prob = (a / (2 * np.pi * hbar)) * (1. + np.cos(xes * a / hbar))
    _x = np.random.choice(xes, lim_total, p=prob/np.sum(prob))
    plt.scatter(_x, np.random.uniform(lim_bottom, lim_top, _x.shape), s=0.1)


new_shot(np.linspace(lim_bottom, lim_top, 1000))
plt.show()
