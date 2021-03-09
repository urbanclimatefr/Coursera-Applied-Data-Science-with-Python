# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:16:41 2020

@author: kench
"""


import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)
plt.hist(x, 100)
plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
plt.savefig('matplotlib_histogram.png')
plt.show()