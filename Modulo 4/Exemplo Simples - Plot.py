#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:54:14 2020

@author: erik
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic =[]
myCubic = []
myExponential = []

for i in range (0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
plt.plot(mySamples,myLinear)