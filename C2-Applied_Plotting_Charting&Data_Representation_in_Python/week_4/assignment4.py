# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:43:15 2020

@author: kench
"""
#Bcoming an Independent Data Scientist
#This assignment required to identify at least two publicly accessible datasets that are consistent across a meaningful dimension.
# I had to state a research question that can be answered using these datasets and then create a visual using matplotlib that addresses the stated research question. 
#I also had to justify how the visual addresses my research question.

#As this assignment was for the whole course, I had to incorporate and defend the principles discussed in the first week and align with Cairo’s principles of truth, beauty, function, and insight.

#Region and the domain category of the dataset
# Central, Tung Chung, and air quality


#Research question
#How is the air quality in Central, a district of financial centre in Hong Kong,
#in comparison with the air quality of a new town as Tung Chung in Hong Kong.

#Datasets

#Central, Hong Kong. Air quality 2019 
#Download here
#https://cd.epic.epd.gov.hk/EPICDI/air/station/

#Tung Chung, Hong Kong. Air quality 2019 
#Download here
#https://cd.epic.epd.gov.hk/EPICDI/air/station/

#The data included air quality measurements of:
#Carbon Monoxide
#Nitrogen Oxides
#Sulphur Dioxide
#Ozone
#Nitrogen Dioxide


# Import useful libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os


# Read Central air quality data
central_air = pd.read_csv('air_hourly_central.csv')
