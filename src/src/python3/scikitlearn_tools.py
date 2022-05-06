#! /usr/bin/python3
# coding: utf-8
"""Tools to simplify the usage of scikit-learn package."""
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
import sys
import matplotlib as mpl
import math
mpl.use('Agg')
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance
from joblib import dump, load
from python3.plots import boxplot


def get_importance_validation(df,
                              model,
                              data_build,
                              target_build,
                              data_validation,
                              target_validation,
                              iteration,
                              folder,
                              scoring,
                              lcl_seed):
    """Get features importances at the validation step."""
    model.fit(data_build, target_build)
    build_accuracy = model.score(data_build, target_build)
    # "Predict on the test set"
    validation_accuracy = model.score(data_validation, target_validation)

    # Prepare graph and model path
    path_graph = os.path.join(folder,
                              'graphs',
                              'Importance_' + str(iteration) + '.png')
    path_model = os.path.join(folder,
                              'models',
                              'Model_' + str(iteration) + '.joblib')
    # get permutation importance of the parameter with the build dataset
    (mean_build,
     importances_build,
     means_build,
     stds_build) = get_just_importance(model,
                                       data_build,
                                       target_build,
                                       scoring=scoring,
                                       random_state=lcl_seed + 100)
    # get permutation importance of the parameter with the validation dataset
    (mean_val,
     importances_val,
     means_val,
     stds_val) = get_just_importance(model,
                                     data_validation,
                                     target_validation,
                                     scoring=scoring,
                                     random_state=lcl_seed + 100)
    # Generate the boxplots
    sorted_idx = mean_val.argsort()
    fingerprint = f'\nDownsampling {iteration}'

    boxplot(importances_build[sorted_idx].T,
            data_build.columns[sorted_idx],
            'Build',
            path_graph,
            fingerprint=fingerprint ,
            values_2=importances_val[sorted_idx].T,
            name_2='Validation')

    # Store the scoring values
    values = np.append(np.round(means_val, 5),
                       [iteration,
                        'Validation_mean',
                        np.nan,
                        np.nan,
                        round(build_accuracy, 5),
                        round(validation_accuracy, 5)])
    df.loc[len(df.index)] = values

    values = np.append(np.round(stds_val, 5),
                       [iteration,
                        'Validation_std',
                        np.nan,
                        np.nan,
                        round(build_accuracy, 5),
                        round(validation_accuracy, 5)])
    df.loc[len(df.index)] = values
    # Save the model
    dump(model, path_model)

    return df


def get_importance_training(df,
                            cv_scores,
                            data_train,
                            target_train,
                            iteration,
                            folder,
                            scoring,
                            lcl_seed,
                            save=False):
    """Get permutation importance for each split of cross validation."""
    # Retrieve the importance of the feature for each split with associated
    # score
    all_means = np.empty((0, len(data_train.columns)),
                         float)
    for split, est in enumerate(cv_scores['estimator']):

        # Prepare paths
        fingerprint = f'\nDownsampling {iteration}, Split {split}'
        graph = f'Importance_{iteration}_Training_{split}.png'
        model = f'Model_{iteration}_Training_{split}.joblib'
        path_graph = os.path.join(folder,
                                  'graphs',
                                  graph)
        path_model = os.path.join(folder,
                                  'models',
                                  model)
        # Get permutation importance
        means, stds = get_importance(est,
                                     data_train,
                                     target_train,
                                     path_graph,
                                     scoring=scoring,
                                     fingerprint=fingerprint,
                                     random_state=lcl_seed + 100)
        # Store the scoring values
        values = np.append(np.round(means, 5),
                           [iteration,
                            f'Training_mean_{split}',
                            np.round(cv_scores['train_score'][split], 5),
                            np.round(cv_scores['test_score'][split], 5),
                            np.nan,
                            np.nan])
        df.loc[len(df.index)] = values

        values = np.append(np.round(stds, 5),
                           [iteration,
                            f'Training_std_{split}',
                            np.round(cv_scores['train_score'][split], 5),
                            np.round(cv_scores['test_score'][split], 5),
                            np.nan,
                            np.nan])
        df.loc[len(df.index)] = values
        # Save the model
        if save is True:
            dump(est, path_model)

        # Update the means array
        all_means = np.append(all_means,
                              [means],
                              axis=0)

    # Calculate the mean of each feature
    if save is True:
        mean_of_means = np.mean(all_means,
                                axis=0)
        # Generate the graph
        sorted_idx = mean_of_means.argsort()
        fingerprint = f'\nDownsampling {iteration}, mean of all splits'
        graph = 'Importance_' + str(iteration) + '_All_Training.png'
        path_graph = os.path.join(folder,
                                  'graphs',
                                  graph)
        boxplot(all_means[:,sorted_idx],
                data_train.columns[sorted_idx],
                'All means',
                path_graph,
                fingerprint=fingerprint)
    return df

