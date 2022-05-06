#! /usr/bin/python3
# coding: utf-8
"""Utils functions."""
import pandas as pd
import os
import time
import glob
import numpy as np
from python3.plots import boxplot


def get_matches(path_csv,
                col1,
                col2):
    """Open csv file and get percent of matches between the 2 columns."""
    # Open the csv file as a pandas dataframe
    df = pd.read_csv(path_csv)
    n_lines = df.shape[0]
    # find the lines were the 2 columns of interest have the same value
    df_ok = df.loc[df[col1] == df[col2]]
    # Return result as a percentage of the lines
    perc = round(100 * df_ok.shape[0] / n_lines, 2)
    return perc


def list_files_in_dict(folder,
                       pattern):
    """Find all files with pattern recursively and create a dict."""
    regex_path = folder + os.sep + '**' + os.sep + pattern
    dict = {}
    for file_path in glob.iglob(regex_path, recursive = True):
        lcl_folder = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        # Initiate a new key
        if lcl_folder not in dict.keys():
            dict[lcl_folder] = [file_name]
        # Store new values for a key
        else:
            dict[lcl_folder] = np.append(dict[lcl_folder],
                                         file_name)
    return dict


def get_files(folder,
              extension):
    """Returns array with all files with extension in the folder."""
    files = []
    for f in os.listdir(folder):
        if f.endswith(extension):
            files.append(f)
    return files


def get_value(dataframe,
              column_name,
              index_value):
    """Returns the value of the specific column/index values couple."""
    return dataframe[column_name].loc[[index_value]].values[0]


def project_time_stamp():
    """Generates a time stamp for project folders."""
    current_time = time.localtime()
    stamp = time.strftime('%Y-%m-%d_%a_%H-%M-%S',
                          current_time)
    return stamp


def create_machine_learning_folders(root,
                                    time_stamp,
                                    project):
    """Create internal arborescence for the modelling analysis."""
    # Project folder
    project_folder = os.path.join(root, f'{time_stamp}_{project}')
    # Graphs folder
    graphs_folder = os.path.join(project_folder, 'graphs')
    # Models folder
    models_folder = os.path.join(project_folder, 'models')

    for folder in [project_folder,
                   graphs_folder,
                   models_folder]:
        os.mkdir(folder)
    return project_folder
