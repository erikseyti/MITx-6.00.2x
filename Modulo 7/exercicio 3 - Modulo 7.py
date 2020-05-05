#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:55:58 2020

@author: erik
"""
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std


def stdDevOfLeghts(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float('NaN')
    
    lista = list(map(len, L))
    mean = sum(lista)/float(len(lista))
    tot = 0.0
    for l in lista:
        tot += (l - mean)**2
    std = (tot/len(lista))**0.5    
    return std

def stdDevOfLeghts_V2(L):
    """
    L: é uma lista de strings
    
    função que utiliza o conceito de reuso, da função getMeanAndStd(x), 
    para calcular o desvio padrão. 

    returns: um valor float, caso a lista de contenha pelo menos uma string, caso
    contrario, (a lista vazia) retorna o valor NaN.
    """
    if not L:
        return float('NaN')
    
    lista = list(map(len, L))
    media, desvioPadrao = getMeanAndStd(lista)
    return desvioPadrao

def calcularCoeficienteVariancia(lista):
    media, desvioPadrao =getMeanAndStd(lista)
    coefienteVariancia = desvioPadrao/media
    return coefienteVariancia



print(stdDevOfLeghts_V2(["a","z","p"]))
print(stdDevOfLeghts_V2(['apples', 'oranges', 'kiwis', 'pineapples']))
print(stdDevOfLeghts_V2([]))

print(calcularCoeficienteVariancia([0,1,2,3,4,5,6]))
print(calcularCoeficienteVariancia([10,4,12,15,20,5]))
