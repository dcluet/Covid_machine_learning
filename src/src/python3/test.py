#! /usr/bin/python3
# coding: utf-8
"""Test for communication with R."""
import os
from functions import get_files
from plots import confusion_matrix
import pandas as pd
from functions import list_files_in_dict, get_matches
import numpy as np
import math
from plots import boxplot

d = list_files_in_dict('/home/dcluet/Bureau/ML_test/2022-04-06_Wed_08-06-25_COVID',
                       'Vote_*.csv')

means_list = np.empty((0,10), int)
idx = 0
labels = []
for k in d.keys():
    lcl_mean = []
    list_files = d[k]
    for f in list_files:
        lcl_mean = np.append(lcl_mean,
                             get_matches(os.path.join(k, f),
                                         'Status',
                                         'Prediction'))
    means_list = np.append(means_list,
                           [lcl_mean],
                           axis=0)
    labels = np.append(labels, idx)
    idx += 1


boxplot(means_list.T,
        labels,
        'Accuraccy',
        'COVID.png',
        title='Accuracy over the Build/Validation sets',
        fingerprint='',
        values_2=None,
        name_2='')
