#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: ancilliary_funcs.py
Author: Ignacio Soto Zamorano
Email: ignacio[dot]soto[dot]z[at]gmail[dot]com
Github: https://github.com/ignaciosotoz
Description:
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def fetch_descriptives(dataframe):
    for key, value in dataframe.iteritems():
        print(value.describe())


def fetch_null_cases(dataframe, var, print_list=False):
    tmp = dataframe
    tmp['flagnull'] = tmp[var].isnull()
    count_na = 0

    for i, r in tmp.iterrows():
        if r['flagnull'] is True:
            count_na += 1
            if print_list is True:
                print( r['cname'])

    if print_list is True:
        print("Países sin registros de {0}\n".format(var))
    print("Casos perdidos para {0}:\nCantidad de Casos: {1}\nPorcentaje de la muestra {2}\n".format(var, count_na, count_na/len(tmp)))

def plot_hist(dataframe, var, sample_mean=True, true_mean=True):
    tmp = dataframe[var].dropna()
    plt.hist(tmp, color='grey', alpha=.4)
    plt.title(var)

    if sample_mean is True:
        plt.axvline(np.mean(tmp), color='dodgerblue')
    if true_mean is True:
        plt.axvline(np.mean(dataframe[var]), color='tomato')


def dotplot(df, plot_var, plot_by, global_stat = False, statistic = 'mean'):
    tmp_df = df.loc[:, [plot_by, plot_var]]

    if statistic is 'mean':
        tmp_group_stat = tmp_df.groupby(plot_by)[plot_var].mean()
    if statistic is 'median':
        tmp_group_stat = tmp_df.groupby(plot_by)[plot_var].median()

    plt.plot(tmp_group_stat.values, tmp_group_stat.index, 'o', color='grey')

    if global_stat is True and  statistic is 'mean':
        plt.axvline(df[plot_var].mean(), color='tomato', linestyle='--')
    if global_stat is True and statistic is 'median':
        plt.axvline(df[plot_var].median(), color='tomato', linestyle='--')

