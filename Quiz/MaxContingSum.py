#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:03:51 2020

@author: erik
"""


def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
        
    listaResultados = [L[0]]    
    listaAuxiliar = L.copy()
    
    if len(L)==1:
        return L[0]
    
    for a in L:
        listaResultados.append(a)
        soma = a
        listaAuxiliar.pop(0)        
        for x in listaAuxiliar:
            soma = soma + x
            listaResultados.append(soma)
    
    listaResultados = sorted(listaResultados,reverse=True)
            
    return listaResultados[0]
    
    
    
    
print(max_contig_sum([3, 4, -1, 5, -4]))
print(max_contig_sum([3, 4, -8, 15, -1, 2]))
print(max_contig_sum([1]))
print(max_contig_sum([1, -1]))
print(max_contig_sum([10, 9, 8, -1]))
print(max_contig_sum([5, -7, 1]))


# ainda a fazer tratamento do codigo fonte
print(max_contig_sum([0, -2, -5, -1, 5]))
print(max_contig_sum([-3, -2, 1, -1, -5]))
print(max_contig_sum([5, -7, 1]))
