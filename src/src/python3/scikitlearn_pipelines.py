#! /usr/bin/python3
# coding: utf-8
"""Library of functionnal pipelines."""
from sklearn.compose import make_column_selector as selector
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.pipeline import Pipeline
import numpy as np

def separate_for_ordinal_or_onehot(dataframe,
                                   categorical_columns):
    """Identifies where to use OneHotEncoder or OrdinalEncoder."""
    for_one_hot = []
    for_ordinal = []
    for col in categorical_columns:
        uniques = dataframe[col].unique()
        if len(uniques) <= 2:
            for_ordinal = np.append(for_ordinal, col)
        else:
            for_one_hot = np.append(for_one_hot, col)
    return for_one_hot, for_ordinal

def GBC_pipeline(data,
                 seed):
    """Create pipeline for Gradient Boosting Classifier."""
    # Handle categorical columns
    categorical_columns_selector = selector(dtype_include=object)
    categorical_cols = categorical_columns_selector(data)
    categorical_proc1 = OrdinalEncoder(handle_unknown='use_encoded_value',
                                       unknown_value=-1)
    categorical_proc2 = OneHotEncoder(handle_unknown='ignore')
    for_one_hot, for_ordinal = separate_for_ordinal_or_onehot(data,
                                                              categorical_cols)
    preprocessor = ColumnTransformer([('cat_preprocessor1',
                                       categorical_proc1,
                                       for_ordinal),
                                      ('cat_preprocessor2',
                                       categorical_proc2,
                                       for_one_hot)],
                                       remainder='passthrough',
                                       sparse_threshold=0)
    # Pipeline
    model = Pipeline([('preprocessor',
                       preprocessor),
                      ('classifier',
                       GradientBoostingClassifier(random_state=seed,
                                                  n_iter_no_change=5))
                      ])
    return model


def HistGBC_pipeline(data,
                     seed):
    """Create pipeline for Gradient Boosting Classifier."""
    # Handle categorical columns
    categorical_columns_selector = selector(dtype_include=object)
    categorical_columns = categorical_columns_selector(data)
    categorical_proc = OrdinalEncoder(handle_unknown='use_encoded_value',
                                      unknown_value=-1)
    preprocessor = ColumnTransformer([('cat_preprocessor',
                                       categorical_proc,
                                       categorical_columns)],
                                       remainder='passthrough',
                                       sparse_threshold=0)
    # Pipeline
    model = Pipeline([('preprocessor',
                       preprocessor),
                      ('classifier',
                       HistGradientBoostingClassifier(random_state=seed,
                                                      n_iter_no_change=5))
                      ])
    print('Hist')
    return model
