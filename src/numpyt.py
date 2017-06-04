# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 17:12:45 2017

@author: AutuanLiu
"""

import numpy as np
def matsum():
    a = np.array([1, 2, 4, -6, 7])
    b = np.array([2, 4, 5, -3, 5])
    t = a ** 2 + b ** 3
    return t
result = matsum()
print("the result is: ", result)