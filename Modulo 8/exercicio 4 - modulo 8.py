#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:41:06 2020

@author: erik
"""
import random;

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    bucket = ['r','r','r','g','g','g']
    estimatives = 0
    mesmaCor = 0
    
    for t in range(numTrials):
        balde = bucket.copy()
        for i in range(3):
            bola = random.choice(balde)
            balde.remove(bola)
        if balde == ['r','r','r'] or balde == ['g','g','g']:
            mesmaCor = mesmaCor + 1
    estimatives = mesmaCor/numTrials
    return estimatives



print(noReplacementSimulation(5000))
