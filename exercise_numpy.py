#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:07:35 2018

@author: Lingshu
"""

import numpy as np
import pandas as pd

array = np.array([[1, 2, 3], [2, 3, 4]])

print(array)
print('number of dim: ', array.ndim)
print('shape: ', array.shape)
print('size: ', array.size)

A = np.arange(14, 2, -1).reshape((3,4))

print(A)
print(np.transpose(A))
print(A[1, 1:3])

B = np.array([1, 1, 1])
C = np.array([2, 2, 2])
D = np.vstack((B, C))
print(D)
print(D.T)
print(np.hstack((B, C)))

dates = pd.date_range('20170101', periods = 6)
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = ['a', 'b', 'c', 'd'])

