#! /usr/bin/python3
# coding: utf-8
"""Functions used for COVID project."""
import pandas as pd
import os
import numpy as np
from python3.functions import get_files, get_value
from python3.covid_dicts import df_treshold_pDCs,  dict_samples_pDCs
from python3.covid_dicts import df_treshold_mDC1s,  dict_samples_mDC1s
from python3.covid_dicts import df_treshold_mono,  dict_samples_mono
from python3.covid_dicts import df_treshold_mDC2, dict_samples_mDC2
"""
Expected columns:
FSC-A, FSC-H, FSC-W, SSC-A, SSC-H, SSC-W
IFNa, CD80, viab, HLA-DR, CD11c, CD123, CD2, Lin(CD3 14 16 19 20 56 14)
IFN-Lambda, PD-L1, CD83, BDCA3
"""

def test_equality(array1,
                  array2):
    """Test if both array are equal position at position."""
    res = True
    for i in range (len(array1)):
        if array1[i] != array2[i]:
            res = False
    return res

def build_database(folder,
                   ext,
                   activation=None):
    """Builds a dataframe as database and one for display files seen."""
    # Generate databases for all cell types
    (df_db_pDCs,
     df_val_pDCs,
     df_summary_pDCs) = extract_pDCs(folder,
                                     ext)
    (df_db_mDC1s,
     df_val_mDC1s,
     df_summary_mDC1s) = extract_mDC1s(folder,
                                       ext)
    """
    (df_db_mono,
     df_val_mono,
     df_summary_mono) = extract_mono(folder,
                                     ext)
    """
    # get all samples IDs
    pdcs = df_summary_pDCs['Sample'].values
    mdcs = df_summary_mDC1s['Sample'].values
    #monos = df_summary_mono['Sample'].values

    # get samples present in all dataframe
    list_ok = []
    for element in pdcs:
        if (element in mdcs):
            list_ok = np.append(list_ok, element)

    # reduce dataframe to the common samples
    df_summary_pDCs = df_summary_pDCs[df_summary_pDCs['Sample'].isin(list_ok)]
    df_summary_mDC1s = df_summary_mDC1s[df_summary_mDC1s['Sample'].isin(list_ok)]
    #df_summary_mono = df_summary_mono[df_summary_mono['Sample'].isin(list_ok)]
    print('merging')
    df_summary = pd.merge(df_summary_pDCs,
                          df_summary_mDC1s)
    #df_summary = pd.merge(df_summary,
    #                      df_summary_mono)
    df_summary = df_summary.reset_index(drop=True)
    print('Summary')
    df_db = df_db_pDCs
    print('DataBase')
    df_validation = df_val_pDCs
    print('Validation')

    return df_db, df_validation, df_summary

