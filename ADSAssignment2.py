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
    '''
    Reading and performing file manipulation
    '''
    dframe = pd.read_csv(filename, skiprows=4)
    return dframe


def datafilter(dframe, col, value, coun, yr):
    '''
    Grouping the data using the function groupby.
    parameters required are passed from function call.
    '''

    df1 = dframe.groupby(col, group_keys=True)
    #Retrieving the data using get_group
    df1 = df1.get_group(value)
    #Resetting the data frame index
    df1 = df1.reset_index()
    df1.set_index('Country Name', inplace=True)
    #Cropping the dataframe data
    df1 = df1.loc[:, yr]
    df1 = df1.loc[coun, :]
    #Dropping the NAN values from dataframe
    df1 = df1.dropna(axis=1)
    df1 = df1.reset_index()
    df2 = df1.set_index('Country Name')
    #Transposing the data
    df2 = df2.transpose()
    return df1, df2


def stat_data(dframe, col, value, yr, indi):
    '''
stat_data function is used for calculating the statistical values.
dataframe along with other parameters are passed.
    '''
    df3 = dframe.groupby(col, group_keys=True)
    #Grouping the data and resetting the index
    df3 = df3.get_group(value)
    df3 = df3.reset_index()
    df2 = df3.set_index('Indicator Name', inplace=True)
    #Cropping the dataframe data
    df3 = df3.loc[:, yr]
    #Transposing the data
    df3 = df3.transpose()
    df3 = df3.loc[:, indi]
    #Returning the dataframe
    return df3


def bar_plot(data, title, x, y):
    #Plotting bar graph using plot function
    ax = data.plot.bar(x='Country Name', rot=0, figsize=(50, 30), fontsize=50)
    #Setting the y axis
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    #Setting the title, x and y labels
    ax.set_title(title.upper(), fontsize=50, fontweight='bold')
    ax.set_xlabel(x, fontsize=50)
    ax.set_ylabel(y, fontsize=50)
    ax.legend(fontsize=50)
    #Saving the figure
    plt.savefig(title + '.png')
    plt.show()
    return

#Function for lineplot is defined


def line_plot(data, title, x, y):
    #Plotting line graph
    data.plot.line(figsize=(50, 30), fontsize=36, linewidth=10.0)
    plt.yticks([0, 5, 10, 15, 20])
    plt.title(title.upper(), fontsize=50, fontweight='bold')
    plt.xlabel(x, fontsize=50)
    plt.ylabel(y, fontsize=50)
    #Setting legend
    plt.legend(fontsize=50)
    #saving ploted graph
    plt.savefig(title + '.png')
    plt.show()
    return

#Function to create heatmap


def heat_map(data):
    #Setting title for Heat Map
    title = 'Heat Map of Brazil'
    plt.figure(figsize=(20, 18))
    #Creating Heat Map and saving ploted image
    heatmap = sns.heatmap(data.corr(), annot=True, cmap="Spectral")
    plt.title(title, fontsize=50, fontweight='bold')
    plt.savefig(title + '.png', dpi=300, bbox_inches='tight')
    return data


#Reading data for filtering dataframe
data = read_data("CompleteDataSet.csv")
#Countries and Years for filtering bargraph data
bar_country = ['Rwanda', 'Poland', 'Burkina Faso', 'Lithuania']
bar_year = ['2000', '2001', '2002', '2003']
#Calling filtering function and passing required parameters for bar graph
bardata1, bardata2 = datafilter(
    data, 'Indicator Name', 'CO2 emissions from liquid fuel consumption (% of total)', bar_country, bar_year)
print(bardata1)
print(bardata2)
bardata3, bardata4 = datafilter(data, 'Indicator Name',
                                'Agricultural land (% of land area)', bar_country, bar_year)
print(bardata3)
print(bardata4)
#Calling bar_plot function for ploting bar graph
bar_plot(bardata1, 'CO2 emissions from liquid fuel consumption',
         'Countries', 'CO2 Emissions(% of total)')
bar_plot(bardata3, 'Agricultural land ', 'Countries', 'Agricultural land(% of land area)')


#Countries and Years for filtering lineplot data
line_country = ['Angola', 'Ghana', 'Ethiopia', 'Brazil']
line_year = ['1961', '1962', '1963', '1964']
#Calling filtering function and passing required parameters for line plot
linedata1, linedata2 = datafilter(
    data, 'Indicator Name', 'CO2 emissions from solid fuel consumption (% of total)', line_country, line_year)
print(linedata1)
print(linedata2)

linedata3, linedata4 = datafilter(data, 'Indicator Name',
                                  'Arable land (% of land area)', line_country, line_year)
print(linedata3)
print(linedata4)
#Calling line_plot function for ploting line plot
line_plot(linedata2, 'CO2 emissions from solid fuel consumption',
          'Years', 'CO2 emissions(% of total)')
line_plot(linedata4, 'Arable land', 'Years', 'Arable land(% of land area)')


#Setting the years and indicators to be passed as parameters
years = ['1990', '1995', '2000', '2005', '2010']
indicator = ['CO2 emissions from liquid fuel consumption (% of total)', 'Agricultural land (% of land area)',
             'CO2 emissions from solid fuel consumption (% of total)', 'Arable land (% of land area)']
datastat = stat_data(data, 'Country Name', 'Brazil', years, indicator)
print(datastat.head())
#Calling heatmap function along with parameters
heat_map(datastat)


#Range of years, for data analysis
start = 1995
end = 2010
year_range = [str(i) for i in range(start, end+1)]
#Setting indicators for statistical analysis
indic = ['CO2 emissions from liquid fuel consumption (% of total)', 'Agricultural land (% of land area)',
         'Agriculture, forestry, and fishing, value added (% of GDP)', 'Arable land (% of land area)']
des = stat_data(data, 'Country Name', 'Kuwait', year_range, indic)
#Describing the statistical table
summary_stats = des.describe()
print(summary_stats)
#Using the Statistical methods
skewness = stats.skew(des['Arable land (% of land area)'])
kurtosis = des['Agricultural land (% of land area)'].kurtosis()
print('Skewness of Arable land in Brazil : ', skewness)
print('kurtosis of CO2 emissions  in Brazil : ', kurtosis)
summary_stats.to_csv('summary_statis1.csv')
