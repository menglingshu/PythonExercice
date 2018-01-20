#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:03:16 2018

@author: Lingshu
"""

import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
        
    def move(self):
        self.x -= 1
        print('my coordinate is: ', self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('delicious')
            self.hungry = False
        else:
            print('i can\'t est anymore')


    