def extract_pDCs(folder,
                 ext,
                 activation=None):
    """Get values of the pDCs."""
    print('Building pDCs database')
    dict_samples = dict_samples_pDCs
    df_treshold = df_treshold_pDCs
    folder = os.path.join(folder,
                          'pDCs')
    df_db = pd.DataFrame()
    df_validation = pd.DataFrame()
    df_summary = pd.DataFrame(columns = ['Sample',
                                         'Cohorte',
                                         'Status',
                                         'Activation_Mock',
                                         'Activation_SARS',
                                         'Activation_Agonist',
                                         'perc_pDCs',
                                         'pDCs_ IFNl',
                                         'pDCs_CD83',
                                         'pDCs_PDL1',
                                         'pDCs_IFNa',
                                         'pDCs_IFNahi',
                                         'pDCs_CD80'])

    files = get_files(folder,
                      ext)
    for file in files:

        df = pd.read_csv(folder + os.sep + file)
        # Name without extension
        key = file.replace(ext, '')

        if (((key in dict_samples.keys()) and
            (activation is None)) or (
            (key in dict_samples.keys()) and
            (dict_samples[key][2] == activation)
            )):
            sample = key.replace('_pDCs_', '_')
            # Add IFNahi column
            df['IFNahi'] = df['IFNa']
            # Select columns and rename them
            df = df[df_treshold.columns]
            new_columns = ['pDCs_' + col for col in df_treshold.columns]
            df.columns = new_columns

            df['Sample'] = sample
            df['Cohorte'] =  dict_samples[key][6]
            Activation =  dict_samples[key][2]

            if Activation ==  'Mock':
                activation_mock = 1
                activation_sars = 0
                activation_agonist = 0

            elif Activation ==  'SARS':
                activation_mock = 0
                activation_sars = 1
                activation_agonist = 0

            elif Activation ==  'Agonist':
                activation_mock = 0
                activation_sars = 0
                activation_agonist = 1

            df['Activation_Mock'] = activation_mock
            df['Activation_SARS'] = activation_sars
            df['Activation_Agonist'] = activation_agonist

            status = dict_samples[key][0]
            if (status in ['mild-early', 'mild-late']):
                status = 'mild'
            df['Status'] = status
            df['perc_pDCs'] =  dict_samples[key][5]

            info_array = [sample,
                           dict_samples[key][6],
                           status,
                           activation_mock,
                           activation_sars,
                           activation_agonist,
                           dict_samples[key][5],
                          ]

            for c in df_treshold.columns:

                threshold = get_value(df_treshold,
                                      c,
                                      dict_samples[key][6])
                df['pDCs_' + c] = np.where(df['pDCs_' + c] < threshold,
                                           0,
                                           1)
                info_array.append(round(100 * df['pDCs_' + c].mean(), 2))


            if  dict_samples[key][4] == 'modeling':
                df_db = pd.concat([df_db, df],
                                  ignore_index=True)
            else:
                df_validation = pd.concat([df_validation, df],
                                          ignore_index=True)
            df_summary.loc[len(df_summary.index)] = info_array

    df_summary = df_summary.sort_values(by='Sample',
                                        ascending=True)


    df_db = df_db.sort_values(by='Sample',
                              ascending=True)

    if df_validation.shape[0] > 0:
        df_validation = df_validation.sort_values(by='Sample',
                                                  ascending=True)

    return df_db, df_validation, df_summary


def extract_mDC1s(folder,
                  ext,
                  activation=None):
    """Get values of the mDC1s."""
    print('Building mDC1s database')
    dict_samples = dict_samples_mDC1s
    df_treshold = df_treshold_mDC1s
    folder = os.path.join(folder,
                          'mDC1s')
    df_db = pd.DataFrame()
    df_validation = pd.DataFrame()
    df_summary = pd.DataFrame(columns = ['Sample',
                                         'Cohorte',
                                         'Status',
                                         'Activation_Mock',
                                         'Activation_SARS',
                                         'Activation_Agonist',
                                         'perc_mDC1s',
                                         'mDC1s_IFNl',
                                         'mDC1s_CD83',
                                         'mDC1s_PDL1',
                                         'mDC1s_IFNa',
                                         'mDC1s_IFNahi',
                                         'mDC1s_CD80'])
    files = get_files(folder,
                      ext)
    for file in files:

        df = pd.read_csv(folder + os.sep + file)
        # Name without extension
        key = file.replace(ext, '')

        if (((key in dict_samples.keys()) and
            (activation is None)) or (
            (key in dict_samples.keys()) and
            (dict_samples[key][2] == activation)
            )):
            sample = key.replace('_mDC1s_', '_')
            # Add IFNahi column
            df['IFNahi'] = df['IFNa']
            # Select columns and rename them
            cols = df_treshold.columns
            df = df[cols]
            new_columns = ['mDC1s_' + col for col in df_treshold.columns]
            df.columns = new_columns

            df['Sample'] = sample
            status = dict_samples[key][0]
            if (status in ['mild-early', 'mild-late']):
                status = 'mild'
            df['Status'] = status
            df['Cohorte'] =  dict_samples[key][6]
            Activation =  dict_samples[key][2]
            if Activation ==  'Mock':
                activation_mock = 1
                activation_sars = 0
                activation_agonist = 0

            elif Activation ==  'SARS':
                activation_mock = 0
                activation_sars = 1
                activation_agonist = 0

            elif Activation ==  'Agonist':
                activation_mock = 0
                activation_sars = 0
                activation_agonist = 1

            df['Activation_Mock'] = activation_mock
            df['Activation_SARS'] = activation_sars
            df['Activation_Agonist'] = activation_agonist
            df['perc_mDC1s'] =  dict_samples[key][5]

            info_array = [sample,
                          dict_samples[key][6],
                          status,
                          activation_mock,
                          activation_sars,
                          activation_agonist,
                          dict_samples[key][5],
                          ]

            for c in df_treshold.columns:

                threshold = get_value(df_treshold,
                                      c,
                                      dict_samples[key][6])
                df['mDC1s_' + c] = np.where(df['mDC1s_' + c] < threshold,
                                            0,
                                            1)
                info_array.append(round(100 * df['mDC1s_' + c].mean(), 2))

            if  dict_samples[key][4] == 'modeling':
                df_db = pd.concat([df_db, df],
                                  ignore_index=True)
            else:
                df_validation = pd.concat([df_validation, df],
                                          ignore_index=True)
            df_summary.loc[len(df_summary.index)] = info_array

    df_summary = df_summary.sort_values(by='Sample',
                                        ascending=True)
    df_db = df_db.sort_values(by='Sample',
                              ascending=True)
    if df_validation.shape[0] > 0:
        df_validation = df_validation.sort_values(by='Sample',
                                                  ascending=True)

    return df_db, df_validation, df_summary