def get_just_importance(tree_model,
                        data,
                        target,
                        n_repeats=10,
                        random_state=42,
                        scoring='accuracy',
                        n_jobs=1):
    """Get importance of parameters for a tree based model without graph."""
    result = permutation_importance(tree_model,
                                    data,
                                    target,
                                    scoring=scoring,
                                    n_repeats=n_repeats,
                                    random_state=random_state,
                                    n_jobs=n_jobs)

    sorted_idx = result.importances_mean.argsort()

    return (result.importances_mean,
            result.importances,
            result['importances_mean'],
            result['importances_std'])


def get_importance(tree_model,
                   data,
                   target,
                   savepath,
                   n_repeats=10,
                   random_state=42,
                   scoring='accuracy',
                   fingerprint='',
                   n_jobs=1):
    """Get importance of parameters for a tree based model."""
    result = permutation_importance(tree_model,
                                    data,
                                    target,
                                    scoring=scoring,
                                    n_repeats=n_repeats,
                                    random_state=random_state,
                                    n_jobs=n_jobs)

    sorted_idx = result.importances_mean.argsort()

    boxplot(result.importances[sorted_idx].T,
            data.columns[sorted_idx],
            'All means',
            savepath,
            fingerprint=fingerprint)
    return result['importances_mean'], result['importances_std']


def KFold_crossvalidation(model,
                          data_train,
                          target_train,
                          n_splits=10,
                          test_size=None,
                          random_state=0,
                          scoring='accuracy',
                          return_train_score=True,
                          return_estimator=True,
                          n_jobs=1):
    """Perform cross validation with KFold."""
    cv = KFold(n_splits=n_splits)
    cv_scores = cross_validate(model,
                               data_train,
                               target_train,
                               cv=cv,
                               scoring=scoring,
                               return_train_score=True,
                               return_estimator=True,
                               n_jobs=n_jobs)
    return cv_scores


def shufflesplit_crossvalidation(model,
                                 data_train,
                                 target_train,
                                 n_splits=10,
                                 test_size=0.2,
                                 random_state=0,
                                 scoring='accuracy',
                                 return_train_score=True,
                                 return_estimator=True,
                                 n_jobs=1):
    """Perform cross validation with shufflesplit."""
    cv = ShuffleSplit(n_splits=n_splits,
                      test_size=test_size,
                      random_state=random_state)
    cv_scores = cross_validate(model,
                               data_train,
                               target_train,
                               cv=cv,
                               scoring=scoring,
                               return_train_score=True,
                               return_estimator=True,
                               n_jobs=n_jobs)
    return cv_scores


def separate_data_and_target(dataframe,
                             target_column):
    """Give data and target dataframe."""
    data = dataframe.drop([target_column], axis=1)
    target = dataframe[target_column]

    return data, target


def down(dataframe,
         classes,
         dict_indexes,
         sampling_size,
         seed=1):
    """Generate e down-sampled database."""
    np.random.seed(seed)
    database = pd.DataFrame()
    for classe in classes:
        # Take random sample without replacement
        indexes_to_take = np.random.choice(dict_indexes[classe],
                                           size=sampling_size,
                                           replace=False)
        # Store the sub-sample
        database = pd.concat([database,
                              dataframe.iloc[indexes_to_take]])
    return database


def clean_db(dataframe,
             columns_to_exclude,
             dataframe_validation=None):
    """Remove unwanted columns of build and validation dataframes."""
    df_db_clean = clean(dataframe,
                        columns_to_exclude)
    if dataframe_validation is not None:
        df_validation_clean = clean(dataframe_validation,
                                    columns_to_exclude)
        return df_db_clean, df_validation_clean
    else:
        return df_db_clean


def clean(dataframe,
          columns_to_exclude):
    """Remove unwanted columns."""
    print(f"Columns initially present:\n{dataframe.columns}\n")
    if columns_to_exclude is not None:
        df = dataframe.drop(columns_to_exclude,
                            axis=1)
    else:
        df = dataframe
    print(f"Remaining columns:\n{dataframe.columns}\n")
    return df


def detect_imbalance(df_db,
                     target_column,
                     permissivity=10,
                     n_sampling=10):
    """Detect imbalance between classes."""
    # Get all unique classes with their count
    classes_counts = df_db[target_column].value_counts()
    classes = np.array(classes_counts.index)

    # Get min an max representation
    min = classes_counts.min()
    max = classes_counts.max()

    # Generate dataframe for display
    dict_classes = {}
    for i in range(len(classes)):
        dict_classes[classes[i]] = classes_counts[i]
    df_classes = pd.DataFrame(dict_classes,
                              index = ['counts'])
    print(f"Imbalance of the dataset:\n{df_classes}\n")

    # Determine if imbalance has to be handled
    if min < (max * (100 - permissivity) / 100):
        print(f"Imbalance will be handled.\n")
        n_sampling = n_sampling
    else:
        print(f"Imbalance does not need to be handled.\n")
        n_sampling = 1
    print(f"All classes will be set to {min} for {n_sampling}",
          "downsamplings.\n")
    return n_sampling, min, classes


def get_indexes(df_db,
                target_column,
                classes):
    """Generate a dictionnary with all values of classes."""
    dict_indexes = {}
    for classe in classes:
        test = df_db[target_column] == classe
        dict_indexes[classe] = df_db.index[test].tolist()
    return dict_indexes
