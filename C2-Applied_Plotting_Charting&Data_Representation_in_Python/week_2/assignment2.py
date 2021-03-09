# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:50:47 2020

@author: kench
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df.head()

#convert temperature from tenths of degree C to degree C
df['Data_Value']=0.1*df.Data_Value
days=list(map(lambda x: x.split('-')[-2]+'-'+x.split('-')[-1], df.Date))
years=list(map(lambda x: x.split('-')[0], df.Date))
df['Days']=days 
df['Years']=years
df_2005_to_2014=df[(df.Days!='02-29')&(df.Years!='2015')]
df_2015=df[(df.Days!='02-29')&(df.Years=='2015')]
df_max=df_2005_to_2014.groupby(['Element','Days']).max()
df_min = df_2005_to_2014.groupby(['Element','Days']).min()
df_2015_max=df_2015.groupby(['Element','Days']).max()
df_2015_min = df_2015.groupby(['Element','Days']).min()
record_max=df_max.loc['TMAX'].Data_Value
record_min=df_min.loc['TMIN'].Data_Value
record_2015_max=df_2015_max.loc['TMAX'].Data_Value
record_2015_min=df_2015_min.loc['TMIN'].Data_Value

plt.figure(figsize=(10,7)) 
plt.plot(np.arange(len(record_max)),record_max, '--k', label="record high") 
plt.plot(np.arange(len(record_max)),record_min, '-k',label="record low") 
plt.scatter(np.where(record_2015_min < record_min.values),record_2015_min[record_2015_min < record_min].values,c='b',label='2015 break low')
plt.scatter(np.where(record_2015_max > record_max.values),record_2015_max[record_2015_max > record_max].values,c='r',label='2015 break high') 
plt.xlabel('month',size=14) 
plt.ylabel('temperature($^\circ C$ )',size=14) 
plt.xticks(np.arange(0,365,31), ['Jan','Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']) 
ax=plt.gca() 
ax.axis([0,365,-40,40]) 
plt.gca().fill_between(np.arange(0,365),record_min,record_max,facecolor='blue',alpha=0.25) 
plt.title('Record temperatures for different months between 2005-2014',size=14) 
plt.legend(loc=0) 
plt.show()