def extract_mono(folder,
                 ext,
                 activation=None):
    """Get values of the mono."""
    print('Building mono database')
    dict_samples = dict_samples_mono
    df_treshold = df_treshold_mono
    folder = os.path.join(folder,
                          'mono')
    df_db = pd.DataFrame()
    df_validation = pd.DataFrame()
    df_summary = pd.DataFrame(columns = ['Sample',
                                         'Cohorte',
                                         'Status',
                                         'Activation_Mock',
                                         'Activation_SARS',
                                         'Activation_Agonist',
                                         'perc_mono',
                                         'mono_PDL1',
                                         'mono_CD80',
                                         'mono_IL6',
                                         'perc_CD14_conv',
                                         'perc_CD16-CD14_int',
                                         'perc_CD16-CD14_dim_non_conv'])
    files = get_files(folder,
                      ext)
    for file in files:

        df = pd.read_csv(folder + os.sep + file)
        # Name without extension
        key = file.replace(ext, '')

        if (((key in dict_samples.keys()) and
            (activation is None)) or (
            (key in dict_samples.keys()) and
            (dict_samples[key][2] == activation)
            )):
            sample = key.replace('_mono_', '_')
            # Select columns and rename them
            cols = df_treshold.columns
            df = df[cols]
            new_columns = ['mono_' + col for col in df_treshold.columns]
            df.columns = new_columns

            df['Sample'] = sample
            status = dict_samples[key][0]
            if (status in ['mild-early', 'mild-late']):
                status = 'mild'
            df['Status'] = status
            df['Cohorte'] =  dict_samples[key][6]
            Activation =  dict_samples[key][2]
            if Activation ==  'Mock':
                activation_mock = 1
                activation_sars = 0
                activation_agonist = 0

            elif Activation ==  'SARS':
                activation_mock = 0
                activation_sars = 1
                activation_agonist = 0

            elif Activation ==  'Agonist':
                activation_mock = 0
                activation_sars = 0
                activation_agonist = 1

            df['Activation_Mock'] = activation_mock
            df['Activation_SARS'] = activation_sars
            df['Activation_Agonist'] = activation_agonist
            df['perc_mono'] =  dict_samples[key][5]
            df['perc_CD14_conv'] = dict_samples[key][7]
            df['perc_CD16-CD14_int'] = dict_samples[key][8]
            df['perc_CD16-CD14_dim_non_conv'] = dict_samples[key][9]

            info_array = [sample,
                          dict_samples[key][6],
                          status,
                          activation_mock,
                          activation_sars,
                          activation_agonist,
                          dict_samples[key][5],
                          dict_samples[key][7],
                          dict_samples[key][8],
                          dict_samples[key][9]
                          ]

            for c in df_treshold.columns:

                threshold = get_value(df_treshold,
                                      c,
                                      dict_samples[key][6])
                df['mono_' + c] = np.where(df['mono_' + c] < threshold,
                                            0,
                                            1)
                info_array.append(round(100 * df['mono_' + c].mean(), 2))

            if  dict_samples[key][4] == 'modeling':
                df_db = pd.concat([df_db, df],
                                  ignore_index=True)
            else:
                df_validation = pd.concat([df_validation, df],
                                          ignore_index=True)
            df_summary.loc[len(df_summary.index)] = info_array

    df_summary = df_summary.sort_values(by='Sample',
                                        ascending=True)
    df_db = df_db.sort_values(by='Sample',
                              ascending=True)
    if df_validation.shape[0] > 0:
        df_validation = df_validation.sort_values(by='Sample',
                                                  ascending=True)

    return df_db, df_validation, df_summary

