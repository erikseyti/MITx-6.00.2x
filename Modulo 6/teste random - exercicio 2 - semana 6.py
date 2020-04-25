#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:31:44 2020

@author: erik
"""


import random
mylist = []


for x in range(10):
    for i in range(random.randint(1, 10)):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
    print(mylist)