#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:36:05 2020

@author: erik
"""
import time

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# for i in range(121):
#     print('fib(' + str(i) + ') =', fib(i))


def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:     
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result

for i in range(121):
    start = time.time()
    print('fib(' + str(i) + ') =', fastFib(i))

## code to be timed
end = time.time()
print(end - start)