# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:07:31 2020

@author: kench
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

# Read Toulouse data
A = ["Season","Attendance"]
toulouse = pd.read_csv('toulouse.csv', sep=',' , usecols=A)

# Read Paris data
A = ["Season","Attendance"]
paris = pd.read_csv('paris.csv', sep=',' , usecols=A)

#get the attendance and the season
attendance_toulouse = toulouse.Attendance
attendance_paris = paris.Attendance
Season = toulouse.Season

#reverse the series
attendance_paris = attendance_paris.iloc[::-1]
attendance_toulouse = attendance_toulouse.iloc[::-1]
Season = Season.iloc[::-1]

#plot
fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(Season,attendance_toulouse,'--r',label='Toulouse')
ax.plot(Season,attendance_paris,'-b', label="Paris") 

# rotate and align the tick labels so they look better
fig.autofmt_xdate()

# use a more precise date string for the x axis locations in the
# toolbar
ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
#set the x,y label
ax.set_xlabel('Season',size=14) 
ax.set_ylabel('Attendance',size=14) 
#eliminate spines
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
#set the legend
ax.legend()