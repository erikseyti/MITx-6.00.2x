#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:58:38 2020

@author: erik
"""


import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    valorRandomico = random.randrange(10,21,2)
    return valorRandomico
    # Your code here

# print(deterministicNumber())
