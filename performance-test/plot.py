#! /usr/bin/env python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import pandas as pd

# Plotting performance testing data

if_data = pd.read_csv('./InitFacilityNum.csv', delimiter=',', index_col=0)
ts_data = pd.read_csv('./SimDur.csv', delimiter=',', index_col=0)

# Pre-filter
if_none = if_data[(if_data['TableEval']=='BigJoin[:]') & (if_data['Inventory']=='none') & (if_data['WriteFlag']=='--write')]
if_inv = if_data[(if_data['TableEval']=='BigJoin[:]') & (if_data['Inventory']=='inv') & (if_data['WriteFlag']=='--write')]
if_inv_c = if_data[(if_data['TableEval']=='BigJoin[:]') & (if_data['Inventory']=='inv_compact') & (if_data['WriteFlag']=='--write')]
ts_none = ts_data[(ts_data['TableEval']=='BigJoin[:]') & (ts_data['Inventory']=='none') & (ts_data['WriteFlag']=='--write')]
ts_inv = ts_data[(ts_data['TableEval']=='BigJoin[:]') & (ts_data['Inventory']=='inv') & (ts_data['WriteFlag']=='--write')]
ts_inv_c = ts_data[(ts_data['TableEval']=='BigJoin[:]') & (ts_data['Inventory']=='inv_compact') & (ts_data['WriteFlag']=='--write')]

# Time vs DbSize by nucs tracked, HDF5 vs SQLite
full_params = ['Initial Facility Number, ', 'Simulation Duration, ']
params = ['InitFacilityNum', 'SimDur']
dbtype = ['h5', 'sqlite']
nucs = ['three', 'eight', 'nea_spent_uox']
nums = ['3', '8', '23']
lines = ['--', '-.', '-']

# Customize
mpl.rcParams.update({'font.size': 16})
mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams['lines.markersize'] = 10 

for p, param in zip(full_params, params):
    for d in dbtype:
        count = 0
        for n, s, num in zip(nucs, lines, nums):
            if full_params.index(p)==0:
                df1 = if_none[(if_none['NucsTracked']==n) & (if_none['DbType']==d)]
                df2 = if_inv[(if_inv['NucsTracked']==n) & (if_inv['DbType']==d)]
                df3 = if_inv[(if_inv_c['NucsTracked']==n) & (if_inv_c['DbType']==d)]
            elif full_params.index(p)==1:
                df1 = ts_none[(ts_none['NucsTracked']==n) & (ts_none['DbType']==d)]
                df2 = ts_inv[(ts_inv['NucsTracked']==n) & (ts_inv['DbType']==d)]
                df3 = ts_inv[(ts_inv_c['NucsTracked']==n) & (ts_inv_c['DbType']==d)]
            s1 = 'b' + s
            s2 = 'r' + s
            s3 = 'g' + s
            lbl1 = 'No Inv: ' + num + ' nucs'
            lbl2 = 'Inv: ' + num + ' nucs'
            lbl3 = 'Comp Inv: ' + num + ' nucs'
            if count==0:
                ax1 = df1.plot(x='DbSize', y='Time', label=lbl1, style=s1, marker='.')
            else:
                df1.plot(ax=ax1, x='DbSize', y='Time', label=lbl1, style=s1, marker='.')
            ax2 = ax1.twiny()
            ax1.set_xlabel('DbSize (B)')
            ax2.set_xlabel(param)
            df2.plot(ax=ax1, x='DbSize', y='Time', label=lbl2, style=s2, marker='.')
            #df3.plot(ax=ax1, x='DbSize', y='Time', label=lbl3, style=s3, marker='.')
            count += 1
        title = p + 'Inv Table & Nucs Tracked (Write Only): ' + d
        plt.title(title, y=1.09)
        plt.show()

