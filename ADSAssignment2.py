# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 23:45:13 2023

@author: mypc
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

def read_data(filename):
    dframe = pd.read_csv(filename, skiprows = 4)
    return dframe

def datafilter(dframe, col, value, coun, yr):
    df1 = dframe.groupby(col, group_keys= True)
    df1 = df1.get_group(value)
    df1 = df1.reset_index()
    df1.set_index('Country Name', inplace=True)
    df1 = df1.loc[:, yr]
    df1 = df1.loc[coun, :]
    df1= df1.dropna(axis = 1)
    df1 = df1.reset_index()
    df2 = df1.set_index('Country Name')  
    df2=df2.transpose()
    return df1,df2

