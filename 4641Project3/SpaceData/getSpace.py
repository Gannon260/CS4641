# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 21:28:42 2018

@author: PeterLee
"""

import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler
dtype={'user_id': float}
dataset = pd.read_csv("SpaceData.csv")  
X = dataset.iloc[:, range(0, 15)].values  
y = dataset.iloc[:, 15].values
X_train_raw, X_test_raw, Y_train_raw, Y_test_raw = train_test_split(X, y, test_size=.25)

Xscaler = StandardScaler()  
X_train = Xscaler.fit_transform(X_train_raw)  
X_test = Xscaler.transform(X_test_raw)

Yscaler = StandardScaler()
Y_train = Y_train_raw
Y_test = Y_test_raw