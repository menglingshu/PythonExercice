#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 16:30:02 2018

@author: Lingshu
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (1-x / 2+x**5 + Y**3) * np.exp(-x**2 - y**2)

n = 256
X = np.linspace(-3, 3, n)
Y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(X, Y)

plt.contourf(X, Y, f(X, Y), 8, alpha = 0.75, cmap = 'jet')
C = plt.contour(X, Y, f(X, Y), 8, colors = 'black', linewidth = 0.5)

