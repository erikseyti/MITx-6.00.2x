#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:24:47 2020

@author: erik
"""


def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    
    soma = s
    contador = 0
    
    if len(L) == 0:
        return "no solution"
    
    
    for a in L:
        numeroMenor = True
        
        while numeroMenor == True:
            if soma == 0:
                return contador
            
            if soma< a:
                break
            
            soma = soma - a
            contador = contador + 1
    
    return 'no solution'
            
    
    
    
    
    

    # listMupliers = sorted(L,reverse=True)    
    # soma = 0
    # somaMultiplicadores = 0
    
    # contador  = 0 
    # for a in L:
    #     soma =  soma + (a * listMupliers[contador])
    #     somaMultiplicadores = somaMultiplicadores + listMupliers[contador]
    #     contador = contador + 1
        
    #     if soma == s:
    #         return somaMultiplicadores
    return "no solution"


# corretos
print(greedySum([], 10)) # no solution
print(greedySum([1], 20)) # 20
print(greedySum([2], 5)) # no solution
print(greedySum([10, 5, 1], 14)) # 5
print(greedySum([10, 5, 1], 11)) # 2
print(greedySum([10, 9, 8, 1], 20)) # 2
print(greedySum([10, 9, 8, 1], 17)) # 8
print(greedySum([10, 8, 5, 1], 13)) # 4
print(greedySum([15, 12, 4, 3, 1], 29)) # 4
print(greedySum([16, 12, 5, 3, 1], 15)) # 2
print(greedySum([16, 12, 5, 3, 1], 24)) # 3


# print(greedySum([10, 7, 6, 3], 19)) # 19
# print(greedySum([10, 8, 5, 2], 16)) # no solution
# print(greedySum([11, 10, 8, 5, 1], 16)) # 2
# print(greedySum([12, 10, 8, 5, 2], 17)) # 2
# print(greedySum([20, 10, 4, 3, 1], 21)) # 2
# print(greedySum([21, 10, 8, 3, 1], 11)) # 2
# print(greedySum([30, 20, 10], 60)) # 2
# print(greedySum([50, 25, 5], 5)) # 1
# greedySum([101, 51, 11, 2, 1], 3000) # 30


