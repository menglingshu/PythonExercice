#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 16:05:37 2018

@author: Lingshu
"""

import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)

T = np.arctan2(Y, X)
plt.scatter(X, Y, s = 75, c = T, alpha = 0.5)

plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))

plt.xticks(())
plt.yticks(())