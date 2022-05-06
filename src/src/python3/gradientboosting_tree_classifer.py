#! /usr/bin/python3
# coding: utf-8
"""GradientBoosting classification."""
import pandas as pd
import numpy as np
import time
import os
from sklearn.model_selection import train_test_split
from multiprocessing import Pool
from python3.functions import project_time_stamp
from python3.functions import create_machine_learning_folders
from python3.scikitlearn_tools import separate_data_and_target, down, clean_db
from python3.scikitlearn_tools import detect_imbalance, get_indexes
from python3.scikitlearn_pipelines import GBC_pipeline, HistGBC_pipeline
from python3.scikitlearn_tools import shufflesplit_crossvalidation
from python3.scikitlearn_tools import KFold_crossvalidation
from python3.scikitlearn_tools import get_importance_training
from python3.scikitlearn_tools import get_importance_validation


class classifier:
    """Auto threshold method and associated functions."""

    def __init__(self,
                 dataframe,
                 target_column,
                 folder,
                 dataframe_validation=None,
                 columns_to_exclude=None,
                 pipeline=GBC_pipeline,
                 crossvalidation=shufflesplit_crossvalidation,
                 suffix='',
                 permissivity=10,
                 n_sampling=10,
                 n_splits='auto',
                 save_split_models=False,
                 seed=666,
                 processes=4,
                 scoring='accuracy',
                 jobs=1,
                 perform_qc_on_prediction=None,
                 arguments_for_qc=None):
        """Construct method."""
        # Create the dedicated folder and subfolders
        self.pipeline = pipeline
        if self.pipeline == GBC_pipeline:
            self.name = f'GradientBoostClassifier_{suffix}'
        elif self.pipeline == HistGBC_pipeline:
            self.name = f'HistGradientBoostClassifier_{suffix}'
        self.folder = create_machine_learning_folders(folder,
                                                      project_time_stamp(),
                                                      self.name)
        # Set the seed for all potential numpy random actions
        self.seed = seed
        self.jobs = jobs
        self.target_column = target_column
        self.score = scoring
        self.validation_db = dataframe_validation
        self.validation_raw_db = dataframe_validation.copy()
        self.qc = perform_qc_on_prediction
        self.args = arguments_for_qc
        self.cv = crossvalidation
        self.n_splits = n_splits
        self.save_split_models = save_split_models
        # Clean the databases of unwanted columns
        df_db_clean, df_validation_clean = clean_db(dataframe,
                                                    columns_to_exclude,
                                                    self.validation_db)
        # Generate the model
        start = time.perf_counter()
        self._generate_model(df_db_clean,
                             target_column,
                             df_validation = df_validation_clean,
                             permissivity= permissivity,
                             n_sampling=n_sampling,
                             processes=processes,
                             jobs=jobs)
        end = time.perf_counter()
        print(f"Time elapsed: {(end-start) // 60} min")

    def _generate_model(self,
                        df_db,
                        target_column,
                        df_validation=None,
                        permissivity=10,
                        n_sampling=10,
                        processes=4,
                        jobs=4):
        """Perform gradient boosting classifier pipeline"""
        # Perform diagnosis on imbalance
        (n_sampling,
         self.min,
         self.classes) = detect_imbalance(df_db,
                                          target_column,
                                          permissivity=permissivity,
                                          n_sampling=n_sampling)
        # Get dictionnary of indexes list for all classes in target
        self.dict_indexes = get_indexes(df_db,
                                        target_column,
                                        self.classes)
        # Handle imbalance and perform model
        self.current_db = df_db.copy()
        if df_validation is None:
            self.validation_db = None
            print("Validation set was not given and will be generated.")
        else:
            self.validation_db = df_validation.copy()
            print("Validation set was given.")
        # Perform parrallel processes or not
        if processes > 1:
            with Pool(processes) as pool:
                models = list(pool.map(self._make_model,
                                       range(0, n_sampling, 1)))
        else:
            models = list(map(self._make_model,
                              range(0, n_sampling, 1)))
        # Concatenate all downsampling results
        result_df = pd.concat(models,
                              ignore_index=True)
        result_df.to_csv(self.folder +
                         os.sep +
                         self.name +
                         '.csv')

    def _make_model(self,
                    iteration):
        """Make the gradient boosting model for a downsampling"""

        # Set the seed for all potential numpy random actions
        lcl_seed = self.seed + iteration
        # Generate the downsampled database
        database = down(self.current_db,
                        self.classes,
                        self.dict_indexes,
                        self.min,
                        seed=lcl_seed)
        # Generate data and target df for scikit-learn
        data, target = separate_data_and_target(database,
                                                self.target_column)

        # Generate build and when require validation sets
        if self.validation_db is None:
            # Prepare set
            (data_build,
             data_validation,
             target_build,
             target_validation) = train_test_split(data,
                                                   target,
                                                   shuffle=True,
                                                   test_size=0.3,
                                                   random_state=lcl_seed)
        else:
            data_build, target_build = data, target
            (data_validation,
             target_validation) = separate_data_and_target(self.validation_db,
                                                           self.target_column)
        # Generate pipeline
        model = self.pipeline(data,
                              lcl_seed)
        # Perform cross validation when building the model
        if self.n_splits == 'auto' and self.cv == KFold_crossvalidation:
            n_splits = target_build.shape[0]
        elif self.n_splits == 'auto' and self.cv == shufflesplit_crossvalidation:
            n_splits = 10
        else:
            n_splits = self.n_splits
        cv_scores = self.cv(model,
                            data_build,
                            target_build,
                            n_splits=n_splits,
                            test_size=0.2,
                            random_state=lcl_seed,
                            scoring=self.score,
                            return_train_score=True,
                            return_estimator=True,
                            n_jobs=self.jobs)
        # Format the output dataframe
        columns = np.append(data_build.columns, ['Downsampling',
                                                 'Step',
                                                 f'{self.score}_train',
                                                 f'{self.score}_test',
                                                 f'{self.score}_build',
                                                 f'{self.score}_validation',])
        df = pd.DataFrame(columns=columns)
        df2 = df.copy()
        try:
            # Nota Bene: the split and final models models are saved within a slave
            # function of get_importance to force quality control

            # Get features permutation importance for each split
            df_splits = get_importance_training(df.copy(),
                                                cv_scores,
                                                data_build,
                                                target_build,
                                                iteration,
                                                self.folder,
                                                self.score,
                                                lcl_seed,
                                                save=self.save_split_models)
            # Get features permutation importance with the validation set
            df_validation = get_importance_validation(df.copy(),
                                                      model,
                                                      data_build,
                                                      target_build,
                                                      data_validation,
                                                      target_validation,
                                                      iteration,
                                                      self.folder,
                                                      self.score,
                                                      lcl_seed)
            # Generate prediction and save it
            result_prediction_df = self.validation_raw_db.copy()
            result_prediction_df['Prediction'] = model.predict(data_validation)
            result_prediction_df.to_csv(self.folder +
                                        os.sep +
                                        self.name +
                                        f'_Prediction_Downsampling_{iteration}.csv')
            # Perform pst-process quality control.
            if self.qc is not None:
                self.qc(result_prediction_df,
                        self.args,
                        self.folder,
                        iteration)
            # Generate output df
            df = pd.concat([df_splits,
                            df_validation],
                           ignore_index=True)

            return df
        except:
            print(f'fitting failure for iteration {iteration}')
            return df2
