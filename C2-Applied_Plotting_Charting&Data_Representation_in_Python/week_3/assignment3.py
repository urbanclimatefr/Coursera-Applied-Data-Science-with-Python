# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:15:28 2020

@author: kench
"""

# Use the following data for this assignment:

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
mean = df.mean(axis=1).tolist()
std = df.std(axis=1)

import matplotlib.pyplot as plt
from scipy.stats import t
import matplotlib.colors as mcol
import matplotlib.cm as cm

def barplot(y_interested):
    plt.figure()
    yerr = t.ppf(1-0.05/2, df.shape[1] -1) * std / np.sqrt(df.shape[1])

    cm1 = mcol.LinearSegmentedColormap.from_list("colormap",["blue", "white", "red"])
    cpick = cm.ScalarMappable(cmap=cm1)
    cpick.set_array([])

    percentages = []
    for bar, yerr_ in zip(mean, yerr):
        low = bar - yerr_
        high = bar + yerr_
        percentage = (high - y_interested) / (high - low)
        if percentage > 1: percentage = 1
        if percentage < 0: percentage = 0
        percentages.append(percentage)


    cpick.to_rgba(percentages)

    bars = plt.bar(range(df.shape[0]), mean, yerr=yerr, color=cpick.to_rgba(percentages), capsize=15)
    plt.colorbar(cpick, orientation='horizontal')

    plt.xticks(np.arange(4), df.index)

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.axhline(y=y_interested, color='green')
    plt.annotate('y = %d' % y_interested, xy=(-0.4, y_interested + 2000))

barplot(40000)