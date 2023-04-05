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
    dframe = pd.read_csv(filename, skiprows=4)
    return dframe


def datafilter(dframe, col, value, coun, yr):
    df1 = dframe.groupby(col, group_keys=True)
    df1 = df1.get_group(value)
    df1 = df1.reset_index()
    df1.set_index('Country Name', inplace=True)
    df1 = df1.loc[:, yr]
    df1 = df1.loc[coun, :]
    df1 = df1.dropna(axis=1)
    df1 = df1.reset_index()
    df2 = df1.set_index('Country Name')
    df2 = df2.transpose()
    return df1, df2


def stat_data(dframe, col, value, yr, indi):
    df3 = dframe.groupby(col, group_keys=True)
    df3 = df3.get_group(value)
    df3 = df3.reset_index()
    df2 = df3.set_index('Indicator Name', inplace=True)
    df3 = df3.loc[:, yr]
    df3 = df3.transpose()
    df3 = df3.loc[:, indi]
    return df3


def bar_plot(data, title, x, y):
    ax = data.plot.bar(x='Country Name', rot=0, figsize=(50, 30), fontsize=50)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.set_title(title.upper(), fontsize=50, fontweight='bold')
    ax.set_xlabel(x, fontsize=50)
    ax.set_ylabel(y, fontsize=50)
    ax.legend(fontsize=50)
    plt.savefig(title + '.png')
    plt.show()
    return


def line_plot(data, title, x, y):
    data.plot.line(figsize=(50, 30), fontsize=36, linewidth=10.0)
    plt.yticks([0, 5, 10, 15, 20])
    plt.title(title.upper(), fontsize=50, fontweight='bold')
    plt.xlabel(x, fontsize=50)
    plt.ylabel(y, fontsize=50)
    plt.legend(fontsize=50)
    plt.savefig(title + '.png')
    plt.show()
    return


def heat_map(data):
    title = 'Heat Map of Brazil'
    plt.figure(figsize=(20, 18))
    sns.heatmap(data.corr(), annot=True)
    plt.title(title, fontsize=50, fontweight='bold')
    plt.savefig(title + '.png')
    return data


data = read_data("CompleteDataSet.csv")
bar_country = ['Rwanda', 'Poland', 'Burkina Faso', 'Lithuania']
bar_year = ['2000', '2001', '2002', '2003']
bardata1, bardata2 = datafilter(
    data, 'Indicator Name', 'CO2 emissions from liquid fuel consumption (% of total)', bar_country, bar_year)
print(bardata1)
print(bardata2)
bardata3, bardata4 = datafilter(data, 'Indicator Name',
                                'Agricultural land (% of land area)', bar_country, bar_year)
print(bardata3)
print(bardata4)
bar_plot(bardata1, 'CO2 emissions from liquid fuel consumption',
         'Countries', 'CO2 Emissions')
bar_plot(bardata3, 'Agricultural land ', 'Countries', 'Agricultural land')


line_country = ['Angola', 'Ghana', 'Ethiopia', 'Brazil']
line_year = ['1961', '1962', '1963', '1964']
linedata1, linedata2 = datafilter(
    data, 'Indicator Name', 'CO2 emissions from solid fuel consumption (% of total)', line_country, line_year)
print(linedata1)
print(linedata2)

linedata3, linedata4 = datafilter(data, 'Indicator Name',
                                  'Arable land (% of land area)', line_country, line_year)
print(linedata3)
print(linedata4)
line_plot(linedata2, 'CO2 emissions from solid fuel consumption',
          'Years', 'CO2 emissions')
line_plot(linedata4, 'Arable land', 'Years', 'Arable land')

years = ['1990', '1995', '2000', '2005', '2010']
indicator = ['CO2 emissions from liquid fuel consumption (% of total)', 'Agricultural land (% of land area)',
             'CO2 emissions from solid fuel consumption (% of total)', 'Arable land (% of land area)']
datastat = stat_data(data, 'Country Name', 'Brazil', years, indicator)
print(datastat.head())
heat_map(datastat)


start = 1995
end = 2010
year_range = [str(i) for i in range(start, end+1)]
indic = ['CO2 emissions from liquid fuel consumption (% of total)', 'Agricultural land (% of land area)',
         'Agriculture, forestry, and fishing, value added (% of GDP)', 'Arable land (% of land area)']
des = stat_data(data, 'Country Name', 'Kuwait', year_range, indic)
summary_stats = des.describe()
print(summary_stats)
skewness = stats.skew(des['Arable land (% of land area)'])
kurtosis = des['Agricultural land (% of land area)'].kurtosis()
print('Skewness of Arable land in Brazil : ', skewness)
print('kurtosis of CO2 emissions  in Brazil : ', kurtosis)
summary_stats.to_csv('summary_statistics7.csv')
