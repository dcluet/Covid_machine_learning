#! /usr/bin/python3
# coding: utf-8
"""Various plot functions."""
import matplotlib as mpl
mpl.use('Agg')  # To aalow multi processes with matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


def confusion_matrix(dataframe,
                     folder,
                     fingerprint='',
                     cmap='cool',
                     pondarated=False):
    """Generate a confusion matrix even in multi-processes."""
    # The dataframe shouldbe formated with two columns:
    # ['Oberved', 'Predicted']
    df = dataframe[['Observed', 'Predicted']]
    # Detect all unique values present in Observed AND Predicted and sort them
    uniques = np.sort(np.unique(np.append(df['Observed'].unique(),
                                         df['Predicted'].unique())))
    fontsize = round(16 * 4 / uniques.shape[0])
    # Create dictionary for pondaration
    if pondarated is True:
        fingerprint = f'pondarated {fingerprint}'
        dict_pond = {}
        for u in uniques:
            dict_pond[u] = df.loc[(df['Observed'] == u)].shape[0]
        vmin = 0
        vmax = 2
        cmap = 'bwr'

    # Create the dictionnary to generate the correlation matrix
    dict = {}
    for key in uniques:
        dict[key] = []
    # Create the confusion_matrix
    for observed in uniques:
        for predicted in uniques:
            hits = df.loc[((df['Observed'] == observed) &
                           (df['Predicted'] == predicted))].shape[0]
            if pondarated is True:
                if dict_pond[observed] != 0:
                    hits = hits / dict_pond[observed]
                else:
                    hits = np.nan
            dict[observed] = np.append(dict[observed], hits)
    conf_mat = pd.DataFrame(dict,
                            index=uniques)
    # Set the min and max values
    if pondarated is False:
        vmin = np.min(conf_mat.min())
        vmax = np.max(conf_mat.max())
    # Create the graphical representation
    fig, ax = plt.subplots(figsize=(8,16))
    im = ax.imshow(conf_mat,
                   cmap=cmap,
                   vmin=vmin,
                   vmax=vmax,
                   interpolation='nearest')
    fig.colorbar(im,
                 orientation='horizontal',
                 fraction = 0.05)
    # Show all ticks and label them with the classes
    ax.set_xticks(range(uniques.shape[0]))
    ax.set_xticklabels(uniques,
                       rotation=90,
                       fontsize=fontsize)
    ax.set_xlabel('Observed',
                  fontsize=16)
    ax.set_yticks(range(uniques.shape[0]))
    ax.set_yticklabels(uniques,
                       rotation=0,
                       fontsize=fontsize)
    ax.set_ylabel('Predicted',
                  fontsize=16)
    # Loop over confusion matrix dimensions and create text annotations
    for i in range(uniques.shape[0]):
        for j in range(uniques.shape[0]):
            text = ax.text(j,
                           i,
                           round(conf_mat.to_numpy()[i, j], 2),
                           ha='center',
                           va='center',
                           color='black',
                           fontsize=fontsize)
    plt.title(f'Confusion matrix {fingerprint}',
              fontsize=16)
    path_graph = folder + os.sep + f'Confusion_matrix_{fingerprint}.pdf'
    plt.savefig(path_graph,
                bbox_inches='tight')
    plt.close()


def boxplot(values_1,
            labels_1,
            name_1,
            path_graph,
            title='Permutation Importances',
            fingerprint='',
            values_2=None,
            name_2='',
            xmin=None,
            xmax=None):
    """Generate Boxplot."""
    # structure of the dict_value entry:
    # name_serie: (importances_val[sorted_idx].T,
    #                data_build.columns[sorted_idx])
    # Personal color code
    color_code = ['mediumslateblue',
                  'crimson',
                  'limegreen',
                  'goldenrod']

    # number of series
    fig, ax = plt.subplots()
    if values_2 is not None:
        bp1 = ax.boxplot(values_1,
                         positions = range(1, 2 * labels_1.shape[0], 2),
                         notch=True,
                         vert=False,
                         labels=labels_1,
                         patch_artist=True,
                         boxprops=dict(facecolor=color_code[0])
                         )
        bp2 = ax.boxplot(values_2,
                         positions = range(0, 2 * labels_1.shape[0], 2),
                         notch=True,
                         vert=False,
                         labels=labels_1,
                         patch_artist=True,
                         boxprops=dict(facecolor=color_code[1])
                         )
        ax.legend([bp1['boxes'][0],
                   bp2['boxes'][0]],
                  [name_1, name_2],
                  bbox_to_anchor=(1.05, 0.8),
                  loc='upper left')
    else:
        ax.boxplot(values_1,
                   notch=True,
                   vert=False,
                   labels=labels_1,
                   patch_artist=True,
                   boxprops=dict(facecolor=color_code[0])
                   )

    ax.set_title(f"{title} {fingerprint}")
    if (xmin is not None and xmax is not None):
        ax.set_xlim([xmin, xmax])
    ax.set_aspect(1.0 / ax.get_data_ratio(),
                  adjustable='box')
    fig.tight_layout()

    plt.savefig(path_graph,
                bbox_inches='tight')
    plt.close()