def extract_mDC2s(folder,
                  ext,
                  activation=None):
    """Get values of the mono."""
    print('Building mDC2s database')
    dict_samples = dict_samples_mDC2
    df_treshold = df_treshold_mDC2
    folder = os.path.join(folder,
                          'mDC2')
    df_db = pd.DataFrame()
    df_validation = pd.DataFrame()
    df_summary = pd.DataFrame(columns = ['Sample',
                                         'Cohorte',
                                         'Status',
                                         'Activation_Mock',
                                         'Activation_SARS',
                                         'Activation_Agonist',
                                         'perc_mDC2s',
                                         'mDC2s_PDL1',
                                         'mDC2s_CD80',
                                         'mDC2s_IL6'])
    files = get_files(folder,
                      ext)
    for file in files:

        df = pd.read_csv(folder + os.sep + file)
        # Name without extension
        key = file.replace(ext, '')

        if (((key in dict_samples.keys()) and
            (activation is None)) or (
            (key in dict_samples.keys()) and
            (dict_samples[key][2] == activation)
            )):
            sample = key.replace('_mono_', '_')
            # Select columns and rename them
            cols = df_treshold.columns
            df = df[cols]
            new_columns = ['mDC2s_' + col for col in df_treshold.columns]
            df.columns = new_columns

            df['Sample'] = sample
            status = dict_samples[key][0]
            if (status in ['mild-early', 'mild-late']):
                status = 'mild'
            df['Status'] = status
            df['Cohorte'] =  dict_samples[key][6]
            Activation =  dict_samples[key][2]
            if Activation ==  'Mock':
                activation_mock = 1
                activation_sars = 0
                activation_agonist = 0

            elif Activation ==  'SARS':
                activation_mock = 0
                activation_sars = 1
                activation_agonist = 0

            elif Activation ==  'Agonist':
                activation_mock = 0
                activation_sars = 0
                activation_agonist = 1

            df['Activation_Mock'] = activation_mock
            df['Activation_SARS'] = activation_sars
            df['Activation_Agonist'] = activation_agonist
            df['perc_mDC2s'] =  dict_samples[key][5]

            info_array = [sample,
                          dict_samples[key][6],
                          status,
                          activation_mock,
                          activation_sars,
                          activation_agonist,
                          dict_samples[key][5]
                          ]

            for c in df_treshold.columns:

                threshold = get_value(df_treshold,
                                      c,
                                      dict_samples[key][6])
                df['mDC2s_' + c] = np.where(df['mDC2s_' + c] < threshold,
                                            0,
                                            1)
                info_array.append(round(100 * df['mDC2s_' + c].mean(), 2))

            if  dict_samples[key][4] == 'modeling':
                df_db = pd.concat([df_db, df],
                                  ignore_index=True)
            else:
                df_validation = pd.concat([df_validation, df],
                                          ignore_index=True)
            df_summary.loc[len(df_summary.index)] = info_array

    df_summary = df_summary.sort_values(by='Sample',
                                        ascending=True)
    df_db = df_db.sort_values(by='Sample',
                              ascending=True)
    if df_validation.shape[0] > 0:
        df_validation = df_validation.sort_values(by='Sample',
                                                  ascending=True)

    return df_db, df_validation, df_summary
