#! /usr/bin/python3
# coding: utf-8

import os
import time
from python3.covidfunctions import build_database
from python3.covidfunctions import extract_pDCs, extract_mDC1s
from python3.covidfunctions import extract_mono, extract_mDC2s
from python3.gradientboosting_tree_classifer import classifier
from python3.scikitlearn_pipelines import GBC_pipeline, HistGBC_pipeline
from python3.scikitlearn_tools import separate_data_and_target
from sklearn.model_selection import train_test_split
from python3.quality_control import lets_them_vote
from python3.functions import project_time_stamp
from python3.functions import list_files_in_dict, get_matches
from python3.results_analysis import get_vote_accuracy
from python3.scikitlearn_tools import KFold_crossvalidation
from python3.scikitlearn_tools import shufflesplit_crossvalidation
from python3.results_analysis import estimate_score, estimate_importance

# Input folder
input = '/home/dcluet/Bureau/Programmes/2022_Covid_Multinomial/src/data'
# Output folder
folder_output = '/home/dcluet/Bureau/ML_test'
# Proportion of the validation set
validation_frac = 0.2
number_of_splits = 10


def covid():
    """Perform ML on COVID data."""
    # Create the database
    df_db, df_validation, df_summary = extract_mono(input,
                                                    '.csv')

    print(df_summary['Status'].value_counts())
    # Prepare the output folder
    footprint = f'_{validation_frac}_COVID_'
    output = os.path.join(folder_output ,
                          project_time_stamp() + footprint)
    os.mkdir(output)
    # Save database for inspection
    df_summary.to_csv(os.path.join(output,
                                   'summary_database.csv'))


    # Perform 10 build-validation couples sets
    for val in range(0, 10, 1):
        # Use a different seed for each build/validation sets combinations
        lcl_seed = 666 + val

        # Separtrate build and validation sets at the scale of the samples
        # Here we work at the sample level
        (data,
         target) = separate_data_and_target(df_summary,
                                            'Status')
        if validation_frac > 0:
            (modeling,
             validation,
             target_modeling,
             target_validation) = train_test_split(data,
                                                   target,
                                                   shuffle=True,
                                                   test_size=validation_frac,
                                                   random_state=lcl_seed)
        else:
            modeling = data
            validation = data
            target_modeling = target
            target_validation = target

        patient_modeling = modeling
        patient_modeling['Status'] = target_modeling
        patient_modeling = patient_modeling.reset_index(drop=True)
        patient_validation = validation
        patient_validation['Status'] = target_validation
        patient_validation = patient_validation.reset_index(drop=True)


        # Transform these patient level sets into single cell level sets
        unique_modeling = modeling.Sample.unique()
        unique_validation = validation.Sample.unique()
        df_modeling = df_db.loc[df_db['Sample'].isin(unique_modeling)]
        df_modeling = df_modeling.reset_index(drop=True)
        df_validation = df_db.loc[df_db['Sample'].isin(unique_validation)]
        df_validation = df_validation.reset_index(drop=True)
        # Print general information about the current analysis
        print(project_time_stamp() + f" Validation set number {val}")
        print('Building set')
        print(df_modeling['Status'].value_counts())
        print('Validation set')
        print(df_validation['Status'].value_counts())
        # Execute the machine learning pipeline
        modelling = classifier(patient_modeling,
                               'Status',
                               output,
                               columns_to_exclude=['Cohorte',
                                                   #'perc_pDCs',
                                                   #'perc_mDC1s',
                                                   #'perc_mDC2s',
                                                   'perc_mono',
                                                   'Sample',
                                                   'Activation_Mock',
                                                   'Activation_SARS',
                                                   'Activation_Agonist']
,
                               # 'perc_pDCs'
                               dataframe_validation=patient_validation,
                               pipeline=GBC_pipeline,
                               crossvalidation=shufflesplit_crossvalidation,
                               n_splits=number_of_splits,
                               save_split_models=True,
                               processes=10,
                               suffix=val,
                               perform_qc_on_prediction=lets_them_vote,
                               arguments_for_qc=['Sample',
                                                 'Status',
                                                 'Prediction'])
    # Get all vote prediction accuracy
    estimate_score(output,
                   'GradientBoostClassifier_[0-9].csv')
    estimate_importance(output,
                        'GradientBoostClassifier_[0-9].csv',
                        filter_step='Validation_mean',
                        xmin=-0.05,
                        xmax=0.3)
    """
    get_vote_accuracy(output,
                      'Vote_*.csv',
                      'Status',
                      'Prediction')
    """

if __name__ == "__main__":
   covid()
