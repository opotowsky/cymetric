#! /usr/bin/env python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import pandas as pd

# Plotting a preliminary version of performance testing data

if_data = pd.read_csv('./InitFacilityNum_old.csv', delimiter=',', index_col=0)
ts_data = pd.read_csv('./SimDur_old.csv', delimiter=',', index_col=0)

# IF: Time vs DbSize by nucs tracked
# HDF5
h_if_no_w = if_data[(if_data['WriteFlag']=='--no-write') & (if_data['DbType']=='h5')]
h_if_no_3 = h_if_no_w[h_if_no_w['NucsTracked']=='three']
h_if_no_8 = h_if_no_w[h_if_no_w['NucsTracked']=='eight']
h_if_no_23 = h_if_no_w[h_if_no_w['NucsTracked']=='nea_spent_uox']

h_if_w = if_data[(if_data['WriteFlag']=='--write') & (if_data['DbType']=='h5')] 
h_if_w_3 = h_if_w[h_if_w['NucsTracked']=='three']
h_if_w_8 = h_if_w[h_if_w['NucsTracked']=='eight']
h_if_w_23 = h_if_w[h_if_w['NucsTracked']=='nea_spent_uox']

h_ax = h_if_no_3.plot(x='DbSize', y='Time', kind='scatter', legend=False)
h_if_no_8.plot(ax = h_ax, x='DbSize', y='Time', kind='scatter', legend=False)
h_if_no_23.plot(ax = h_ax, x='DbSize', y='Time', kind='scatter', legend=False)
h_if_w_3.plot(ax = h_ax, x='DbSize', y='Time', kind='scatter', legend=False)
h_if_w_8.plot(ax = h_ax, x='DbSize', y='Time', kind='scatter', legend=False)
h_if_w_23.plot(ax = h_ax, x='DbSize', y='Time', kind='scatter', legend=False)

hl = plt.legend()
hl.get_texts()[0].set_text('no-write, 3 nucs')
hl.get_texts()[1].set_text('no-write, 8 nucs')
hl.get_texts()[2].set_text('no-write, 23 nucs')
hl.get_texts()[3].set_text('write, 3 nucs')
hl.get_texts()[4].set_text('write, 8 nucs')
hl.get_texts()[5].set_text('write, 23 nucs')
hl.set_title('Write Flag & Nucs Tracked, HDF5')
plt.show()

#SQLITE
s_if_no_w = if_data[(if_data['WriteFlag']=='--no-write') & (if_data['DbType']=='sqlite')]
s_if_no_3 = s_if_no_w[s_if_no_w['NucsTracked']=='three']
s_if_no_8 = s_if_no_w[s_if_no_w['NucsTracked']=='eight']
s_if_no_23 = s_if_no_w[s_if_no_w['NucsTracked']=='nea_spent_uox']

s_if_w = if_data[(if_data['WriteFlag']=='--write') & (if_data['DbType']=='sqlite')] 
s_if_w_3 = s_if_w[s_if_w['NucsTracked']=='three']
s_if_w_8 = s_if_w[s_if_w['NucsTracked']=='eight']
s_if_w_23 = s_if_w[s_if_w['NucsTracked']=='nea_spent_uox']

s_ax = s_if_no_3.plot(x='DbSize', y='Time', kind='scatter', legend=False)
s_if_no_8.plot(ax = s_ax, x='DbSize', y='Time', kind='scatter', legend=False)
s_if_no_23.plot(ax = s_ax, x='DbSize', y='Time', kind='scatter', legend=False)
s_if_w_3.plot(ax = s_ax, x='DbSize', y='Time', kind='scatter', legend=False)
s_if_w_8.plot(ax = s_ax, x='DbSize', y='Time', kind='scatter', legend=False)
s_if_w_23.plot(ax = s_ax, x='DbSize', y='Time', kind='scatter', legend=False)

sl = plt.legend()
sl.get_texts()[0].set_text('no-write, 3 nucs')
sl.get_texts()[1].set_text('no-write, 8 nucs')
sl.get_texts()[2].set_text('no-write, 23 nucs')
sl.get_texts()[3].set_text('write, 3 nucs')
sl.get_texts()[4].set_text('write, 8 nucs')
sl.get_texts()[5].set_text('write, 23 nucs')
sl.set_title('Write Flag & Nucs Tracked, SQLITE')
plt.show()

# TS: Time vs DbSize by nucs tracked
ts_no_w = ts_data[ts_data['WriteFlag']=='--no-write']
ts_no_3 = ts_no_w[ts_no_w['NucsTracked']=='three']
ts_no_8 = ts_no_w[ts_no_w['NucsTracked']=='eight']
ts_no_23 = ts_no_w[ts_no_w['NucsTracked']=='nea_spent_uox']

ts_w = ts_data[ts_data['WriteFlag']=='--write'] 
ts_w_3 = ts_w[ts_w['NucsTracked']=='three']
ts_w_8 = ts_w[ts_w['NucsTracked']=='eight']
ts_w_23 = ts_w[ts_w['NucsTracked']=='nea_spent_uox']

hh_ax = ts_no_3.plot(x='DbSize', y='Time', kind='scatter', legend=False)
ts_no_8.plot(ax = hh_ax, x='DbSize', y='Time', kind='scatter', legend=False)
ts_no_23.plot(ax = hh_ax, x='DbSize', y='Time', kind='scatter', legend=False)
ts_w_3.plot(ax = hh_ax, x='DbSize', y='Time', kind='scatter', legend=False)
ts_w_8.plot(ax = hh_ax, x='DbSize', y='Time', kind='scatter', legend=False)
ts_w_23.plot(ax = hh_ax, x='DbSize', y='Time', kind='scatter', legend=False)

ll = plt.legend()
ll.get_texts()[0].set_text('no-write, 3 nucs')
ll.get_texts()[1].set_text('no-write, 8 nucs')
ll.get_texts()[2].set_text('no-write, 23 nucs')
ll.get_texts()[3].set_text('write, 3 nucs')
ll.get_texts()[4].set_text('write, 8 nucs')
ll.get_texts()[5].set_text('write, 23 nucs')
ll.set_title('Write Flag & Nucs Tracked, HDF5')
plt.show()

