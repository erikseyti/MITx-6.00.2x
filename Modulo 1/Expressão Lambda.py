#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:05:20 2020

@author: erik
"""


f1 =  lambda x:x
print(f1(3))
f2 = lambda x,y: x+y
print(f2(2,3))
print(f2("Ana"," Paula"))
f3 = lambda x,y: 'fatorial' if (x%y==0) else "não é fatorial"
print(f3(4,2))
print(f3(9,5))


