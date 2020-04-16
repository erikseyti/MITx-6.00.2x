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

# um unico plot com 1 unica curva.    
# plt.plot(mySamples,myLinear)
    
# cria um plot unico com todos os elementos no mesmo eixo x.
# plt.plot(mySamples, myLinear)
# plt.plot(mySamples, myQuadratic)
# plt.plot(mySamples, myCubic)
# plt.plot(mySamples, myExponential)

# exibindo todos os plots em janelas separadas.
# plt.figure('lin')
# plt.plot(mySamples, myLinear)
# plt.figure('quad')
# plt.plot(mySamples, myQuadratic)
# plt.figure('cube')
# plt.plot(mySamples, myCubic)
# plt.figure('expo')
# plt.plot(mySamples, myExponential)


# exibindo os graficos com seus respectivos titulos.
# Somente o primeiro é nomeado qual o nome de seus eixos.
# plt.figure('lin')
# plt.title('Linear')
# plt.plot(mySamples, myLinear)
# plt.figure('quad')
# plt.title('Quadratic')
# plt.plot(mySamples, myQuadratic)
# plt.figure('cube')
# plt.title('Cubic')
# plt.plot(mySamples, myCubic)
# plt.figure('expo')
# plt.title('Exponencial')
# plt.plot(mySamples, myExponential)


# exibindo os graficos de forma individual.
# Tambem foi limpado as suas respectivas "janelas" com a função clf() 
# para tirar qualquer configuração anteriomente colocada nos graficos
# plt.figure('lin')
# plt.clf()
# plt.title('Linear')
# plt.plot(mySamples, myLinear)
# plt.figure('quad')
# plt.clf()
# plt.title('Quadratic')
# plt.plot(mySamples, myQuadratic)
# plt.figure('cube')
# plt.clf()
# plt.title('Cubic')
# plt.plot(mySamples, myCubic)
# plt.figure('expo')
# plt.clf()
# plt.title('Exponencial')
# plt.plot(mySamples, myExponential)


# cria 2 graficos contendo ambos um mesmo valor maximo para o limite do eixo Y.
# Para poder comparar os 2 graficos.
# plt.figure('lin')
# plt.clf()
# plt.ylim(0,1000)
# plt.plot(mySamples,myLinear)
# plt.figure('quad')
# plt.clf()
# plt.ylim(0,1000)
# plt.plot(mySamples,myQuadratic)

# plt.figure('lin quad')
# plt.clf()
# plt.plot(mySamples,myLinear,label='linear')
# plt.plot(mySamples,myQuadratic,label='quadratic')
# plt.legend(loc='upper left')
# plt.title('Linear vx. Quadratic')

# plt.figure('cub exp')
# plt.clf()
# plt.plot(mySamples,myCubic,label='cubic')
# plt.plot(mySamples,myExponential,label='exponencial')
# plt.legend()
# plt.title('Cubic Vs. Exponential')


plt.figure('lin quad')
plt.clf()
plt.subplot(211)
plt.ylim(0,900)

plt.plot(mySamples,myLinear,'b-',label='linear',linewidth=2.0)
plt.subplot(212)
plt.ylim(0,900)
plt.plot(mySamples,myQuadratic,'r',label='quadratic',linewidth=3.0)
plt.legend(loc='upper left')
plt.title('Linear vx. Quadratic')

plt.figure('cub exp')
plt.clf()
plt.subplot(121)
plt.ylim(0,14000)
plt.plot(mySamples,myCubic,'g--',label='cubic',linewidth=4.0)
plt.subplot(122)
plt.ylim(0,14000)
plt.plot(mySamples,myExponential,'k^',label='exponencial',linewidth=5.0)
plt.legend()
plt.title('Cubic Vs. Exponential')


