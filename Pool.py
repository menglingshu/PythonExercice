#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:17:59 2018

@author: Lingshu
"""

class Turtle:
    def __init__(self, x):
        self.num = x

class Fish:
    def __init__(self, x):
        self.num = x
        
class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
        
    def print_num(self):
        print('there are %d turtles and %d fishes ' % (self.turtle.num, self.fish.num))