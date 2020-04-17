#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:24:17 2020

@author: erik
"""

import random

def rollDie():
    """retorna um valor randomico ent entre 1  e 6"""
    return random.choice([1,2,3,4,5,6])

def testRoll(n=10):
    result = ""
    for i in range(n):
        result = result + str(rollDie())
    print(result)


testRoll()