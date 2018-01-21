#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:46:01 2018

@author: Lingshu
"""
import time as t

class MyTimer():
    def __init__(self):
        self.unit = ['years', 'month', 'day', 'hour', 'min', 'second']
        self.prompt = 'not yet begin timer'
        self.lasted = []
        self.begin = 0
        self.end = 0
        
    def __str__(self):
        return self.prompt
    
    __repr__ = __str__
    
    def __add__(self, other):
        prompt = 'total running time is: '
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
    
    def start(self):
        self.begin = t.localtime()
        self.prompt = 'please stop time first'
        print('time begin')
    
    def stop(self):
        if not self.begin:
            print('please start timer please')
        else:
            self.end = t.localtime()
            self._calc()
            print('time stop')
    
    def _calc(self):
        self.lasted = []
        self.prompt = "total running time is: "
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        self.begin = 0
        self.end = 0