#! /usr/bin/python3
# coding: utf-8
"""Quality control functions for prediction."""
import pandas as pd
import numpy as np
import os
from python3.plots import confusion_matrix

def lets_them_vote(dataframe,
                   columns_list,
                   folder,
                   suffix):
    """Perform majoritary vote on prediction and compare with expected."""
    ref_col = columns_list[0]
    target_col = columns_list[1]
    predicted_col = columns_list[2]

    # get all unique values (samples) in ref column
    IDs = dataframe[ref_col].unique()
    target = []
    prediction = []
    for id in IDs:
        # Get the sub-dataframe for a specific sample
        df_4_vote = dataframe.loc[dataframe[ref_col] == id]
        # Get the value with the max count in the target column
        lcl_target = df_4_vote[target_col].value_counts().idxmax()
        # Get the value with the max count in the prediction column column
        lcl_pred = df_4_vote[predicted_col].value_counts().idxmax()
        # Store the main target and prediction values
        target = np.append(target,
                           lcl_target)
        prediction = np.append(prediction,
                               lcl_pred)
    # Build the output dataframe transforming single cell prediction
    # into sample "elected" prediction
    bilan_df = pd.DataFrame({'Sample': IDs,
                             'Status': target,
                             'Prediction': prediction})

    bilan_df.to_csv(folder +
                    os.sep +
                    f'Vote_Downsampling_{suffix}.csv')
    # Generate confusion matrixes for visual inspection
    df = pd.DataFrame({'Observed': target,
                       'Predicted': prediction})
    confusion_matrix(df,
                     folder,
                     pondarated=True,
                     fingerprint=f'Downsampling {suffix}')
    confusion_matrix(df,
                     folder,
                     pondarated=False,
                     fingerprint=f'Downsampling {suffix}')
