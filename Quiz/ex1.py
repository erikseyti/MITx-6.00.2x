#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:00:54 2020

@author: erik
"""
import random

def f(x):
    # x is an integer
    return int(x + random.choice([0.25, 0.5, 0.75]))

print(f(10))