# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:47:10 2021

@author: NANDA
"""


import mplsoccer as mpl
import pandas as pd

import os
import sys
import numpy as np
sys.path.append(os.pardir)

import helper


match_id = '0'
data_path = os.path.join(os.pardir, 'data','20_21',match_id+'.csv')


df = pd.read_csv(data_path)

df = df.query('type_displayName not in @helper.ex_list').reset_index()


df_plot = df.iloc[15:15+8]


x = [60.0,78.0,100.0-17.6,100.0-17.6,56.1,100.0-32.1,63.7,100.0-40.2]

y = [100,93.5,100-10,100-9.2,85.3,100-27.7,63.5,100-65.1]

endX = [78,81.5,np.nan,100-42.4,66.5,np.nan,59.8,100-31.1]

endY = [93.5,92.1,np.nan,100-14.3,80,np.nan,35.9,100-74.1]

pitch = mpl.Pitch('opta')


fig, ax = pitch.draw(figsize=(8, 4))



pitch.scatter(endX,endY,ax=ax)
pitch.scatter(x, y, ax=ax)
pitch.lines(x, y, endX, endY, ax=ax,comet=True,linewidth=0.2)


pitch.scatter(df_plot.endX,df_plot.endY,ax=ax)
pitch.lines(df_plot.x, df_plot.y, df_plot.endX, df_plot.endY, ax=ax,comet=True,linewidth=0.2)


    # "        df_all = pd.read_csv(f\"../data/20_21/{match_id}.csv\")\n",
    # "        \n",
    # "        df_all = df_all.query('type_displayName not in @ex_list').reset_index()

helper.ex_list?
