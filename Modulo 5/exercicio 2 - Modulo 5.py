#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:11:23 2020

@author: erik
"""


import random
import numpy as np

# uma solução do problema utilizando a biblioteca numpy
def genEven():
    valorRandomico = random.choice(np.arange(0,100,2))
    return valorRandomico

print(genEven())

# outra solução apenas usando a biblioteca random
def genEven():
    valorRandomico = random.randrange(0,100,2)
    return valorRandomico

print(genEven())