#! /usr/bin/python3
# coding: utf-8
import os
from python3.functions import list_files_in_dict
import pandas as pd
import numpy as np
from python3.plots import boxplot
from python3.functions import get_matches
from python3.scikitlearn_tools import clean_db
import time



def get_vote_accuracy(folder,
                      file_pattern,
                      column1,
                      column2):
    """Generate boxplots to follow vote accuracy over validation set."""
    # Get all vote files as list for a specific validation set
    dict_votes = list_files_in_dict(folder,
                                    file_pattern)
    # Study the variability of the vote within the downsamplings of each set
    means_list = np.empty((0,10), int)
    idx = 0
    labels = []
    for k in dict_votes.keys():
        lcl_mean = []
        list_files = dict_votes[k]
        for f in list_files:
            lcl_mean = np.append(lcl_mean,
                                 get_matches(os.path.join(k, f),
                                             column1,
                                             column2))
        means_list = np.append(means_list,
                               [lcl_mean],
                               axis=0)
        labels = np.append(labels, idx)
        idx += 1
    # Generate the boxplot
    fingerprint = f'\nmean = {round(np.mean(means_list), 2)}'
    fingerprint += f' +/- {round(np.std(means_list), 2)}'
    boxplot(means_list.T,
            labels,
            'Accuraccy',
            os.path.join(folder,
                         'Vote_accuracies.pdf'),
            title='Vote Accuracy over Validation sets',
            fingerprint=fingerprint,
            values_2=None,
            name_2='')


def estimate_importance(folder,
                        file_pattern,
                        filter_step='Validation_mean',
                        xmin=None,
                        xmax=None):
    """Generate the boxplot for each parameter importance."""
    # Get all files containg our data
    dict_importances = list_files_in_dict(folder,
                                          file_pattern)
    # Generate the 2D array with the means
    parameters = []
    means = np.empty(0)
    for key in dict_importances.keys():
        # Open the current file
        current_df = pd.read_csv(os.path.join(key,
                                              dict_importances[key][0]))
        if current_df.shape[0] > 0:
            # Get only the lines of iterest
            filter = current_df['Step'].str.contains(filter_step)
            current_df = current_df[filter]
            # remove unwanted columns
            current_df = clean_db(current_df,
                                  ['Unnamed: 0',
                                   'Downsampling',
                                   'accuracy_train',
                                   'accuracy_test',
                                   'accuracy_build',
                                   'accuracy_validation'])
            # Calculate the mean of each parameter
            mean_df = current_df.mean()
            # If firts round, initiate the 2D array and the parameter list
            if len(parameters) == 0:
                parameters = mean_df.index.values
                means = np.empty((0,
                                  len(parameters)))
            lcl_means = mean_df.values
            # Store the local means
            means = np.append(means,
                              [lcl_means],
                              axis=0)
    # Create the graph
    if means.shape[0] > 1:
        boxplot(means,
                parameters,
                'Accuraccy',
                os.path.join(folder,
                             f'Parameters_importance_{filter_step}.pdf'),
                title='Parameters importance',
                xmin=xmin,
                xmax=xmax)



def estimate_score(folder,
                   file_pattern):
    """Generate boxplots to follow vote accuracy over downsamplings."""
    # Get all vote files as list for a specific validation set
    dict_votes = list_files_in_dict(folder,
                                    file_pattern)
    # Study the variability of the vote within the downsamplings of each set
    idx = 0
    labels = []
    means_valid_list = np.empty(0)
    for k in dict_votes.keys():
        lcl_mean = []
        list_files = dict_votes[k]
        for f in list_files:

            # Open the csv file of the current subset
            df_lcl = pd.read_csv(os.path.join(k, f))
            if df_lcl.shape[0] > 0:
                # Get only the row of interest
                df_lcl = df_lcl.loc[df_lcl['Step'] == 'Validation_mean']
                means_build = df_lcl['accuracy_build'].values
                means_valid = df_lcl['accuracy_validation'].values

                # Store the values
                if idx == 0:
                    n = len(means_build)
                    means_build_list = np.empty((0, n), int)
                    means_valid_list = np.empty((0, n), int)
                means_build_list = np.append(means_build_list,
                                             [means_build],
                                             axis=0)
                means_valid_list = np.append(means_valid_list,
                                             [means_valid],
                                             axis=0)
                labels = np.append(labels, f'Dataset {idx}')
                idx += 1
    # Generate the boxplot
    if means_valid_list.shape[0] > 1:
        fingerprint = f'\nmean = {round(np.mean(means_valid_list), 2)}'
        fingerprint += f' +/- {round(np.std(means_valid_list), 2)}'
        boxplot(means_valid_list.T,
                labels,
                'Accuraccy',
                os.path.join(folder,
                             'Tracking_Validation_accuracies.pdf'),
                title='Accuracy over the Build datasets sets',
                fingerprint=fingerprint,
                values_2=None,
                name_2=None,
                xmin=0,
                xmax=1)
        fingerprint = f'\nmean = {round(np.mean(means_build_list), 2)}'
        fingerprint += f' +/- {round(np.std(means_build_list), 2)}'
        boxplot(means_build_list.T,
                labels,
                'Accuraccy',
                os.path.join(folder,
                             'Tracking_Build_accuracies.pdf'),
                title='Accuracy over the Build datasets sets',
                fingerprint=fingerprint,
                values_2=None,
                name_2=None,
                xmin=0,
                xmax=1)
