#! /usr/bin/env python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import pandas as pd

gf_data = pd.read_csv('./GrowthFactor.csv', delimiter=',', index_col=0)
if_data = pd.read_csv('./InitFacilityNum.csv', delimiter=',', index_col=0)
ts_data = pd.read_csv('./TimestepDur.csv', delimiter=',', index_col=0)

# GF: Time vs DbSize by nucs tracked
gf_no_w = gf_data[gf_data['WriteFlag']=='--no-write']
gf_no_3 = gf_no_w[gf_no_w['NucsTracked']=='three']
gf_no_8 = gf_no_w[gf_no_w['NucsTracked']=='eight']
gf_no_23 = gf_no_w[gf_no_w['NucsTracked']=='nea_spent_uox']

gf_w = gf_data[gf_data['WriteFlag']=='--write'] 
gf_w_3 = gf_w[gf_w['NucsTracked']=='three']
gf_w_8 = gf_w[gf_w['NucsTracked']=='eight']
gf_w_23 = gf_w[gf_w['NucsTracked']=='nea_spent_uox']

ax = gf_no_3.plot(x='DbSize', y='Time', kind='line', legend=False)
gf_no_8.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)
gf_no_23.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)
gf_w_3.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)
gf_w_8.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)
gf_w_23.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)

l = plt.legend()
l.get_texts()[0].set_text('no-write, 3 nucs')
l.get_texts()[1].set_text('no-write, 8 nucs')
l.get_texts()[2].set_text('no-write, 23 nucs')
l.get_texts()[3].set_text('write, 3 nucs')
l.get_texts()[4].set_text('write, 8 nucs')
l.get_texts()[5].set_text('write, 23 nucs')
l.set_title('Write Flag & Nucs Tracked')
plt.show()

# IF: Time vs DbSize by nucs tracked
if_no_w = if_data[if_data['WriteFlag']=='--no-write']
if_no_3 = if_no_w[if_no_w['NucsTracked']=='three']
if_no_8 = if_no_w[if_no_w['NucsTracked']=='eight']
if_no_23 = if_no_w[if_no_w['NucsTracked']=='nea_spent_uox']

if_w = if_data[if_data['WriteFlag']=='--write'] 
if_w_3 = if_w[if_w['NucsTracked']=='three']
if_w_8 = if_w[if_w['NucsTracked']=='eight']
if_w_23 = if_w[if_w['NucsTracked']=='nea_spent_uox']

ax = if_no_3.plot(x='DbSize', y='Time', kind='line', legend=False)
if_no_8.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)
if_no_23.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)
if_w_3.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)
if_w_8.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)
if_w_23.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)

ll = plt.legend()
ll.get_texts()[0].set_text('no-write, 3 nucs')
ll.get_texts()[1].set_text('no-write, 8 nucs')
ll.get_texts()[2].set_text('no-write, 23 nucs')
ll.get_texts()[3].set_text('write, 3 nucs')
ll.get_texts()[4].set_text('write, 8 nucs')
ll.get_texts()[5].set_text('write, 23 nucs')
ll.set_title('Write Flag & Nucs Tracked')
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

ax = ts_no_3.plot(x='DbSize', y='Time', kind='line', legend=False)
ts_no_8.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)
ts_no_23.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)
ts_w_3.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)
ts_w_8.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)
ts_w_23.plot(ax = ax, x='DbSize', y='Time', kind='line', legend=False)

lll = plt.legend()
lll.get_texts()[0].set_text('no-write, 3 nucs')
lll.get_texts()[1].set_text('no-write, 8 nucs')
lll.get_texts()[2].set_text('no-write, 23 nucs')
lll.get_texts()[3].set_text('write, 3 nucs')
lll.get_texts()[4].set_text('write, 8 nucs')
lll.get_texts()[5].set_text('write, 23 nucs')
lll.set_title('Write Flag & Nucs Tracked')
plt.show()

