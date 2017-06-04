# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 14:56:00 2017

@author: AutuanLiu
"""

import numpy as np
import matplotlib.pyplot as plt

# test so so
plt.plot([3, 1, 4, -5, 6])
plt.ylabel("grade")
plt.savefig("test",  dpi = 600)
plt.show()

def f(x):
    return np.exp(-x) * np.cos(2 * np.pi * x)
a = np.arange(0, 5, .02)
plt.subplot(2, 1, 1)
plt.plot(a, f(a))

plt.subplot(2, 1, 2)
plt.plot(a, np.cos(2 * np.pi * a), 'r--')
plt.show()

# plot multi image
plt.plot(a, np.sin(a), a, np.sinh(a), a, np.exp(a), a, a ** 3)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()


