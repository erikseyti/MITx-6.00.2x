#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:38:14 2020

@author: erik
"""


import random, pylab

random.seed(0)

xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

pylab.plot(xVals,zVals, label="Grafico de xVals e zVals" )
pylab.legend(loc='best')
pylab.title("Grafico de R2")
pylab.show()

pylab.plot(xVals,yVals, label="Grafico de xVals e yVals" )
pylab.legend(loc='best')
pylab.title("Grafico de R2")
pylab.show()

pylab.plot(xVals,sorted(yVals), label="Grafico de xVals e sorted(yVals)" )
pylab.legend(loc='best')
pylab.title("Grafico de R2")
pylab.show()

pylab.plot(sorted(xVals),yVals, label="Grafico de sorted(xVals) e yVals" )
pylab.legend(loc='best')
pylab.title("Grafico de R2")
pylab.show()

pylab.plot(sorted(xVals),sorted(yVals), label="Grafico de sorted(xVals) e sorted(yVals)" )
pylab.legend(loc='best')
pylab.title("Grafico de R2")
pylab.show()
