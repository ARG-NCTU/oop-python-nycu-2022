# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:29:43 2016

@author: johnguttag
"""

import random
import matplotlib.pyplot as plt
import numpy as np

#set line width
plt.rcParams['lines.linewidth'] = 4
#set font size for titles 
plt.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
plt.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
plt.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
plt.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
#set size of markers
plt.rcParams['lines.markersize'] = 10
#set number of examples shown in legends
plt.rcParams['legend.numpoints'] = 1

def calculate_probability(numCasesPerYear, numYears, numCommunities, numTrials, threshold, region):
    numGreater = 0
    for t in range(numTrials):
        locs = [0] * numCommunities
        for i in range(numYears * numCasesPerYear):
            locs[random.choice(range(numCommunities))] += 1
        if locs[region] >= threshold:
            numGreater += 1
    prob = round(numGreater / numTrials, 4)
    return prob

if __name__ == "__main__":
    random.seed(0)
    numCasesPerYear = 36000
    numYears = 3
    stateSize = 10000
    communitySize = 10
    numCommunities = stateSize // communitySize
    numTrials = 100
    threshold = 143
    region = 111

    prob = calculate_probability(numCasesPerYear, numYears, numCommunities, numTrials, threshold, region)
    print('Est. probability of region 111 having at least 143 cases =', prob)