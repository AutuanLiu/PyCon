# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:56:53 2017

@author: AutuanLiu
"""

import pandas as pd
import numpy as np

a = pd.Series([9, 8, 7, 6])
d = pd.DataFrame(np.arange(10).reshape(2, 5))
dt = {"one": pd.Series([1, 2, 3], index = ['a', 'b', 'c']),
      "two": pd.Series([9, 8, 7, 6], index = ['a', 'b', 'c', 'd'])}
d1 = pd.DataFrame(dt)
print(d1)
print(d)
print(d1)

# from list dict create dataframe
d2 = {"one": [1, 2, 3, 4], "two": [9, 8, 7, 6]}
d3 = pd.DataFrame(d2, index = ['a', 'b', 'c', 'd'])
print(d3)
d4 = d3.drop(['a', 'b'])
print(d4)
b1 = pd.DataFrame(np.arange(12).reshape(3, 4))
b2 = pd.DataFrame(np.arange(20).reshape(4, 5))
print(b1, b2, b1 + b2)
print(b1 * b2)
print(b1/b2)
print(b1.add(b2, fill_value = 100))








