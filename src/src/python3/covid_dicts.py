#! /usr/bin/python3
# coding: utf-8
"""Dictionnaries used for COVID project."""
import pandas as pd

"""
Threshold used for the different cohorts (2022-02-08, mail)
          Cohorte 1 Cohorte 2 Cohorte 3 Cohorte 4 Cohorte 5 Cohorte 6 Pilot 1 Pilot 2
IFN lambda	2,8k      3,1k      2,5k      2,4k      2,5k      1,5k      9,5k    1,9k
CD83        10k       9,9k      11k       5,7k      5,5k      5,3k      2,3k    10k
PDL1         528       1,6k      2,7k      1,8k      1,6k      1,3k      652     2,4k
IFNa	     437       1k        1,2k      1k        936       628       685     718
CD80        1,3k      1k        1k        936	      936       898       254     898

          Cohorte 1 Cohorte 2 Cohorte 3 Cohorte 4 Cohorte 5 Cohorte 6 Pilot 1 Pilot 2
IFN lambda	4200      4100       2600      2100      3100      2100     10000    2600
CD83        9900     10000      11000      5200      5200      5200      2200** 10000
PDL1         574      1200       5200**    1200      1200      1200       388    2200
IFNa	     437       482        579       447       623       447       479     535
IFNahi 	1,9k	1,1k	1k	923	2k	2,6k	1,1k	2,1k
CD80         574       528        623       464	      623       667       256     623

"""

df_treshold_pDCs = pd.DataFrame({
  'IFN-Lambda': [4200,4100, 2600, 2100, 3100, 2100, 10000, 2600],
  'CD83': [9900, 10000, 11000, 5200, 5200, 5200, 2200, 10000],
  'PD-L1': [574, 1200, 5200, 1200, 1200, 388, 652, 2200],
  'IFNa': [437, 482, 579, 447, 623, 447, 479, 535],
  'IFNahi': [1900, 1100, 1000, 933, 2000, 2600, 1100, 2100],
  'CD80': [574, 528, 623, 464, 623, 667, 256, 623]
}, index=['Cohorte 1',
          'Cohorte 2',
          'Cohorte 3',
          'Cohorte 4',
          'Cohorte 5',
          'Cohorte 6',
          'Pilote 1',
          'Pilote 2'])

df_variability = pd.DataFrame({
  'channel': ['IFN-Lambda', 'CD83', 'PD-L1', 'IFNa', 'IFNahi', 'CD80'],
  'mean': df_treshold_pDCs.mean(axis=0).values,
  'std': df_treshold_pDCs.std(axis=0).values
})

# Early <= 15

dict_samples_pDCs = {
  'PD-0041_pDCs_A1': ['mild-early', 'pDCs', 'Mock', 4, 'modeling', 1.17, 'Cohorte 1'],
  'PD-0041_pDCs_A2': ['mild-early', 'pDCs', 'SARS', 4, 'modeling', 1.31, 'Cohorte 1'],
  'PD-0041_pDCs_A3': ['mild-early', 'pDCs', 'Agonist', 4, 'modeling', 1.66, 'Cohorte 1'],
  'PD-0041_pDCs_B1': ['mild-early', 'pDCs', 'Mock', 11, 'modeling', 2.8, 'Cohorte 1'],
  'PD-0041_pDCs_B2': ['mild-early', 'pDCs', 'SARS', 11, 'modeling', 2.72, 'Cohorte 1'],
  'PD-0041_pDCs_B3': ['mild-early', 'pDCs', 'Agonist', 11, 'modeling', 2.25, 'Cohorte 1'],
  'PD-0041_pDCs_C1': ['mild-late', 'pDCs', 'Mock', 18, 'modeling', 3.07, 'Cohorte 1'],
  'PD-0041_pDCs_C2': ['mild-late', 'pDCs', 'SARS', 18, 'modeling', 3.84, 'Cohorte 1'],
  'PD-0041_pDCs_C3': ['mild-late', 'pDCs', 'Agonist', 18, 'modeling', 2.64, 'Cohorte 1'],
  'PD-0041_pDCs_D1': ['mild-late', 'pDCs', 'Mock', 32, 'modeling', 5.73, 'Cohorte 1'],
  'PD-0041_pDCs_D2': ['mild-late', 'pDCs', 'SARS', 32, 'modeling', 5.83, 'Cohorte 1'],
  'PD-0041_pDCs_D3': ['mild-late', 'pDCs', 'Agonist', 32, 'modeling', 3.57, 'Cohorte 1'],

  'GC-0038_pDCs_A1': ['mild-early', 'pDCs', 'Mock', 1, 'modeling', 2.28, 'Cohorte 2'],
  'GC-0038_pDCs_A2': ['mild-early', 'pDCs', 'SARS', 1, 'modeling', 2.96, 'Cohorte 2'],
  'GC-0038_pDCs_A3': ['mild-early', 'pDCs', 'Agonist', 1, 'modeling', 2.29, 'Cohorte 2'],
  'GC-0038_pDCs_B1': ['mild-early', 'pDCs', 'Mock', 8, 'modeling', 3.84, 'Cohorte 2'],
  'GC-0038_pDCs_B2': ['mild-early', 'pDCs', 'SARS', 8, 'modeling', 5.32, 'Cohorte 2'],
  'GC-0038_pDCs_B3': ['mild-early', 'pDCs', 'Agonist', 8, 'modeling', 5.54, 'Cohorte 2'],
  'GC-0038_pDCs_C1': ['mild-early', 'pDCs', 'Mock', 15, 'modeling', 6.34, 'Cohorte 2'],
  'GC-0038_pDCs_C2': ['mild-early', 'pDCs', 'SARS', 15, 'modeling', 8.07, 'Cohorte 2'],
  'GC-0038_pDCs_C3': ['mild-early', 'pDCs', 'Agonist', 15, 'modeling', 4.92, 'Cohorte 2'],
  'GC-0038_pDCs_D1': ['mild-late', 'pDCs', 'Mock', 22, 'modeling', 6.93, 'Cohorte 2'],
  'GC-0038_pDCs_D2': ['mild-late', 'pDCs', 'SARS', 22, 'modeling', 6.54, 'Cohorte 2'],
  'GC-0038_pDCs_D3': ['mild-late', 'pDCs', 'Agonist', 22, 'modeling', 6.98, 'Cohorte 2'],

  'GC-0017_pDCs_A1': ['mild-early', 'pDCs', 'Mock', 4, 'modeling', 3.09, 'Cohorte 3'],
  'GC-0017_pDCs_A2': ['mild-early', 'pDCs', 'SARS', 4, 'modeling', 3.25, 'Cohorte 3'],
  'GC-0017_pDCs_A3': ['mild-early', 'pDCs', 'Agonist', 4, 'modeling', 5.38, 'Cohorte 3'],
  'GC-0017_pDCs_B1': ['mild-early', 'pDCs', 'Mock', 10, 'modeling', 1.66, 'Cohorte 3'],
  'GC-0017_pDCs_B2': ['mild-early', 'pDCs', 'SARS', 10, 'modeling', 2.17, 'Cohorte 3'],
  'GC-0017_pDCs_B3': ['mild-early', 'pDCs', 'Agonist', 10, 'modeling', 1.8, 'Cohorte 3'],
  'GC-0017_pDCs_C1': ['mild-late', 'pDCs', 'Mock', 19, 'modeling', 2.87, 'Cohorte 3'],
  'GC-0017_pDCs_C2': ['mild-late', 'pDCs', 'SARS', 19, 'modeling', 4.16, 'Cohorte 3'],
  'GC-0017_pDCs_C3': ['mild-late', 'pDCs', 'Agonist', 19, 'modeling', 5.28, 'Cohorte 3'],
  #'GC-0017_pDCs_D1': ['mild-late', 'pDCs', 'Mock', 25, 'bad-quality', 1.63, 'Cohorte 3'],
  #'GC-0017_pDCs_D2': ['mild-late', 'pDCs', 'SARS', 25, 'bad-quality', 1.52, 'Cohorte 3'],
  'GC-0017_pDCs_E1': ['mild-late', 'pDCs', 'Mock', 183, 'modeling', 3.86, 'Cohorte 3'],
  'GC-0017_pDCs_E2': ['mild-late', 'pDCs', 'SARS', 183, 'modeling', 4.5, 'Cohorte 3'],
  'GC-0017_pDCs_E3': ['mild-late', 'pDCs', 'Agonist', 183, 'modeling', 4.25, 'Cohorte 3'],

  'AS-0030_pDCs_A1': ['mild-early', 'pDCs', 'Mock', 1, 'modeling', 7.75, 'Cohorte 4'],
  'AS-0030_pDCs_A2': ['mild-early', 'pDCs', 'SARS', 1, 'modeling', 22.2, 'Cohorte 4'],
  'AS-0030_pDCs_A3': ['mild-early', 'pDCs', 'Agonist', 1, 'modeling', 13.1, 'Cohorte 4'],
  'AS-0030_pDCs_B1': ['mild-early', 'pDCs', 'Mock', 8, 'modeling', 5.39, 'Cohorte 4'],
  'AS-0030_pDCs_B2': ['mild-early', 'pDCs', 'SARS', 8, 'modeling', 9.07, 'Cohorte 4'],
  'AS-0030_pDCs_B3': ['mild-early', 'pDCs', 'Agonist', 8, 'modeling', 14.9, 'Cohorte 4'],
  #'AS-0030_pDCs_C1': ['mild-early', 'pDCs', 'Mock', 14, 'bad-quality', 7.69, 'Cohorte 4'],
  'AS-0030_pDCs_C2': ['mild-early', 'pDCs', 'SARS', 14, 'modeling', 14.2, 'Cohorte 4'],
  #'AS-0030_pDCs_C3': ['mild-early', 'pDCs', 'Agonist', 14, 'bad-quality', 11, 'Cohorte 4'],
  'AS-0030_pDCs_D1': ['mild-late', 'pDCs', 'Mock', 22, 'modeling', 11.7, 'Cohorte 4'],
  'AS-0030_pDCs_D2': ['mild-late', 'pDCs', 'SARS', 22, 'modeling', 25.6, 'Cohorte 4'],
  'AS-0030_pDCs_D3': ['mild-late', 'pDCs', 'Agonist', 22, 'modeling', 14.7, 'Cohorte 4'],
  'AS-0030_pDCs_E1': ['mild-late', 'pDCs', 'Mock', 183, 'modeling', 5.7, 'Cohorte 4'],
  'AS-0030_pDCs_E2': ['mild-late', 'pDCs', 'SARS', 183, 'modeling', 8.42, 'Cohorte 4'],
  'AS-0030_pDCs_E3': ['mild-late', 'pDCs', 'Agonist', 183, 'modeling', 8.95, 'Cohorte 4'],

  'LD-0175_pDCs_A1': ['mild-early', 'pDCs', 'Mock', 1, 'modeling', 1.01, 'Cohorte 5'],
  'LD-0175_pDCs_A2': ['mild-early', 'pDCs', 'SARS', 1, 'modeling', 0.74, 'Cohorte 5'],
  'LD-0175_pDCs_A3': ['mild-early', 'pDCs', 'Agonist', 1, 'modeling', 1.9, 'Cohorte 5'],
  'LD-0175_pDCs_B1': ['mild-early', 'pDCs', 'Mock', 8, 'modeling', 7.4, 'Cohorte 5'],
  'LD-0175_pDCs_B2': ['mild-early', 'pDCs', 'SARS', 8, 'modeling', 10.9, 'Cohorte 5'],
  'LD-0175_pDCs_B3': ['mild-early', 'pDCs', 'Agonist', 8, 'modeling', 7.73, 'Cohorte 5'],
  'LD-0175_pDCs_C1': ['mild-early', 'pDCs', 'Mock', 13, 'modeling', 5.26, 'Cohorte 5'],
  'LD-0175_pDCs_C2': ['mild-early', 'pDCs', 'SARS', 13, 'modeling', 7.57, 'Cohorte 5'],
  'LD-0175_pDCs_C3': ['mild-early', 'pDCs', 'Agonist', 13, 'modeling', 5.46, 'Cohorte 5'],
  'LD-0175_pDCs_D1': ['mild-late', 'pDCs', 'Mock', 20, 'modeling', 1.94, 'Cohorte 5'],
  'LD-0175_pDCs_D2': ['mild-late', 'pDCs', 'SARS', 20, 'modeling', 2.01, 'Cohorte 5'],
  'LD-0175_pDCs_D3': ['mild-late', 'pDCs', 'Agonist', 20, 'modeling', 3.48, 'Cohorte 5'],
  #'LD-0175_pDCs_E1': ['mild-late', 'pDCs', 'Mock', 183, 'bad-quality', 0.97, 'Cohorte 5'],
  #'LD-0175_pDCs_E2': ['mild-late', 'pDCs', 'SARS', 183, 'bad-quality', 1.23, 'Cohorte 5'],
  #'LD-0175_pDCs_E3': ['mild-late', 'pDCs', 'Agonist', 183, 'bad-quality', 1.14, 'Cohorte 5'],

  'PS-0029_pDCs_A1': ['mild-early', 'pDCs', 'Mock', 2, 'modeling', 1.97, 'Cohorte 6'],
  'PS-0029_pDCs_A2': ['mild-early', 'pDCs', 'SARS', 2, 'modeling', 2.9, 'Cohorte 6'],
  'PS-0029_pDCs_A3': ['mild-early', 'pDCs', 'Agonist', 2, 'modeling', 5.74, 'Cohorte 6'],
  #'PS-0029_pDCs_B1': ['mild-early', 'pDCs', 'Mock', 9, 'bad-quality', 0.61, 'Cohorte 6'],
  #'PS-0029_pDCs_B2': ['mild-early', 'pDCs', 'SARS', 9, 'bad-quality', 0.79, 'Cohorte 6'],
  #'PS-0029_pDCs_B3': ['mild-early', 'pDCs', 'Agonist', 9, 'bad-quality', 0.64, 'Cohorte 6'],
  'PS-0029_pDCs_C1': ['mild-late', 'pDCs', 'Mock', 16, 'modeling', 2.2, 'Cohorte 6'],
  'PS-0029_pDCs_C2': ['mild-late', 'pDCs', 'SARS', 16, 'modeling', 3.03, 'Cohorte 6'],
  'PS-0029_pDCs_C3': ['mild-late', 'pDCs', 'Agonist', 16, 'modeling', 3.72, 'Cohorte 6'],
  #'PS-0029_pDCs_D1': ['mild-late', 'pDCs', 'Mock', 23, 'bad-quality', 0.31, 'Cohorte 6'],
  #'PS-0029_pDCs_D2': ['mild-late', 'pDCs', 'SARS', 23, 'bad-quality', 0.32, 'Cohorte 6'],
  'PS-0029_pDCs_E1': ['mild-late', 'pDCs', 'Mock', 30, 'modeling', 3.4, 'Cohorte 6'],
  'PS-0029_pDCs_E2': ['mild-late', 'pDCs', 'SARS', 30, 'modeling', 4.31, 'Cohorte 6'],
  'PS-0029_pDCs_E3': ['mild-late', 'pDCs', 'Agonist', 30, 'modeling', 5.59, 'Cohorte 6'],
  'PS-0029_pDCs_F1': ['mild-late', 'pDCs', 'Mock', 183, 'modeling', 3.91, 'Cohorte 6'],
  'PS-0029_pDCs_F2': ['mild-late', 'pDCs', 'SARS', 183, 'modeling', 4.61, 'Cohorte 6'],
  'PS-0029_pDCs_F3': ['mild-late', 'pDCs', 'Agonist', 183, 'modeling', 4.24, 'Cohorte 6'],

  #'CHA_Mah_pDCs_E1': ['severe', 'pDCs', 'Mock', 27, 'bad-quality', 0.68, 'Cohorte 1'],
  #'CHA_Mah_pDCs_E2': ['severe', 'pDCs', 'SARS', 27, 'bad-quality', 0.93, 'Cohorte 1'],
  #'CHA_Mah_pDCs_E3': ['severe', 'pDCs', 'Agonist', 27, 'bad-quality', 1.33, 'Cohorte 1'],
  'CHA_Mah_pDCs_F1': ['severe', 'pDCs', 'Mock', 37, 'modeling', 2.78, 'Cohorte 1'],
  'CHA_Mah_pDCs_F2': ['severe', 'pDCs', 'SARS', 37, 'modeling', 4.32, 'Cohorte 1'],
  'CHA_Mah_pDCs_F3': ['severe', 'pDCs', 'Agonist', 37, 'modeling', 2.99, 'Cohorte 1'],

  #'BRU_Chr_pDCs_E1': ['severe', 'pDCs', 'Mock', 9, 'bad-quality', 0.59, 'Cohorte 2'],
  #'BRU_Chr_pDCs_E2': ['severe', 'pDCs', 'SARS', 9, 'bad-quality', 0.61, 'Cohorte 2'],
  #'BRU_Chr_pDCs_E3': ['severe', 'pDCs', 'Agonist', 9, 'bad-quality', 0.5, 'Cohorte 2'],
  'BRU_Chr_pDCs_F1': ['severe', 'pDCs', 'Mock', 11, 'modeling', 1.62, 'Cohorte 2'],
  'BRU_Chr_pDCs_F2': ['severe', 'pDCs', 'SARS', 11, 'modeling', 1.26, 'Cohorte 2'],
  'BRU_Chr_pDCs_F3': ['severe', 'pDCs', 'Agonist', 11, 'modeling', 0.88, 'Cohorte 2'],
  #'BRU_Chr_pDCs_G1': ['severe', 'pDCs', 'Mock', 15, 'bad-quality', 0.19, 'Cohorte 2'],
  #'BRU_Chr_pDCs_G2': ['severe', 'pDCs', 'SARS', 15, 'bad-quality', 0.19, 'Cohorte 2'],
  #'BRU_Chr_pDCs_G3': ['severe', 'pDCs', 'Agonist', 15, 'bad-quality', 0.55, 'Cohorte 2'],

  'HOU_ED_pDCs_F1': ['severe', 'pDCs', 'Mock', 15, 'modeling', 1.6, 'Cohorte 3'],
  'HOU_ED_pDCs_F2': ['severe', 'pDCs', 'SARS', 15, 'modeling', 1.52, 'Cohorte 3'],
  'HOU_ED_pDCs_F3': ['severe', 'pDCs', 'Agonist', 15, 'modeling', 2.87, 'Cohorte 3'],
  'HOU_ED_pDCs_G1': ['severe', 'pDCs', 'Mock', 18, 'modeling', 1.47, 'Cohorte 3'],
  'HOU_ED_pDCs_G2': ['severe', 'pDCs', 'SARS', 18, 'modeling', 1.29, 'Cohorte 3'],
  'HOU_ED_pDCs_G3': ['severe', 'pDCs', 'Agonist', 18, 'modeling', 2.01, 'Cohorte 3'],
  'HOU_ED_pDCs_H1': ['severe', 'pDCs', 'Mock', 20, 'modeling', 1.52, 'Cohorte 3'],
  'HOU_ED_pDCs_H2': ['severe', 'pDCs', 'SARS', 20, 'modeling', 0.78, 'Cohorte 3'],
  'HOU_ED_pDCs_H3': ['severe', 'pDCs', 'Agonist', 20, 'modeling', 0.98, 'Cohorte 3'],

  #'FAY_Rob_pDCs_F1': ['severe', 'pDCs', 'Mock', 12, 'bad-quality', 1.6, 'Cohorte 4'],
  #'FAY_Rob_pDCs_F2': ['severe', 'pDCs', 'SARS', 12, 'bad-quality', 1.09, 'Cohorte 4'],
  #'FAY_Rob_pDCs_G1': ['severe', 'pDCs', 'Mock', 28, 'bad-quality', 1.85, 'Cohorte 4'],
  #'FAY_Rob_pDCs_G2': ['severe', 'pDCs', 'SARS', 28, 'bad-quality', 3.54, 'Cohorte 4'],
  #'FAY_Rob_pDCs_H1': ['severe', 'pDCs', 'Mock', 35, 'bad-quality', 0.17, 'Cohorte 4'],
  #'FAY_Rob_pDCs_H2': ['severe', 'pDCs', 'SARS', 35, 'bad-quality', 0.73, 'Cohorte 4'],

  #'OZBE_pDCs_G1': ['severe', 'pDCs', 'Mock', 16, 'bad-quality', 0.59, 'Cohorte 5'],
  #'OZBE_pDCs_G2': ['severe', 'pDCs', 'SARS', 16, 'bad-quality', 0.57, 'Cohorte 5'],
  'OZBE_pDCs_I1': ['severe', 'pDCs', 'Mock', 30, 'modeling', 1.14, 'Cohorte 5'],
  'OZBE_pDCs_I2': ['severe', 'pDCs', 'SARS', 30, 'modeling', 1.15, 'Cohorte 5'],

  #'RESU_pDCs_G1': ['severe', 'pDCs', 'Mock', 36, 'bad-quality', 0.59, 'Cohorte 6'],
  #'RESU_pDCs_G2': ['severe', 'pDCs', 'SARS', 36, 'bad-quality', 0.32, 'Cohorte 6'],
  'RESU_pDCs_H1': ['severe', 'pDCs', 'Mock', 43, 'modeling', 1.23, 'Cohorte 6'],
  'RESU_pDCs_H2': ['severe', 'pDCs', 'SARS', 43, 'modeling', 0.96, 'Cohorte 6'],
  'RESU_pDCs_I1': ['severe', 'pDCs', 'Mock', 50, 'modeling', 0.70, 'Cohorte 6'],
  'RESU_pDCs_I2': ['severe', 'pDCs', 'SARS', 50, 'modeling', 0.99, 'Cohorte 6'],

  'Hu3_1_pDCs_G1': ['healthy', 'pDCs', 'Mock', 1, 'modeling', 13.5, 'Cohorte 1'],
  'Hu3_1_pDCs_G2': ['healthy', 'pDCs', 'SARS', 1, 'modeling', 13.8, 'Cohorte 1'],
  'Hu3_1_pDCs_G3': ['healthy', 'pDCs', 'Agonist', 1, 'modeling', 10.9, 'Cohorte 1'],

  'Hu3_2_pDCs_H1': ['healthy', 'pDCs', 'Mock', 11, 'modeling', 15.7, 'Cohorte 2'],
  'Hu3_2_pDCs_H2': ['healthy', 'pDCs', 'SARS', 11, 'modeling', 23.3, 'Cohorte 2'],
  'Hu3_2_pDCs_H3': ['healthy', 'pDCs', 'Agonist', 11, 'modeling', 16.5, 'Cohorte 2'],

  'Hu3_3_pDCs_I1': ['healthy', 'pDCs', 'Mock', 25, 'modeling', 0.99, 'Cohorte 3'],
  'Hu3_3_pDCs_I2': ['healthy', 'pDCs', 'SARS', 25, 'modeling', 1.36, 'Cohorte 3'],
  'Hu3_3_pDCs_I3': ['healthy', 'pDCs', 'Agonist', 25, 'modeling', 2.78, 'Cohorte 3'],

  'Hu3_4_pDCs_I1': ['healthy', 'pDCs', 'Mock', 35, 'modeling', 3.92, 'Cohorte 4'],
  'Hu3_4_pDCs_I2': ['healthy', 'pDCs', 'SARS', 35, 'modeling', 13, 'Cohorte 4'],
  'Hu3_4_pDCs_I3': ['healthy', 'pDCs', 'Agonist', 35, 'modeling', 13.6, 'Cohorte 4'],

  'Hu3_5_pDCs_J1': ['healthy', 'pDCs', 'Mock', 50, 'modeling', 7.88, 'Cohorte 5'],
  'Hu3_5_pDCs_J2': ['healthy', 'pDCs', 'SARS', 50, 'modeling', 13.6, 'Cohorte 5'],
  'Hu3_5_pDCs_J3': ['healthy', 'pDCs', 'Agonist', 50, 'modeling', 10, 'Cohorte 5'],

  #'Hu3_6_pDCs_J1': ['healthy', 'pDCs', 'Mock', 8, 'bad-quality', 1.66, 'Cohorte 6'],
  #'Hu3_6_pDCs_J2': ['healthy', 'pDCs', 'SARS', 8, 'bad-quality', 1.78, 'Cohorte 6'],

  'HD_6M20_pDCs_H1': ['healthy', 'pDCs', 'Mock', 183, 'modeling', 11.4, 'Cohorte 1'],
  'HD_6M20_pDCs_H2': ['healthy', 'pDCs', 'SARS', 183, 'modeling', 13.8, 'Cohorte 1'],
  'HD_6M20_pDCs_H3': ['healthy', 'pDCs', 'Agonist', 183, 'modeling', 13.6, 'Cohorte 1'],

  'BC_HV2_pDCs_I1': ['healthy', 'pDCs', 'Mock', 14, 'modeling', 3.4, 'Cohorte 2'],
  'BC_HV2_pDCs_I2': ['healthy', 'pDCs', 'SARS', 14, 'modeling', 5.84, 'Cohorte 2'],
  'BC_HV2_pDCs_I3': ['healthy', 'pDCs', 'Agonist', 14, 'modeling', 4.66, 'Cohorte 2'],

  'BV_HV1_pDCs_J1': ['healthy', 'pDCs', 'Mock', 27, 'modeling', 9.24, 'Cohorte 3'],
  'BV_HV1_pDCs_J2': ['healthy', 'pDCs', 'SARS', 27, 'modeling', 10.4, 'Cohorte 3'],
  'BV_HV1_pDCs_J3': ['healthy', 'pDCs', 'Agonist', 27, 'modeling', 10.7, 'Cohorte 3'],

  'HV_29_pDCs_J1': ['healthy', 'pDCs', 'Mock', 37, 'modeling', 9.05, 'Cohorte 4'],
  'HV_29_pDCs_J2': ['healthy', 'pDCs', 'SARS', 37, 'modeling', 9.66, 'Cohorte 4'],
  'HV_29_pDCs_J3': ['healthy', 'pDCs', 'Agonist', 37, 'modeling', 10.6, 'Cohorte 4'],

  'HD_3M31_pDCs_K1': ['healthy', 'pDCs', 'Mock', 15, 'modeling', 6.23, 'Cohorte 5'],
  'HD_3M31_pDCs_K2': ['healthy', 'pDCs', 'SARS', 15, 'modeling', 9.78, 'Cohorte 5'],
  'HD_3M31_pDCs_K3': ['healthy', 'pDCs', 'Agonist', 15, 'modeling', 5.66, 'Cohorte 5'],

  'HD_EF9S_pDCs_K1': ['healthy', 'pDCs', 'Mock', 22, 'modeling', 4.25, 'Cohorte 6'],
  'HD_EF9S_pDCs_K2': ['healthy', 'pDCs', 'SARS', 22, 'modeling', 6.43, 'Cohorte 6'],
  #'HD_EF9S_pDCs_K3': ['healthy', 'pDCs', 'Agonist', 22, 'modeling', 4.15, 'Cohorte 6'],

  'HV_F23_pDCs_L1': ['healthy', 'pDCs', 'Mock', 30, 'modeling', 5.41, 'Cohorte 6'],
  'HV_F23_pDCs_L2': ['healthy', 'pDCs', 'SARS', 30, 'modeling', 4.25, 'Cohorte 6'],

  'EFS_P1_0901_pDCs_3': ['healthy', 'pDCs', 'Mock', 43, 'modeling', 8.14, 'Pilote 1'],
  'EFS_P1_0901_pDCs_4': ['healthy', 'pDCs', 'SARS', 43, 'modeling', 9.61, 'Pilote 1'],
  'EFS_P1_0901_pDCs_5': ['healthy', 'pDCs', 'Agonist', 43, 'modeling', 8.73, 'Pilote 1'],

  #'EFS_P2_0901_pDCs_3': ['healthy', 'pDCs', 'Mock', 19, 'bad-quality', 3.19, 'Pilote 2'],
  'EFS_P2_0901_pDCs_4': ['healthy', 'pDCs', 'SARS', 19, 'modeling', 9.03, 'Pilote 2'],
  #'EFS_P2_0901_pDCs_7': ['healthy', 'pDCs', 'Agonist', 19, 'modeling', 0, 'Pilote 2'],

  'EFS_P1_0930_pDCs_6': ['healthy', 'pDCs', 'Mock', 32, 'modeling', 16.2, 'Pilote 1'],
  'EFS_P1_0930_pDCs_7': ['healthy', 'pDCs', 'SARS', 32, 'modeling', 15.8, 'Pilote 1'],
  'EFS_P1_0930_pDCs_8': ['healthy', 'pDCs', 'Agonist', 32, 'modeling', 7.65, 'Pilote 1'],

  'EFS_P2_1112_pDCs_8': ['healthy', 'pDCs', 'Mock', 4, 'modeling', 25.7, 'Pilote 2'],
  'EFS_P2_1112_pDCs_9': ['healthy', 'pDCs', 'SARS', 4, 'modeling', 28, 'Pilote 2'],
 # 'EFS_P2_1112_pDCs_12': ['healthy', 'pDCs', 'Agonist', 4, 'modeling', 0, 'Pilote 2']
}



################################################################################
# MDC1
################################################################################
"""
	       Cohorte 1	Cohorte 2	Cohorte 3	Cohorte 4	Cohorte 5	Cohorte 6	Pilot 1	Pilot 2
IFN lambda	5,7K	    2,8k	   2,7k	           2k	        3,7k	2,2k	      9,3k	2,2k
CD83	      11k	     10k	    11k	            5,3k	   5,3k	     5,3k	     2,2k	11k
PDL1	      574	     1,2k	   2,2k	            1,2k	  1,2k	       940	       455	2,2k
IFNa	       848	    482	        665	            665	        711	        665	        479	620
CD80	       574	    1,2k	   711	            1,2k	   665	        711	        191	711
"""

df_treshold_mDC1s = pd.DataFrame({
  'IFN-Lambda': [5700, 2800, 2700, 2000, 3700, 2200, 9300, 2200],
  'CD83': [11000, 10000, 11000, 5300, 5300, 5300, 2200, 11000],
  'PD-L1': [574, 1200, 2200, 1200, 1200, 940, 455, 2200],
  'IFNa': [848, 482, 665, 665, 711, 665, 479, 620],
  'IFNahi':	[803, 803, 803,	1200, 665, 1200, 315, 482],
  'CD80': [574, 1200, 711, 1200, 665, 711, 191, 711]
}, index=['Cohorte 1',
          'Cohorte 2',
          'Cohorte 3',
          'Cohorte 4',
          'Cohorte 5',
          'Cohorte 6',
          'Pilote 1',
          'Pilote 2'])

dict_samples_mDC1s = {
  'PD-0041_mDC1s_A1': ['mild-early', 'mDC1s', 'Mock', 4, 'modeling', 0.98, 'Cohorte 1'],
  'PD-0041_mDC1s_A2': ['mild-early', 'mDC1s', 'SARS', 4, 'modeling', 0.86, 'Cohorte 1'],
  'PD-0041_mDC1s_A3': ['mild-early', 'mDC1s', 'Agonist', 4, 'modeling', 0.59, 'Cohorte 1'],
  'PD-0041_mDC1s_B1': ['mild-early', 'mDC1s', 'Mock', 11, 'modeling', 2.28, 'Cohorte 1'],
  'PD-0041_mDC1s_B2': ['mild-early', 'mDC1s', 'SARS', 11, 'modeling', 2.28, 'Cohorte 1'],
  'PD-0041_mDC1s_B3': ['mild-early', 'mDC1s', 'Agonist', 11, 'modeling', 1.66, 'Cohorte 1'],
  'PD-0041_mDC1s_C1': ['mild-late', 'mDC1s', 'Mock', 18, 'modeling', 5.84, 'Cohorte 1'],
  'PD-0041_mDC1s_C2': ['mild-late', 'mDC1s', 'SARS', 18, 'modeling', 6.67, 'Cohorte 1'],
  'PD-0041_mDC1s_C3': ['mild-late', 'mDC1s', 'Agonist', 18, 'modeling', 3.27, 'Cohorte 1'],
  'PD-0041_mDC1s_D1': ['mild-late', 'mDC1s', 'Mock', 32, 'modeling', 7.47, 'Cohorte 1'],
  'PD-0041_mDC1s_D2': ['mild-late', 'mDC1s', 'SARS', 32, 'modeling', 7.43, 'Cohorte 1'],
  'PD-0041_mDC1s_D3': ['mild-late', 'mDC1s', 'Agonist', 32, 'modeling', 5.31, 'Cohorte 1'],

  'GC-0038_mDC1s_A1': ['mild-early', 'mDC1s', 'Mock', 1, 'modeling', 2.31, 'Cohorte 2'],
  'GC-0038_mDC1s_A2': ['mild-early', 'mDC1s', 'SARS', 1, 'modeling', 2.0, 'Cohorte 2'],
  'GC-0038_mDC1s_A3': ['mild-early', 'mDC1s', 'Agonist', 1, 'modeling', 1.71, 'Cohorte 2'],
  'GC-0038_mDC1s_B1': ['mild-early', 'mDC1s', 'Mock', 8, 'modeling', 6.72, 'Cohorte 2'],
  'GC-0038_mDC1s_B2': ['mild-early', 'mDC1s', 'SARS', 8, 'modeling', 5.23, 'Cohorte 2'],
  'GC-0038_mDC1s_B3': ['mild-early', 'mDC1s', 'Agonist', 8, 'modeling', 6.18, 'Cohorte 2'],
  'GC-0038_mDC1s_C1': ['mild-early', 'mDC1s', 'Mock', 15, 'modeling', 9.21, 'Cohorte 2'],
  'GC-0038_mDC1s_C2': ['mild-early', 'mDC1s', 'SARS', 15, 'modeling', 7.95, 'Cohorte 2'],
  'GC-0038_mDC1s_C3': ['mild-early', 'mDC1s', 'Agonist', 15, 'modeling', 5.77, 'Cohorte 2'],
  'GC-0038_mDC1s_D1': ['mild-late', 'mDC1s', 'Mock', 22, 'modeling', 8.5, 'Cohorte 2'],
  'GC-0038_mDC1s_D2': ['mild-late', 'mDC1s', 'SARS', 22, 'modeling', 5.58, 'Cohorte 2'],
  'GC-0038_mDC1s_D3': ['mild-late', 'mDC1s', 'Agonist', 22, 'modeling', 8.92, 'Cohorte 2'],

  'GC-0017_mDC1s_A1': ['mild-early', 'mDC1s', 'Mock', 4, 'modeling', 7.84, 'Cohorte 3'],
  'GC-0017_mDC1s_A2': ['mild-early', 'mDC1s', 'SARS', 4, 'modeling', 7.59, 'Cohorte 3'],
  'GC-0017_mDC1s_A3': ['mild-early', 'mDC1s', 'Agonist', 4, 'modeling', 1.53, 'Cohorte 3'],
  'GC-0017_mDC1s_B1': ['mild-early', 'mDC1s', 'Mock', 10, 'modeling', 8.93, 'Cohorte 3'],
  'GC-0017_mDC1s_B2': ['mild-early', 'mDC1s', 'SARS', 10, 'modeling', 8.41, 'Cohorte 3'],
  'GC-0017_mDC1s_B3': ['mild-early', 'mDC1s', 'Agonist', 10, 'modeling', 2.73, 'Cohorte 3'],
  'GC-0017_mDC1s_C1': ['mild-late', 'mDC1s', 'Mock', 19, 'modeling', 13.7, 'Cohorte 3'],
  'GC-0017_mDC1s_C2': ['mild-late', 'mDC1s', 'SARS', 19, 'modeling', 8.52, 'Cohorte 3'],
  'GC-0017_mDC1s_C3': ['mild-late', 'mDC1s', 'Agonist', 19, 'modeling', 3.87, 'Cohorte 3'],
  #'GC-0017_mDC1s_D1': ['mild-late', 'mDC1s', 'Mock', 25, 'bad-quality', 1.63, 'Cohorte 3'],
  #'GC-0017_mDC1s_D2': ['mild-late', 'mDC1s', 'SARS', 25, 'bad-quality', 1.52, 'Cohorte 3'],
  'GC-0017_mDC1s_E1': ['mild-late', 'mDC1s', 'Mock', 183, 'modeling', 11.2, 'Cohorte 3'],
  'GC-0017_mDC1s_E2': ['mild-late', 'mDC1s', 'SARS', 183, 'modeling', 9.75, 'Cohorte 3'],
  'GC-0017_mDC1s_E3': ['mild-late', 'mDC1s', 'Agonist', 183, 'modeling', 3.66, 'Cohorte 3'],

  'AS-0030_mDC1s_A1': ['mild-early', 'mDC1s', 'Mock', 1, 'modeling', 6.19, 'Cohorte 4'],
  'AS-0030_mDC1s_A2': ['mild-early', 'mDC1s', 'SARS', 1, 'modeling', 9.46, 'Cohorte 4'],
  'AS-0030_mDC1s_A3': ['mild-early', 'mDC1s', 'Agonist', 1, 'modeling', 9.92, 'Cohorte 4'],
  'AS-0030_mDC1s_B1': ['mild-early', 'mDC1s', 'Mock', 8, 'modeling', 11.5, 'Cohorte 4'],
  'AS-0030_mDC1s_B2': ['mild-early', 'mDC1s', 'SARS', 8, 'modeling', 13.0, 'Cohorte 4'],
  'AS-0030_mDC1s_B3': ['mild-early', 'mDC1s', 'Agonist', 8, 'modeling', 10.3, 'Cohorte 4'],
  #'AS-0030_mDC1s_C1': ['mild-early', 'mDC1s', 'Mock', 14, 'modeling', 18, 'Cohorte 4'],
  'AS-0030_mDC1s_C2': ['mild-early', 'mDC1s', 'SARS', 14, 'modeling', 16.5, 'Cohorte 4'],
  #'AS-0030_mDC1s_C3': ['mild-early', 'mDC1s', 'Agonist', 14, 'bad-quality', 11, 'Cohorte 4'],
  'AS-0030_mDC1s_D1': ['mild-late', 'mDC1s', 'Mock', 22, 'modeling', 17.9, 'Cohorte 4'],
  'AS-0030_mDC1s_D2': ['mild-late', 'mDC1s', 'SARS', 22, 'modeling', 15.7, 'Cohorte 4'],
  'AS-0030_mDC1s_D3': ['mild-late', 'mDC1s', 'Agonist', 22, 'modeling', 10.5, 'Cohorte 4'],
  'AS-0030_mDC1s_E1': ['mild-late', 'mDC1s', 'Mock', 183, 'modeling', 14.5, 'Cohorte 4'],
  'AS-0030_mDC1s_E2': ['mild-late', 'mDC1s', 'SARS', 183, 'modeling', 17.1, 'Cohorte 4'],
  'AS-0030_mDC1s_E3': ['mild-late', 'mDC1s', 'Agonist', 183, 'modeling', 9.87, 'Cohorte 4'],

  'LD-0175_mDC1s_A1': ['mild-early', 'mDC1s', 'Mock', 1, 'modeling', 2.0, 'Cohorte 5'],
  'LD-0175_mDC1s_A2': ['mild-early', 'mDC1s', 'SARS', 1, 'modeling', 1.75, 'Cohorte 5'],
  'LD-0175_mDC1s_A3': ['mild-early', 'mDC1s', 'Agonist', 1, 'modeling', 2.88, 'Cohorte 5'],
  'LD-0175_mDC1s_B1': ['mild-early', 'mDC1s', 'Mock', 8, 'modeling', 23.1, 'Cohorte 5'],
  'LD-0175_mDC1s_B2': ['mild-early', 'mDC1s', 'SARS', 8, 'modeling', 25.7, 'Cohorte 5'],
  'LD-0175_mDC1s_B3': ['mild-early', 'mDC1s', 'Agonist', 8, 'modeling', 7.15, 'Cohorte 5'],
  'LD-0175_mDC1s_C1': ['mild-early', 'mDC1s', 'Mock', 13, 'modeling', 16.2, 'Cohorte 5'],
  'LD-0175_mDC1s_C2': ['mild-early', 'mDC1s', 'SARS', 13, 'modeling', 21.4, 'Cohorte 5'],
  'LD-0175_mDC1s_C3': ['mild-early', 'mDC1s', 'Agonist', 13, 'modeling', 6.76, 'Cohorte 5'],
  'LD-0175_mDC1s_D1': ['mild-late', 'mDC1s', 'Mock', 20, 'modeling', 10.1, 'Cohorte 5'],
  'LD-0175_mDC1s_D2': ['mild-late', 'mDC1s', 'SARS', 20, 'modeling', 11.8, 'Cohorte 5'],
  'LD-0175_mDC1s_D3': ['mild-late', 'mDC1s', 'Agonist', 20, 'modeling', 3.35, 'Cohorte 5'],
  #'LD-0175_mDC1s_E1': ['mild-late', 'mDC1s', 'Mock', 183, 'bad-quality', 0.97, 'Cohorte 5'],
  #'LD-0175_mDC1s_E2': ['mild-late', 'mDC1s', 'SARS', 183, 'bad-quality', 1.23, 'Cohorte 5'],
  #'LD-0175_mDC1s_E3': ['mild-late', 'mDC1s', 'Agonist', 183, 'bad-quality', 1.14, 'Cohorte 5'],

  'PS-0029_mDC1s_A1': ['mild-early', 'mDC1s', 'Mock', 2, 'modeling', 6.67, 'Cohorte 6'],
  'PS-0029_mDC1s_A2': ['mild-early', 'mDC1s', 'SARS', 2, 'modeling', 6.98, 'Cohorte 6'],
  'PS-0029_mDC1s_A3': ['mild-early', 'mDC1s', 'Agonist', 2, 'modeling', 12.5, 'Cohorte 6'],
  #'PS-0029_mDC1s_B1': ['mild-early', 'mDC1s', 'Mock', 9, 'modeling', 3.35, 'Cohorte 6'],
  #'PS-0029_mDC1s_B2': ['mild-early', 'mDC1s', 'SARS', 9, 'modeling', 2.67, 'Cohorte 6'],
  #'PS-0029_mDC1s_B3': ['mild-early', 'mDC1s', 'Agonist', 9, 'bad-quality', 0.64, 'Cohorte 6'],
  'PS-0029_mDC1s_C1': ['mild-late', 'mDC1s', 'Mock', 16, 'modeling', 11.9, 'Cohorte 6'],
  'PS-0029_mDC1s_C2': ['mild-late', 'mDC1s', 'SARS', 16, 'modeling', 13.6, 'Cohorte 6'],
  'PS-0029_mDC1s_C3': ['mild-late', 'mDC1s', 'Agonist', 16, 'modeling', 11.6, 'Cohorte 6'],
  #'PS-0029_mDC1s_D1': ['mild-late', 'mDC1s', 'Mock', 23, 'bad-quality', 0.31, 'Cohorte 6'],
  #'PS-0029_mDC1s_D2': ['mild-late', 'mDC1s', 'SARS', 23, 'bad-quality', 0.32, 'Cohorte 6'],
  'PS-0029_mDC1s_E1': ['mild-late', 'mDC1s', 'Mock', 30, 'modeling', 13.0, 'Cohorte 6'],
  'PS-0029_mDC1s_E2': ['mild-late', 'mDC1s', 'SARS', 30, 'modeling', 14.1, 'Cohorte 6'],
  'PS-0029_mDC1s_E3': ['mild-late', 'mDC1s', 'Agonist', 30, 'modeling', 15.0, 'Cohorte 6'],
  'PS-0029_mDC1s_F1': ['mild-late', 'mDC1s', 'Mock', 183, 'modeling', 14.3, 'Cohorte 6'],
  'PS-0029_mDC1s_F2': ['mild-late', 'mDC1s', 'SARS', 183, 'modeling', 14.4, 'Cohorte 6'],
  'PS-0029_mDC1s_F3': ['mild-late', 'mDC1s', 'Agonist', 183, 'modeling', 13.5, 'Cohorte 6'],

  #'CHA_Mah_mDC1s_E1': ['severe', 'mDC1s', 'Mock', 27, 'modeling', 2.02, 'Cohorte 1'],
  #'CHA_Mah_mDC1s_E2': ['severe', 'mDC1s', 'SARS', 27, 'modeling', 2.02, 'Cohorte 1'],
  #'CHA_Mah_mDC1s_E3': ['severe', 'mDC1s', 'Agonist', 27, 'modeling', 6.53, 'Cohorte 1'],
  'CHA_Mah_mDC1s_F1': ['severe', 'mDC1s', 'Mock', 37, 'modeling', 2.81, 'Cohorte 1'],
  'CHA_Mah_mDC1s_F2': ['severe', 'mDC1s', 'SARS', 37, 'modeling', 3.89, 'Cohorte 1'],
  'CHA_Mah_mDC1s_F3': ['severe', 'mDC1s', 'Agonist', 37, 'modeling', 4.18, 'Cohorte 1'],

  #'BRU_Chr_mDC1s_E1': ['severe', 'mDC1s', 'Mock', 9, 'modeling', 2.87, 'Cohorte 2'],
  #'BRU_Chr_mDC1s_E2': ['severe', 'mDC1s', 'SARS', 9, 'modeling', 2.4, 'Cohorte 2'],
  #'BRU_Chr_mDC1s_E3': ['severe', 'mDC1s', 'Agonist', 9, 'modeling', 3.54, 'Cohorte 2'],
  'BRU_Chr_mDC1s_F1': ['severe', 'mDC1s', 'Mock', 11, 'modeling', 3.35, 'Cohorte 2'],
  'BRU_Chr_mDC1s_F2': ['severe', 'mDC1s', 'SARS', 11, 'modeling', 3.25, 'Cohorte 2'],
  'BRU_Chr_mDC1s_F3': ['severe', 'mDC1s', 'Agonist', 11, 'modeling', 3.54, 'Cohorte 2'],
  #'BRU_Chr_mDC1s_G1': ['severe', 'mDC1s', 'Mock', 15, 'modeling', 5.73, 'Cohorte 2'],
  #'BRU_Chr_mDC1s_G2': ['severe', 'mDC1s', 'SARS', 15, 'modeling', 5.26, 'Cohorte 2'],
  #'BRU_Chr_mDC1s_G3': ['severe', 'mDC1s', 'Agonist', 15, 'modeling', 6.61, 'Cohorte 2'],

  'HOU_ED_mDC1s_F1': ['severe', 'mDC1s', 'Mock', 15, 'modeling', 8.84, 'Cohorte 3'],
  'HOU_ED_mDC1s_F2': ['severe', 'mDC1s', 'SARS', 15, 'modeling', 8.34, 'Cohorte 3'],
  'HOU_ED_mDC1s_F3': ['severe', 'mDC1s', 'Agonist', 15, 'modeling', 6.7, 'Cohorte 3'],
  'HOU_ED_mDC1s_G1': ['severe', 'mDC1s', 'Mock', 18, 'modeling', 7.31, 'Cohorte 3'],
  'HOU_ED_mDC1s_G2': ['severe', 'mDC1s', 'SARS', 18, 'modeling', 6.68, 'Cohorte 3'],
  'HOU_ED_mDC1s_G3': ['severe', 'mDC1s', 'Agonist', 18, 'modeling', 5.68, 'Cohorte 3'],
  'HOU_ED_mDC1s_H1': ['severe', 'mDC1s', 'Mock', 20, 'modeling', 4.42, 'Cohorte 3'],
  'HOU_ED_mDC1s_H2': ['severe', 'mDC1s', 'SARS', 20, 'modeling', 2.82, 'Cohorte 3'],
  'HOU_ED_mDC1s_H3': ['severe', 'mDC1s', 'Agonist', 20, 'modeling', 3.56, 'Cohorte 3'],

  #'FAY_Rob_mDC1s_F1': ['severe', 'mDC1s', 'Mock', 12, 'bad-quality', 1.6, 'Cohorte 4'],
  #'FAY_Rob_mDC1s_F2': ['severe', 'mDC1s', 'SARS', 12, 'bad-quality', 1.09, 'Cohorte 4'],
  #'FAY_Rob_mDC1s_G1': ['severe', 'mDC1s', 'Mock', 28, 'bad-quality', 1.85, 'Cohorte 4'],
  #'FAY_Rob_mDC1s_G2': ['severe', 'mDC1s', 'SARS', 28, 'bad-quality', 3.54, 'Cohorte 4'],
  #'FAY_Rob_mDC1s_H1': ['severe', 'mDC1s', 'Mock', 35, 'bad-quality', 0.17, 'Cohorte 4'],
  #'FAY_Rob_mDC1s_H2': ['severe', 'mDC1s', 'SARS', 35, 'bad-quality', 0.73, 'Cohorte 4'],

  #'OZBE_mDC1s_G1': ['severe', 'mDC1s', 'Mock', 16, 'modeling', 5.81, 'Cohorte 5'],
  #'OZBE_mDC1s_G2': ['severe', 'mDC1s', 'SARS', 16, 'modeling', 5.69, 'Cohorte 5'],
  'OZBE_mDC1s_I1': ['severe', 'mDC1s', 'Mock', 30, 'modeling', 2.18, 'Cohorte 5'],
  'OZBE_mDC1s_I2': ['severe', 'mDC1s', 'SARS', 30, 'modeling', 2.84, 'Cohorte 5'],

  #'RESU_mDC1s_G1': ['severe', 'mDC1s', 'Mock', 36, 'bad-quality', 0.59, 'Cohorte 6'],
  #'RESU_mDC1s_G2': ['severe', 'mDC1s', 'SARS', 36, 'bad-quality', 0.32, 'Cohorte 6'],
  'RESU_mDC1s_H1': ['severe', 'mDC1s', 'Mock', 43, 'modeling', 0.71, 'Cohorte 6'],
  'RESU_mDC1s_H2': ['severe', 'mDC1s', 'SARS', 43, 'modeling', 0.52, 'Cohorte 6'],
  'RESU_mDC1s_I1': ['severe', 'mDC1s', 'Mock', 50, 'modeling', 1.23, 'Cohorte 6'],
  'RESU_mDC1s_I2': ['severe', 'mDC1s', 'SARS', 50, 'modeling', 1.32, 'Cohorte 6'],

  'Hu3_1_mDC1s_G1': ['healthy', 'mDC1s', 'Mock', 1, 'modeling', 6.93, 'Cohorte 1'],
  'Hu3_1_mDC1s_G2': ['healthy', 'mDC1s', 'SARS', 1, 'modeling', 8.19, 'Cohorte 1'],
  'Hu3_1_mDC1s_G3': ['healthy', 'mDC1s', 'Agonist', 1, 'modeling', 7.45, 'Cohorte 1'],

  'Hu3_2_mDC1s_H1': ['healthy', 'mDC1s', 'Mock', 11, 'modeling', 9.49, 'Cohorte 2'],
  'Hu3_2_mDC1s_H2': ['healthy', 'mDC1s', 'SARS', 11, 'modeling', 6.67, 'Cohorte 2'],
  'Hu3_2_mDC1s_H3': ['healthy', 'mDC1s', 'Agonist', 11, 'modeling', 8.8, 'Cohorte 2'],

  'Hu3_3_mDC1s_I1': ['healthy', 'mDC1s', 'Mock', 25, 'modeling', 7.36, 'Cohorte 3'],
  'Hu3_3_mDC1s_I2': ['healthy', 'mDC1s', 'SARS', 25, 'modeling', 8.42, 'Cohorte 3'],
  'Hu3_3_mDC1s_I3': ['healthy', 'mDC1s', 'Agonist', 25, 'modeling', 5.16, 'Cohorte 3'],

  'Hu3_4_mDC1s_I1': ['healthy', 'mDC1s', 'Mock', 35, 'modeling', 7.29, 'Cohorte 4'],
  'Hu3_4_mDC1s_I2': ['healthy', 'mDC1s', 'SARS', 35, 'modeling', 9.51, 'Cohorte 4'],
  'Hu3_4_mDC1s_I3': ['healthy', 'mDC1s', 'Agonist', 35, 'modeling', 7.45, 'Cohorte 4'],

  'Hu3_5_mDC1s_J1': ['healthy', 'mDC1s', 'Mock', 50, 'modeling', 8.62, 'Cohorte 5'],
  'Hu3_5_mDC1s_J2': ['healthy', 'mDC1s', 'SARS', 50, 'modeling', 9.24, 'Cohorte 5'],
  'Hu3_5_mDC1s_J3': ['healthy', 'mDC1s', 'Agonist', 50, 'modeling', 6.78, 'Cohorte 5'],

  #'Hu3_6_mDC1s_J1': ['healthy', 'mDC1s', 'Mock', 8, 'bad-quality', 1.66, 'Cohorte 6'],
  #'Hu3_6_mDC1s_J2': ['healthy', 'mDC1s', 'SARS', 8, 'bad-quality', 1.78, 'Cohorte 6'],

  'HD_6M20_mDC1s_H1': ['healthy', 'mDC1s', 'Mock', 183, 'modeling', 12.2, 'Cohorte 1'],
  'HD_6M20_mDC1s_H2': ['healthy', 'mDC1s', 'SARS', 183, 'modeling', 11.6, 'Cohorte 1'],
  'HD_6M20_mDC1s_H3': ['healthy', 'mDC1s', 'Agonist', 183, 'modeling', 8.33, 'Cohorte 1'],

  'BC_HV2_mDC1s_I1': ['healthy', 'mDC1s', 'Mock', 14, 'modeling', 13.5, 'Cohorte 2'],
  'BC_HV2_mDC1s_I2': ['healthy', 'mDC1s', 'SARS', 14, 'modeling', 12.6, 'Cohorte 2'],
  'BC_HV2_mDC1s_I3': ['healthy', 'mDC1s', 'Agonist', 14, 'modeling', 8.6, 'Cohorte 2'],

  'BV_HV1_mDC1s_J1': ['healthy', 'mDC1s', 'Mock', 27, 'modeling', 7.05, 'Cohorte 3'],
  'BV_HV1_mDC1s_J2': ['healthy', 'mDC1s', 'SARS', 27, 'modeling', 5.43, 'Cohorte 3'],
  'BV_HV1_mDC1s_J3': ['healthy', 'mDC1s', 'Agonist', 27, 'modeling', 4.68, 'Cohorte 3'],

  'HV_29_mDC1s_J1': ['healthy', 'mDC1s', 'Mock', 37, 'modeling', 5.14, 'Cohorte 4'],
  'HV_29_mDC1s_J2': ['healthy', 'mDC1s', 'SARS', 37, 'modeling', 11.0, 'Cohorte 4'],
  'HV_29_mDC1s_J3': ['healthy', 'mDC1s', 'Agonist', 37, 'modeling', 5.37, 'Cohorte 4'],

  'HD_3M31_mDC1s_K1': ['healthy', 'mDC1s', 'Mock', 15, 'modeling', 7.39, 'Cohorte 5'],
  'HD_3M31_mDC1s_K2': ['healthy', 'mDC1s', 'SARS', 15, 'modeling', 10.2, 'Cohorte 5'],
  'HD_3M31_mDC1s_K3': ['healthy', 'mDC1s', 'Agonist', 15, 'modeling', 10.7, 'Cohorte 5'],

  'HD_EF9S_mDC1s_K1': ['healthy', 'mDC1s', 'Mock', 22, 'modeling', 9.82, 'Cohorte 6'],
  'HD_EF9S_mDC1s_K2': ['healthy', 'mDC1s', 'SARS', 22, 'modeling', 11.1, 'Cohorte 6'],
  #'HD_EF9S_mDC1s_K3': ['healthy', 'mDC1s', 'Agonist', 22, 'bad-quality', 4.15, 'Cohorte 6'],  #######

  'HV_F23_mDC1s_L1': ['healthy', 'mDC1s', 'Mock', 30, 'modeling', 16.2, 'Cohorte 6'],
  'HV_F23_mDC1s_L2': ['healthy', 'mDC1s', 'SARS', 30, 'modeling', 15.2, 'Cohorte 6'],

  'EFS_P1_0901_mDC1s_3': ['healthy', 'mDC1s', 'Mock', 43, 'modeling', 5.63, 'Pilote 1'],
  'EFS_P1_0901_mDC1s_4': ['healthy', 'mDC1s', 'SARS', 43, 'modeling', 6.15, 'Pilote 1'],
  'EFS_P1_0901_mDC1s_5': ['healthy', 'mDC1s', 'Agonist', 43, 'modeling', 1.97, 'Pilote 1'],

  #'EFS_P2_0901_mDC1s_3': ['healthy', 'mDC1s', 'Mock', 19, 'bad-quality', 3.19, 'Pilote 2'],
  'EFS_P2_0901_mDC1s_4': ['healthy', 'mDC1s', 'SARS', 19, 'modeling', 5.5, 'Pilote 2'],
  #'EFS_P2_0901_mDC1s_7': ['healthy', 'mDC1s', 'Agonist', 19, 'modeling', 0, 'Pilote 2'],  ######

  'EFS_P1_0930_mDC1s_6': ['healthy', 'mDC1s', 'Mock', 32, 'modeling', 7.57, 'Pilote 1'],
  'EFS_P1_0930_mDC1s_7': ['healthy', 'mDC1s', 'SARS', 32, 'modeling', 7.61, 'Pilote 1'],
  'EFS_P1_0930_mDC1s_8': ['healthy', 'mDC1s', 'Agonist', 32, 'modeling', 3.98, 'Pilote 1'],

  'EFS_P2_1112_mDC1s_8': ['healthy', 'mDC1s', 'Mock', 4, 'modeling', 7.84, 'Pilote 2'],
  'EFS_P2_1112_mDC1s_9': ['healthy', 'mDC1s', 'SARS', 4, 'modeling', 9.51, 'Pilote 2'],
  #'EFS_P2_1112_mDC1s_12': ['healthy', 'mDC1s', 'Agonist', 4, 'modeling', 0, 'Pilote 2'] #####
}

################################################################################
# Mono
################################################################################

"""
          Cohorte 1 Cohorte 2 Cohorte 3 Cohorte 4 Cohorte 5 Cohorte 6 Pilot 1 Pilot 2
mono-PDL1pos	2,8k	3,3k	2,9k	2,9k	 2,9k	    2,9k	4,8k	2,9k
mono-CD80pos	1k	    893	    594	     985	594	         594	1,1k	985
mono-IL6pos	    5,1k	6,6k	3k	    5,1k	5,1k	    5,1k	14k	    5,1k
"""



df_treshold_mono = pd.DataFrame({
  'PD-L1': [2800, 3300, 2900, 2900, 2900, 2900, 4800, 2900],
  'CD80': [1000, 893, 594, 985, 594, 594, 1100, 985],
  'IL6': [5100, 6600, 3000, 5100, 5100, 5100, 14000, 5100]
}, index=['Cohorte 1',
          'Cohorte 2',
          'Cohorte 3',
          'Cohorte 4',
          'Cohorte 5',
          'Cohorte 6',
          'Pilote 1',
          'Pilote 2'])

# Early <= 15
#CD14conv CD16-CD14 CD16CD14int CD16-CD14dim_non_conv
dict_samples_mono = {
  'PD-0041_mono_A1': ['mild-early', 'mono', 'Mock', 4, 'modeling', 43.2, 'Cohorte 1', 33.3, 18.5, 24.0],
  'PD-0041_mono_A2': ['mild-early', 'mono', 'SARS', 4, 'modeling', 42.2, 'Cohorte 1', 31.2, 28.8, 19.6],
  'PD-0041_mono_A3': ['mild-early', 'mono', 'Agonist', 4, 'modeling', 19.6, 'Cohorte 1', 97.2, 0.41, 0.44],
  'PD-0041_mono_B1': ['mild-early', 'mono', 'Mock', 11, 'modeling', 46.8, 'Cohorte 1', 26.7, 16.7, 33.0],
  'PD-0041_mono_B2': ['mild-early', 'mono', 'SARS', 11, 'modeling', 51.5, 'Cohorte 1', 27.8, 29.2, 25.5],
  'PD-0041_mono_B3': ['mild-early', 'mono', 'Agonist', 11, 'modeling', 15.3, 'Cohorte 1', 97.1, 0.5, 0.55],
  'PD-0041_mono_C1': ['mild-late', 'mono', 'Mock', 18, 'modeling', 58.5, 'Cohorte 1', 30.1, 21.1, 27.4],
  'PD-0041_mono_C2': ['mild-late', 'mono', 'SARS', 18, 'modeling', 67.3, 'Cohorte 1', 49.0, 24.6, 12.1],
  'PD-0041_mono_C3': ['mild-late', 'mono', 'Agonist', 18, 'modeling', 33.6, 'Cohorte 1', 95.4, 0.41, 0.17],
  'PD-0041_mono_D1': ['mild-late', 'mono', 'Mock', 32, 'modeling', 59.3, 'Cohorte 1', 24.4, 9.63, 41.3],
  'PD-0041_mono_D2': ['mild-late', 'mono', 'SARS', 32, 'modeling', 67.7, 'Cohorte 1', 31.4, 19.8, 27.8],
  'PD-0041_mono_D3': ['mild-late', 'mono', 'Agonist', 32, 'modeling', 46.2, 'Cohorte 1', 98.4, 0.098, 0.072],

  'GC-0038_mono_A1': ['mild-early', 'mono', 'Mock', 1, 'modeling', 80.3, 'Cohorte 2', 24.6, 69.1, 1.7],
  'GC-0038_mono_A2': ['mild-early', 'mono', 'SARS', 1, 'modeling', 81.1, 'Cohorte 2', 20.2, 73.0, 2.2],
  'GC-0038_mono_A3': ['mild-early', 'mono', 'Agonist', 1, 'modeling', 55.9, 'Cohorte 2', 96.4, 1.33, 0.42],
  'GC-0038_mono_B1': ['mild-early', 'mono', 'Mock', 8, 'modeling', 52.8, 'Cohorte 2', 23.1, 61.6, 10.3],
  'GC-0038_mono_B2': ['mild-early', 'mono', 'SARS', 8, 'modeling', 61.2, 'Cohorte 2', 27.1, 62.6, 5.67],
  'GC-0038_mono_B3': ['mild-early', 'mono', 'Agonist', 8, 'modeling', 44.0, 'Cohorte 2', 98.8, 0.29, 0.15],
  'GC-0038_mono_C1': ['mild-early', 'mono', 'Mock', 15, 'modeling', 81.5, 'Cohorte 2', 29.0, 60.5, 5.55],
  'GC-0038_mono_C2': ['mild-early', 'mono', 'SARS', 15, 'modeling', 84.9, 'Cohorte 2', 31.4, 60.7, 3.57],
  'GC-0038_mono_C3': ['mild-early', 'mono', 'Agonist', 15, 'modeling', 67.9, 'Cohorte 2', 98.3, 0.32, 0.13],
  'GC-0038_mono_D1': ['mild-late', 'mono', 'Mock', 22, 'modeling', 74.8, 'Cohorte 2', 27.4, 59.7, 7.58],
  'GC-0038_mono_D2': ['mild-late', 'mono', 'SARS', 22, 'modeling', 73.1, 'Cohorte 2', 23.6, 65.3, 6.64],
  'GC-0038_mono_D3': ['mild-late', 'mono', 'Agonist', 22, 'modeling', 58.2, 'Cohorte 2', 99.5, 0.11, 0.023],

  #'GC-0017_mono_A1': ['mild-early', 'mono', 'Mock', 4, 'modeling', , 'Cohorte 3'],
  #'GC-0017_mono_A2': ['mild-early', 'mono', 'SARS', 4, 'modeling', , 'Cohorte 3'],
  #'GC-0017_mono_A3': ['mild-early', 'mono', 'Agonist', 4, 'modeling', , 'Cohorte 3'],
  'GC-0017_mono_B1': ['mild-early', 'mono', 'Mock', 10, 'modeling', 69.8, 'Cohorte 3', 48.3, 44.4, 2.68],
  'GC-0017_mono_B2': ['mild-early', 'mono', 'SARS', 10, 'modeling', 70.4, 'Cohorte 3', 44.4, 47.2, 3.97],
  'GC-0017_mono_B3': ['mild-early', 'mono', 'Agonist', 10, 'modeling', 50.1, 'Cohorte 3', 99.6, 0.085, 0.11],
  'GC-0017_mono_C1': ['mild-late', 'mono', 'Mock', 19, 'modeling', 77.7, 'Cohorte 3', 37.5, 53.2, 5.08],
  'GC-0017_mono_C2': ['mild-late', 'mono', 'SARS', 19, 'modeling', 80.7, 'Cohorte 3', 34.6, 54.4, 6.73],
  'GC-0017_mono_C3': ['mild-late', 'mono', 'Agonist', 19, 'modeling', 68, 'Cohorte 3', 99.6, 0.073, 0.063],
  #'GC-0017_mono_D1': ['mild-late', 'mono', 'Mock', 25, 'bad-quality', , 'Cohorte 3'],
  #'GC-0017_mono_D2': ['mild-late', 'mono', 'SARS', 25, 'bad-quality', , 'Cohorte 3'],
  'GC-0017_mono_E1': ['mild-late', 'mono', 'Mock', 183, 'modeling', 72.9, 'Cohorte 3', 67.3, 26.2, 2.15],
  'GC-0017_mono_E2': ['mild-late', 'mono', 'SARS', 183, 'modeling', 75.5, 'Cohorte 3', 67.2, 26.8, 2.18],
  'GC-0017_mono_E3': ['mild-late', 'mono', 'Agonist', 183, 'modeling', 56.2, 'Cohorte 3', 99.9, 0.042, 0.000846],

  #'AS-0030_mono_A1': ['mild-early', 'mono', 'Mock', 1, 'modeling', , 'Cohorte 4'],
  #'AS-0030_mono_A2': ['mild-early', 'mono', 'SARS', 1, 'modeling', , 'Cohorte 4'],
  #'AS-0030_mono_A3': ['mild-early', 'mono', 'Agonist', 1, 'modeling', , 'Cohorte 4'],
  'AS-0030_mono_B1': ['mild-early', 'mono', 'Mock', 8, 'modeling', 69.1, 'Cohorte 4', 19.8, 68.0, 5.47],
  'AS-0030_mono_B2': ['mild-early', 'mono', 'SARS', 8, 'modeling', 72.1, 'Cohorte 4', 23.6, 64.6, 3.9],
  'AS-0030_mono_B3': ['mild-early', 'mono', 'Agonist', 8, 'modeling', 30.9, 'Cohorte 4', 94.6, 1.86, 0.29],
  #'AS-0030_mono_C1': ['mild-early', 'mono', 'Mock', 14, 'bad-quality', , 'Cohorte 4'],
  #'AS-0030_mono_C2': ['mild-early', 'mono', 'SARS', 14, 'modeling', , 'Cohorte 4'],
  #'AS-0030_mono_C3': ['mild-early', 'mono', 'Agonist', 14, 'bad-quality', , 'Cohorte 4'],
  'AS-0030_mono_D1': ['mild-late', 'mono', 'Mock', 22, 'modeling', 65.9, 'Cohorte 4', 21.1, 66.0, 6.29],
  'AS-0030_mono_D2': ['mild-late', 'mono', 'SARS', 22, 'modeling', 64.9, 'Cohorte 4', 22.2, 66.3, 5.64],
  'AS-0030_mono_D3': ['mild-late', 'mono', 'Agonist', 22, 'modeling', 25.9, 'Cohorte 4', 96.5, 0.6, 0.36],
  'AS-0030_mono_E1': ['mild-late', 'mono', 'Mock', 183, 'modeling', 75.0, 'Cohorte 4', 24.7, 63.9, 5.8],
  'AS-0030_mono_E2': ['mild-late', 'mono', 'SARS', 183, 'modeling', 76.1, 'Cohorte 4', 26.9, 60.8, 5.78],
  'AS-0030_mono_E3': ['mild-late', 'mono', 'Agonist', 183, 'modeling', 40.0, 'Cohorte 4', 99.0, 0.54, 0.07],

  'LD-0175_mono_A1': ['mild-early', 'mono', 'Mock', 1, 'modeling', 43.3, 'Cohorte 5', 31.6, 50.4, 10.4],
  'LD-0175_mono_A2': ['mild-early', 'mono', 'SARS', 1, 'modeling', 41.6, 'Cohorte 5', 31.8, 52.5, 8.83],
  'LD-0175_mono_A3': ['mild-early', 'mono', 'Agonist', 1, 'modeling', 5.46, 'Cohorte 5', 98.6, 0.53, 0.11],
  'LD-0175_mono_B1': ['mild-early', 'mono', 'Mock', 8, 'modeling', 74.7, 'Cohorte 5', 41.9, 45.6, 5.53],
  'LD-0175_mono_B2': ['mild-early', 'mono', 'SARS', 8, 'modeling', 74.3, 'Cohorte 5', 34.2, 53.3, 5.39],
  'LD-0175_mono_B3': ['mild-early', 'mono', 'Agonist', 8, 'modeling', 33.9, 'Cohorte 5', 99.1, 0.18, 0.072],
  'LD-0175_mono_C1': ['mild-early', 'mono', 'Mock', 13, 'modeling', 68.6, 'Cohorte 5', 30.9, 53.4, 9.79],
  'LD-0175_mono_C2': ['mild-early', 'mono', 'SARS', 13, 'modeling', 63.5, 'Cohorte 5', 29.8, 51.1, 11.9],
  'LD-0175_mono_C3': ['mild-early', 'mono', 'Agonist', 13, 'modeling', 19.6, 'Cohorte 5', 96.2, 0.37, 0.26],
  'LD-0175_mono_D1': ['mild-late', 'mono', 'Mock', 20, 'modeling', 29.5, 'Cohorte 5', 41.6, 31.1, 19.2],
  'LD-0175_mono_D2': ['mild-late', 'mono', 'SARS', 20, 'modeling', 32.9, 'Cohorte 5', 45.7, 29.9, 15.6],
  'LD-0175_mono_D3': ['mild-late', 'mono', 'Agonist', 20, 'modeling', 3.15, 'Cohorte 5', 98.2, 0.3, 0.3],
  #'LD-0175_mono_E1': ['mild-late', 'mono', 'Mock', 183, 'bad-quality', , 'Cohorte 5'],
  #'LD-0175_mono_E2': ['mild-late', 'mono', 'SARS', 183, 'bad-quality', , 'Cohorte 5'],
  #'LD-0175_mono_E3': ['mild-late', 'mono', 'Agonist', 183, 'bad-quality', , 'Cohorte 5'],

  #'PS-0029_mono_A1': ['mild-early', 'mono', 'Mock', 2, 'modeling', , 'Cohorte 6'],
  #'PS-0029_mono_A2': ['mild-early', 'mono', 'SARS', 2, 'modeling', , 'Cohorte 6'],
  #'PS-0029_mono_A3': ['mild-early', 'mono', 'Agonist', 2, 'modeling', , 'Cohorte 6'],
  #'PS-0029_mono_B1': ['mild-early', 'mono', 'Mock', 9, 'bad-quality', , 'Cohorte 6'],
  #'PS-0029_mono_B2': ['mild-early', 'mono', 'SARS', 9, 'bad-quality', , 'Cohorte 6'],
  #'PS-0029_mono_B3': ['mild-early', 'mono', 'Agonist', 9, 'bad-quality', , 'Cohorte 6'],
  'PS-0029_mono_C1': ['mild-late', 'mono', 'Mock', 16, 'modeling', 65.9, 'Cohorte 6', 39.7, 44.8, 7.45],
  #'PS-0029_mono_C2': ['mild-late', 'mono', 'SARS', 16, 'modeling', , 'Cohorte 6', ],
  'PS-0029_mono_C3': ['mild-late', 'mono', 'Agonist', 16, 'modeling', 42.4, 'Cohorte 6', 92.3, 0.68, 0.51],
  #'PS-0029_mono_D1': ['mild-late', 'mono', 'Mock', 23, 'bad-quality', , 'Cohorte 6'],
  #'PS-0029_mono_D2': ['mild-late', 'mono', 'SARS', 23, 'bad-quality', , 'Cohorte 6'],
  'PS-0029_mono_E1': ['mild-late', 'mono', 'Mock', 30, 'modeling', 67.7, 'Cohorte 6', 35.0, 49.5, 8.0],
  'PS-0029_mono_E2': ['mild-late', 'mono', 'SARS', 30, 'modeling', 62.4, 'Cohorte 6', 40.7, 43.0, 7.91],
  'PS-0029_mono_E3': ['mild-late', 'mono', 'Agonist', 30, 'modeling', 50.5, 'Cohorte 6', 97.4, 0.34, 0.28],
  'PS-0029_mono_F1': ['mild-late', 'mono', 'Mock', 183, 'modeling', 70.3, 'Cohorte 6', 49.7, 37.1, 5.43],
  'PS-0029_mono_F2': ['mild-late', 'mono', 'SARS', 183, 'modeling', 49.6, 'Cohorte 6', 48.4, 37.2, 6.16],
  'PS-0029_mono_F3': ['mild-late', 'mono', 'Agonist', 183, 'modeling', 49.3, 'Cohorte 6', 95.7, 0.52, 0.55],

  #'CHA_Mah_mono_E1': ['severe', 'mono', 'Mock', 27, 'bad-quality', , 'Cohorte 1'],
  #'CHA_Mah_mono_E2': ['severe', 'mono', 'SARS', 27, 'bad-quality', , 'Cohorte 1'],
  #'CHA_Mah_mono_E3': ['severe', 'mono', 'Agonist', 27, 'bad-quality', , 'Cohorte 1'],
  'CHA_Mah_mono_F1': ['severe', 'mono', 'Mock', 37, 'modeling', 46.9, 'Cohorte 1', 23.9, 26.6, 30.5],
  'CHA_Mah_mono_F2': ['severe', 'mono', 'SARS', 37, 'modeling', 65.8, 'Cohorte 1', 46.2, 30.6, 11.5],
  'CHA_Mah_mono_F3': ['severe', 'mono', 'Agonist', 37, 'modeling', 44.8, 'Cohorte 1', 99.1, 0.092, 0.14],

  'BRU_Chr_mono_E1': ['severe', 'mono', 'Mock', 9, 'modeling', 68.3, 'Cohorte 2', 32.8, 63.3, 0.33],
  'BRU_Chr_mono_E2': ['severe', 'mono', 'SARS', 9, 'modeling', 75.1, 'Cohorte 2', 32.0, 64.1, 0.19],
  'BRU_Chr_mono_E3': ['severe', 'mono', 'Agonist', 9, 'modeling', 72.4, 'Cohorte 2', 98.8, 0.79, 0.046],
  'BRU_Chr_mono_F1': ['severe', 'mono', 'Mock', 11, 'modeling', 66.3, 'Cohorte 2', 27.7, 66.7, 0.8],
  'BRU_Chr_mono_F2': ['severe', 'mono', 'SARS', 11, 'modeling', 70.0, 'Cohorte 2', 31.1, 62.6, 0.34],
  'BRU_Chr_mono_F3': ['severe', 'mono', 'Agonist', 11, 'modeling', 60.5, 'Cohorte 2', 98.1, 0.84, 0.11],
  #'BRU_Chr_mono_G1': ['severe', 'mono', 'Mock', 15, 'bad-quality', , 'Cohorte 2'],
  #'BRU_Chr_mono_G2': ['severe', 'mono', 'SARS', 15, 'bad-quality', , 'Cohorte 2'],
  #'BRU_Chr_mono_G3': ['severe', 'mono', 'Agonist', 15, 'bad-quality', , 'Cohorte 2'],

  'HOU_ED_mono_F1': ['severe', 'mono', 'Mock', 15, 'modeling', 49.6, 'Cohorte 3', 57.8, 32.0, 5.67],
  'HOU_ED_mono_F2': ['severe', 'mono', 'SARS', 15, 'modeling', 44.5, 'Cohorte 3', 44.7, 40.2, 10.3],
  'HOU_ED_mono_F3': ['severe', 'mono', 'Agonist', 15, 'modeling', 68.6, 'Cohorte 3', 99.0, 0.29, 0.19],
  'HOU_ED_mono_G1': ['severe', 'mono', 'Mock', 18, 'modeling', 61.7, 'Cohorte 3', 57.9, 32.0, 4.38],
  'HOU_ED_mono_G2': ['severe', 'mono', 'SARS', 18, 'modeling', 65.2, 'Cohorte 3', 44.9, 47.7, 3.59],
  'HOU_ED_mono_G3': ['severe', 'mono', 'Agonist', 18, 'modeling', 78.4, 'Cohorte 3', 98.9, 0.46, 0.17],
  'HOU_ED_mono_H1': ['severe', 'mono', 'Mock', 20, 'modeling', 51.7, 'Cohorte 3', 38.7, 48.6, 8.7],
  'HOU_ED_mono_H2': ['severe', 'mono', 'SARS', 20, 'modeling', 53.0, 'Cohorte 3', 36.6, 52.1, 7.38],
  'HOU_ED_mono_H3': ['severe', 'mono', 'Agonist', 20, 'modeling', 68.9, 'Cohorte 3', 99.7, 0.061, 0.77],

  #'FAY_Rob_mono_F1': ['severe', 'mono', 'Mock', 12, 'bad-quality', , 'Cohorte 4'],
  #'FAY_Rob_mono_F2': ['severe', 'mono', 'SARS', 12, 'bad-quality', , 'Cohorte 4'],
  #'FAY_Rob_mono_G1': ['severe', 'mono', 'Mock', 28, 'bad-quality', , 'Cohorte 4'],
  #'FAY_Rob_mono_G2': ['severe', 'mono', 'SARS', 28, 'bad-quality', , 'Cohorte 4'],
  #'FAY_Rob_mono_H1': ['severe', 'mono', 'Mock', 35, 'bad-quality', , 'Cohorte 4'],
  #'FAY_Rob_mono_H2': ['severe', 'mono', 'SARS', 35, 'bad-quality', , 'Cohorte 4'],

  #'OZBE_mono_G1': ['severe', 'mono', 'Mock', 16, 'bad-quality', , 'Cohorte 5'],
  #'OZBE_mono_G2': ['severe', 'mono', 'SARS', 16, 'bad-quality', , 'Cohorte 5'],
  'OZBE_mono_H1': ['severe', 'mono', 'Mock', 23, 'modeling', 11.9, 'Cohorte 5', 61.6, 23.8, 5.4],
  'OZBE_mono_H2': ['severe', 'mono', 'SARS', 23, 'modeling', 18.9, 'Cohorte 5', 54.5, 33.1, 4.55],
  #'OZBE_mono_I1': ['severe', 'mono', 'Mock', 30, 'modeling', , 'Cohorte 5'],
  #'OZBE_mono_I2': ['severe', 'mono', 'SARS', 30, 'modeling', , 'Cohorte 5'],

  #'RESU_mono_G1': ['severe', 'mono', 'Mock', 36, 'bad-quality', , 'Cohorte 6'],
  #'RESU_mono_G2': ['severe', 'mono', 'SARS', 36, 'bad-quality', , 'Cohorte 6'],
  #'RESU_mono_H1': ['severe', 'mono', 'Mock', 43, 'modeling', , 'Cohorte 6'],
  #'RESU_mono_H2': ['severe', 'mono', 'SARS', 43, 'modeling', , 'Cohorte 6'],
  #'RESU_mono_I1': ['severe', 'mono', 'Mock', 50, 'modeling', , 'Cohorte 6'],
  #'RESU_mono_I2': ['severe', 'mono', 'SARS', 50, 'modeling', , 'Cohorte 6'],

  'Hu3_1_mono_G1': ['healthy', 'mono', 'Mock', 1, 'modeling', 56.5, 'Cohorte 1', 28.3, 19.6, 28.2],
  'Hu3_1_mono_G2': ['healthy', 'mono', 'SARS', 1, 'modeling', 62.5, 'Cohorte 1', 39.9, 24.2, 15.7],
  'Hu3_1_mono_G3': ['healthy', 'mono', 'Agonist', 1, 'modeling', 45.6, 'Cohorte 1', 98.4, 0.19, 0.23],

  'Hu3_2_mono_H1': ['healthy', 'mono', 'Mock', 11, 'modeling', 75.8, 'Cohorte 2', 40.1, 51.9, 2.28 ],
  'Hu3_2_mono_H2': ['healthy', 'mono', 'SARS', 11, 'modeling', 74.7, 'Cohorte 2', 51.0, 40.9, 1.83],
  'Hu3_2_mono_H3': ['healthy', 'mono', 'Agonist', 11, 'modeling', 74.5, 'Cohorte 2', 99.6, 0.19, 0.05],

  'Hu3_3_mono_I1': ['healthy', 'mono', 'Mock', 25, 'modeling', 61.8, 'Cohorte 3', 50.7, 37.8, 5.18],
  'Hu3_3_mono_I2': ['healthy', 'mono', 'SARS', 25, 'modeling', 61.0, 'Cohorte 3', 44.0, 45.7, 4.94],
  'Hu3_3_mono_I3': ['healthy', 'mono', 'Agonist', 25, 'modeling', 50.9, 'Cohorte 3', 99.7, 0.089, 0.078],

  'Hu3_4_mono_I1': ['healthy', 'mono', 'Mock', 35, 'modeling', 63.1, 'Cohorte 4', 29.7, 52.2, 7.05],
  'Hu3_4_mono_I2': ['healthy', 'mono', 'SARS', 35, 'modeling', 57.0, 'Cohorte 4', 33.9, 45.9, 7.32],
  'Hu3_4_mono_I3': ['healthy', 'mono', 'Agonist', 35, 'modeling', 41.5, 'Cohorte 4', 99.6, 0.1, 0.043],

  'Hu3_5_mono_J1': ['healthy', 'mono', 'Mock', 50, 'modeling', 76.6, 'Cohorte 5', 31.8, 54.8, 5.57],
  'Hu3_5_mono_J2': ['healthy', 'mono', 'SARS', 50, 'modeling', 75.7, 'Cohorte 5', 33.7, 54.7, 4.24],
  'Hu3_5_mono_J3': ['healthy', 'mono', 'Agonist', 50, 'modeling', 61.7,'Cohorte 5', 99.4, 0.17, 0.095],

  'Hu3_6_mono_J1': ['healthy', 'mono', 'Mock', 8, 'modeling', 17.5, 'Cohorte 6', 36, 47, 7.92],
  #'Hu3_6_mono_J2': ['healthy', 'mono', 'SARS', 8, 'modeling', , 'Cohorte 6'],
  'Hu3_6_mono_J3': ['healthy', 'mono', 'SARS', 8, 'modeling', 3.89, 'Cohorte 6', 95.0, 3.75, 1.25],

  'HD_6M20_mono_H1': ['healthy', 'mono', 'Mock', 183, 'modeling', 65.5, 'Cohorte 1', 44.0, 33.3, 9.06],
  'HD_6M20_mono_H2': ['healthy', 'mono', 'SARS', 183, 'modeling', 74.2, 'Cohorte 1', 46.6, 38.1, 5.81],
  'HD_6M20_mono_H3': ['healthy', 'mono', 'Agonist', 183, 'modeling', 51.4, 'Cohorte 1', 98.5, 0.26, 0.2],

  'BC_HV2_mono_I1': ['healthy', 'mono', 'Mock', 14, 'modeling', 62.7, 'Cohorte 2', 65.6, 26.6, 2.23],
  'BC_HV2_mono_I2': ['healthy', 'mono', 'SARS', 14, 'modeling', 65.1, 'Cohorte 2', 59.0, 34.2, 1.82],
  'BC_HV2_mono_I3': ['healthy', 'mono', 'Agonist', 14, 'modeling', 63.2, 'Cohorte 2', 99.5, 0.23, 0.00813],

  'BV_HV1_mono_J1': ['healthy', 'mono', 'Mock', 27, 'modeling', 61.9, 'Cohorte 3', 43.9, 38.8, 9.49],
  'BV_HV1_mono_J2': ['healthy', 'mono', 'SARS', 27, 'modeling', 65.0, 'Cohorte 3', 48.7, 39.9, 5.0],
  'BV_HV1_mono_J3': ['healthy', 'mono', 'Agonist', 27, 'modeling', 60.5, 'Cohorte 3', 99.9, 0.044, 0.035],

  'HV_29_mono_J1': ['healthy', 'mono', 'Mock', 37, 'modeling', 49.2, 'Cohorte 4', 25.6, 46.6, 16.3],
  'HV_29_mono_J2': ['healthy', 'mono', 'SARS', 37, 'modeling', 57.8, 'Cohorte 4', 33.7, 46.0, 7.33],
  'HV_29_mono_J3': ['healthy', 'mono', 'Agonist', 37, 'modeling', 19.3, 'Cohorte 4', 99.3, 0.15, 0.15],

  'HD_3M31_mono_K1': ['healthy', 'mono', 'Mock', 15, 'modeling', 75.8, 'Cohorte 5', 36.7, 49.2, 6.63],
  'HD_3M31_mono_K2': ['healthy', 'mono', 'SARS', 15, 'modeling', 73.5, 'Cohorte 5', 32.5, 52.9, 7.36],
  'HD_3M31_mono_K3': ['healthy', 'mono', 'Agonist', 15, 'modeling', 52.7, 'Cohorte 5', 97.4, 0.33, 0.14],

  'HD_EF9S_mono_K1': ['healthy', 'mono', 'Mock', 22, 'modeling', 67.9, 'Cohorte 6', 42.3, 48, 2.73],
  'HD_EF9S_mono_K2': ['healthy', 'mono', 'SARS', 22, 'modeling', 67.2, 'Cohorte 6', 45.8, 44.8, 2.72],
  'HD_EF9S_mono_K3': ['healthy', 'mono', 'Agonist', 22, 'modeling', 51.6, 'Cohorte 6', 99.2, 0.12, 0.25],

  #'HV_F23_mono_L1': ['healthy', 'mono', 'Mock', 30, 'modeling', , 'Cohorte 6'],
  #'HV_F23_mono_L2': ['healthy', 'mono', 'SARS', 30, 'modeling', , 'Cohorte 6'],

  'EFS_P1_0901_mono_3': ['healthy', 'mono', 'Mock', 43, 'modeling', 41, 'Pilote 1', 17.8, 39.3, 33.3],
  'EFS_P1_0901_mono_4': ['healthy', 'mono', 'SARS', 43, 'modeling', 40.6, 'Pilote 1', 20.7, 41.0, 29.1],
  'EFS_P1_0901_mono_5': ['healthy', 'mono', 'Agonist', 43, 'modeling', 7.95, 'Pilote 1', 99.1, 0.0, 0.17],

  #'EFS_P2_0901_mono_3': ['healthy', 'mono', 'Mock', 19, 'bad-quality', , 'Pilote 2'],
  #'EFS_P2_0901_mono_4': ['healthy', 'mono', 'SARS', 19, 'modeling', , 'Pilote 2'],
  #'EFS_P2_0901_mono_7': ['healthy', 'mono', 'Agonist', 19, 'modeling', , 'Pilote 2'],

  'EFS_P1_0930_mono_6': ['healthy', 'mono', 'Mock', 32, 'modeling', 69.8, 'Pilote 1', 11.9, 53.9, 28.8],
  'EFS_P1_0930_mono_7': ['healthy', 'mono', 'SARS', 32, 'modeling', 69.8, 'Pilote 1', 14.9, 53.3, 25.0],
  'EFS_P1_0930_mono_8': ['healthy', 'mono', 'Agonist', 32, 'modeling', 27.5, 'Pilote 1', 99.0, 0.15, 0.077],

  #'EFS_P2_1112_mono_8': ['healthy', 'mono', 'Mock', 4, 'modeling', , 'Pilote 2'],
  #'EFS_P2_1112_mono_9': ['healthy', 'mono', 'SARS', 4, 'modeling', , 'Pilote 2'],
  #'EFS_P2_1112_mono_12': ['healthy', 'mono', 'Agonist', 4, 'modeling', , 'Pilote 2']
}


################################################################################
# mDC2
################################################################################

"""
          Cohorte 1 Cohorte 2 Cohorte 3 Cohorte 4 Cohorte 5 Cohorte 6 Pilot 1 Pilot 2
mono-PDL1pos	1,9k	1,9k	1,9k	1,9k	1,9k	1,9k	9,9k	1,9k
mono-CD80pos	959	568	568	985	568	776	1,1k	959
mono-IL6pos	3,7k	4k	5,3k	4,9k	7,1k	2,3k	9,6k	3,7k
"""

df_treshold_mDC2 = pd.DataFrame({
  'PD-L1': [1900, 1900, 1900, 1900, 1900, 1900, 9900, 1900],
  'CD80': [959, 568, 568, 985, 568, 776, 1100, 959],
  'IL6': [3700, 4000, 5300, 4900, 7100, 2300, 9600, 3700]
}, index=['Cohorte 1',
          'Cohorte 2',
          'Cohorte 3',
          'Cohorte 4',
          'Cohorte 5',
          'Cohorte 6',
          'Pilote 1',
          'Pilote 2'])

# Early <= 15
dict_samples_mDC2 = {
  'PD-0041_mDC2_A1': ['mild-early', 'mDC2', 'Mock', 4, 'modeling', 1.06, 'Cohorte 1'],
  'PD-0041_mDC2_A2': ['mild-early', 'mDC2', 'SARS', 4, 'modeling', 1.54, 'Cohorte 1'],
  'PD-0041_mDC2_A3': ['mild-early', 'mDC2', 'Agonist', 4, 'modeling', 6.06, 'Cohorte 1'],
  'PD-0041_mDC2_B1': ['mild-early', 'mDC2', 'Mock', 11, 'modeling', 2.66, 'Cohorte 1'],
  'PD-0041_mDC2_B2': ['mild-early', 'mDC2', 'SARS', 11, 'modeling', 3.0, 'Cohorte 1'],
  'PD-0041_mDC2_B3': ['mild-early', 'mDC2', 'Agonist', 11, 'modeling', 4.83, 'Cohorte 1'],
  'PD-0041_mDC2_C1': ['mild-late', 'mDC2', 'Mock', 18, 'modeling', 3.2, 'Cohorte 1'],
  'PD-0041_mDC2_C2': ['mild-late', 'mDC2', 'SARS', 18, 'modeling', 5.36, 'Cohorte 1'],
  'PD-0041_mDC2_C3': ['mild-late', 'mDC2', 'Agonist', 18, 'modeling', 6.4, 'Cohorte 1'],
  'PD-0041_mDC2_D1': ['mild-late', 'mDC2', 'Mock', 32, 'modeling', 3.59, 'Cohorte 1'],
  'PD-0041_mDC2_D2': ['mild-late', 'mDC2', 'SARS', 32, 'modeling', 4.46, 'Cohorte 1'],
  'PD-0041_mDC2_D3': ['mild-late', 'mDC2', 'Agonist', 32, 'modeling', 8.12, 'Cohorte 1'],

  'GC-0038_mDC2_A1': ['mild-early', 'mDC2', 'Mock', 1, 'modeling', 2.45, 'Cohorte 2'],
  'GC-0038_mDC2_A2': ['mild-early', 'mDC2', 'SARS', 1, 'modeling', 1.28, 'Cohorte 2'],
  'GC-0038_mDC2_A3': ['mild-early', 'mDC2', 'Agonist', 1, 'modeling', 7.36, 'Cohorte 2'],
  'GC-0038_mDC2_B1': ['mild-early', 'mDC2', 'Mock', 8, 'modeling', 2.13, 'Cohorte 2'],
  'GC-0038_mDC2_B2': ['mild-early', 'mDC2', 'SARS', 8, 'modeling', 3.56, 'Cohorte 2'],
  'GC-0038_mDC2_B3': ['mild-early', 'mDC2', 'Agonist', 8, 'modeling', 6.74, 'Cohorte 2'],
  'GC-0038_mDC2_C1': ['mild-early', 'mDC2', 'Mock', 15, 'modeling', 2.13, 'Cohorte 2'],
  'GC-0038_mDC2_C2': ['mild-early', 'mDC2', 'SARS', 15, 'modeling', 2.58, 'Cohorte 2'],
  'GC-0038_mDC2_C3': ['mild-early', 'mDC2', 'Agonist', 15, 'modeling', 3.85, 'Cohorte 2'],
  'GC-0038_mDC2_D1': ['mild-late', 'mDC2', 'Mock', 22, 'modeling', 3.12, 'Cohorte 2'],
  'GC-0038_mDC2_D2': ['mild-late', 'mDC2', 'SARS', 22, 'modeling', 3.66, 'Cohorte 2'],
  'GC-0038_mDC2_D3': ['mild-late', 'mDC2', 'Agonist', 22, 'modeling', 4.2, 'Cohorte 2'],

  #'GC-0017_mDC2_A1': ['mild-early', 'mDC2', 'Mock', 4, 'modeling', , 'Cohorte 3'],
  #'GC-0017_mDC2_A2': ['mild-early', 'mDC2', 'SARS', 4, 'modeling', , 'Cohorte 3'],
  #'GC-0017_mDC2_A3': ['mild-early', 'mDC2', 'Agonist', 4, 'modeling', , 'Cohorte 3'],
  'GC-0017_mDC2_B1': ['mild-early', 'mDC2', 'Mock', 10, 'modeling', 5.84, 'Cohorte 3'],
  'GC-0017_mDC2_B2': ['mild-early', 'mDC2', 'SARS', 10, 'modeling', 6.59, 'Cohorte 3'],
  'GC-0017_mDC2_B3': ['mild-early', 'mDC2', 'Agonist', 10, 'modeling', 5.15, 'Cohorte 3'],
  'GC-0017_mDC2_C1': ['mild-late', 'mDC2', 'Mock', 19, 'modeling', 5.25, 'Cohorte 3'],
  'GC-0017_mDC2_C2': ['mild-late', 'mDC2', 'SARS', 19, 'modeling', 4.96, 'Cohorte 3'],
  'GC-0017_mDC2_C3': ['mild-late', 'mDC2', 'Agonist', 19, 'modeling', 5.35, 'Cohorte 3'],
  #'GC-0017_mDC2_D1': ['mild-late', 'mDC2', 'Mock', 25, 'bad-quality', , 'Cohorte 3'],
  #'GC-0017_mDC2_D2': ['mild-late', 'mDC2', 'SARS', 25, 'bad-quality', , 'Cohorte 3'],
  'GC-0017_mDC2_E1': ['mild-late', 'mDC2', 'Mock', 183, 'modeling', 6.81, 'Cohorte 3'],
  'GC-0017_mDC2_E2': ['mild-late', 'mDC2', 'SARS', 183, 'modeling', 7.44, 'Cohorte 3'],
  'GC-0017_mDC2_E3': ['mild-late', 'mDC2', 'Agonist', 183, 'modeling', 4.04, 'Cohorte 3'],

  #'AS-0030_mDC2_A1': ['mild-early', 'mDC2', 'Mock', 1, 'modeling', , 'Cohorte 4'],
  #'AS-0030_mDC2_A2': ['mild-early', 'mDC2', 'SARS', 1, 'modeling', , 'Cohorte 4'],
  #'AS-0030_mDC2_A3': ['mild-early', 'mDC2', 'Agonist', 1, 'modeling', , 'Cohorte 4'],
  'AS-0030_mDC2_B1': ['mild-early', 'mDC2', 'Mock', 8, 'modeling', 4.11, 'Cohorte 4'],
  'AS-0030_mDC2_B2': ['mild-early', 'mDC2', 'SARS', 8, 'modeling', 5.06, 'Cohorte 4'],
  'AS-0030_mDC2_B3': ['mild-early', 'mDC2', 'Agonist', 8, 'modeling', 14.1, 'Cohorte 4'],
  #'AS-0030_mDC2_C1': ['mild-early', 'mDC2', 'Mock', 14, 'bad-quality', , 'Cohorte 4'],
  #'AS-0030_mDC2_C2': ['mild-early', 'mDC2', 'SARS', 14, 'modeling', , 'Cohorte 4'],
  #'AS-0030_mDC2_C3': ['mild-early', 'mDC2', 'Agonist', 14, 'bad-quality', , 'Cohorte 4'],
  'AS-0030_mDC2_D1': ['mild-late', 'mDC2', 'Mock', 22, 'modeling', 6.75, 'Cohorte 4'],
  'AS-0030_mDC2_D2': ['mild-late', 'mDC2', 'SARS', 22, 'modeling', 8.26, 'Cohorte 4'],
  'AS-0030_mDC2_D3': ['mild-late', 'mDC2', 'Agonist', 22, 'modeling', 13.9, 'Cohorte 4'],
  'AS-0030_mDC2_E1': ['mild-late', 'mDC2', 'Mock', 183, 'modeling', 3.79, 'Cohorte 4'],
  'AS-0030_mDC2_E2': ['mild-late', 'mDC2', 'SARS', 183, 'modeling', 3.99, 'Cohorte 4'],
  'AS-0030_mDC2_E3': ['mild-late', 'mDC2', 'Agonist', 183, 'modeling', 5.18, 'Cohorte 4'],

  'LD-0175_mDC2_A1': ['mild-early', 'mDC2', 'Mock', 1, 'modeling', 1.94, 'Cohorte 5'],
  'LD-0175_mDC2_A2': ['mild-early', 'mDC2', 'SARS', 1, 'modeling', 1.72, 'Cohorte 5'],
  'LD-0175_mDC2_A3': ['mild-early', 'mDC2', 'Agonist', 1, 'modeling', 4.22, 'Cohorte 5'],
  'LD-0175_mDC2_B1': ['mild-early', 'mDC2', 'Mock', 8, 'modeling', 10.2, 'Cohorte 5'],
  'LD-0175_mDC2_B2': ['mild-early', 'mDC2', 'SARS', 8, 'modeling', 10.4, 'Cohorte 5'],
  'LD-0175_mDC2_B3': ['mild-early', 'mDC2', 'Agonist', 8, 'modeling', 11.0, 'Cohorte 5'],
  'LD-0175_mDC2_C1': ['mild-early', 'mDC2', 'Mock', 13, 'modeling', 12.0, 'Cohorte 5'],
  'LD-0175_mDC2_C2': ['mild-early', 'mDC2', 'SARS', 13, 'modeling', 10.2, 'Cohorte 5'],
  'LD-0175_mDC2_C3': ['mild-early', 'mDC2', 'Agonist', 13, 'modeling', 11.7, 'Cohorte 5'],
  'LD-0175_mDC2_D1': ['mild-late', 'mDC2', 'Mock', 20, 'modeling', 10.7, 'Cohorte 5'],
  'LD-0175_mDC2_D2': ['mild-late', 'mDC2', 'SARS', 20, 'modeling', 12.2, 'Cohorte 5'],
  'LD-0175_mDC2_D3': ['mild-late', 'mDC2', 'Agonist', 20, 'modeling', 6.27, 'Cohorte 5'],
  #'LD-0175_mDC2_E1': ['mild-late', 'mDC2', 'Mock', 183, 'bad-quality', 4.27, 'Cohorte 5'],
  #'LD-0175_mDC2_E2': ['mild-late', 'mDC2', 'SARS', 183, 'bad-quality', 5.17, 'Cohorte 5'],
  #'LD-0175_mDC2_E3': ['mild-late', 'mDC2', 'Agonist', 183, 'bad-quality', 2.33, 'Cohorte 5'],

  #'PS-0029_mDC2_A1': ['mild-early', 'mDC2', 'Mock', 2, 'modeling', , 'Cohorte 6'],
  #'PS-0029_mDC2_A2': ['mild-early', 'mDC2', 'SARS', 2, 'modeling', , 'Cohorte 6'],
  #'PS-0029_mDC2_A3': ['mild-early', 'mDC2', 'Agonist', 2, 'modeling', , 'Cohorte 6'],
  #'PS-0029_mDC2_B1': ['mild-early', 'mDC2', 'Mock', 9, 'bad-quality', , 'Cohorte 6'],
  #'PS-0029_mDC2_B2': ['mild-early', 'mDC2', 'SARS', 9, 'bad-quality', , 'Cohorte 6'],
  #'PS-0029_mDC2_B3': ['mild-early', 'mDC2', 'Agonist', 9, 'bad-quality', , 'Cohorte 6'],
  'PS-0029_mDC2_C1': ['mild-late', 'mDC2', 'Mock', 16, 'modeling', 5.22,'Cohorte 6'],
  #'PS-0029_mDC2_C2': ['mild-late', 'mDC2', 'SARS', 16, 'modeling', , 'Cohorte 6', ],
  'PS-0029_mDC2_C3': ['mild-late', 'mDC2', 'Agonist', 16, 'modeling', 6.27,'Cohorte 6'],
  #'PS-0029_mDC2_D1': ['mild-late', 'mDC2', 'Mock', 23, 'bad-quality', , 'Cohorte 6'],
  #'PS-0029_mDC2_D2': ['mild-late', 'mDC2', 'SARS', 23, 'bad-quality', , 'Cohorte 6'],
  'PS-0029_mDC2_E1': ['mild-late', 'mDC2', 'Mock', 30, 'modeling', 5.66, 'Cohorte 6'],
  'PS-0029_mDC2_E2': ['mild-late', 'mDC2', 'SARS', 30, 'modeling', 5.78, 'Cohorte 6'],
  'PS-0029_mDC2_E3': ['mild-late', 'mDC2', 'Agonist', 30, 'modeling', 4.73, 'Cohorte 6'],
  'PS-0029_mDC2_F1': ['mild-late', 'mDC2', 'Mock', 183, 'modeling', 4.44, 'Cohorte 6'],
  'PS-0029_mDC2_F2': ['mild-late', 'mDC2', 'SARS', 183, 'modeling', 3.58, 'Cohorte 6'],
  'PS-0029_mDC2_F3': ['mild-late', 'mDC2', 'Agonist', 183, 'modeling', 3.84, 'Cohorte 6'],

  #'CHA_Mah_mDC2_E1': ['severe', 'mDC2', 'Mock', 27, 'bad-quality', , 'Cohorte 1'],
  #'CHA_Mah_mDC2_E2': ['severe', 'mDC2', 'SARS', 27, 'bad-quality', , 'Cohorte 1'],
  #'CHA_Mah_mDC2_E3': ['severe', 'mDC2', 'Agonist', 27, 'bad-quality', , 'Cohorte 1'],
  'CHA_Mah_mDC2_F1': ['severe', 'mDC2', 'Mock', 37, 'modeling', 1.5, 'Cohorte 1'],
  'CHA_Mah_mDC2_F2': ['severe', 'mDC2', 'SARS', 37, 'modeling', 1.41, 'Cohorte 1'],
  'CHA_Mah_mDC2_F3': ['severe', 'mDC2', 'Agonist', 37, 'modeling', 1.92, 'Cohorte 1'],

  'BRU_Chr_mDC2_E1': ['severe', 'mDC2', 'Mock', 9, 'modeling', 1.56, 'Cohorte 2'],
  'BRU_Chr_mDC2_E2': ['severe', 'mDC2', 'SARS', 9, 'modeling', 1.91, 'Cohorte 2'],
  'BRU_Chr_mDC2_E3': ['severe', 'mDC2', 'Agonist', 9, 'modeling', 0.86, 'Cohorte 2'],
  'BRU_Chr_mDC2_F1': ['severe', 'mDC2', 'Mock', 11, 'modeling', 2.03, 'Cohorte 2'],
  'BRU_Chr_mDC2_F2': ['severe', 'mDC2', 'SARS', 11, 'modeling', 2.01, 'Cohorte 2'],
  'BRU_Chr_mDC2_F3': ['severe', 'mDC2', 'Agonist', 11, 'modeling', 1.4, 'Cohorte 2'],
  #'BRU_Chr_mDC2_G1': ['severe', 'mDC2', 'Mock', 15, 'bad-quality', , 'Cohorte 2'],
  #'BRU_Chr_mDC2_G2': ['severe', 'mDC2', 'SARS', 15, 'bad-quality', , 'Cohorte 2'],
  #'BRU_Chr_mDC2_G3': ['severe', 'mDC2', 'Agonist', 15, 'bad-quality', , 'Cohorte 2'],

  'HOU_ED_mDC2_F1': ['severe', 'mDC2', 'Mock', 15, 'modeling', 1.01, 'Cohorte 3'],
  'HOU_ED_mDC2_F2': ['severe', 'mDC2', 'SARS', 15, 'modeling', 1.33, 'Cohorte 3'],
  'HOU_ED_mDC2_F3': ['severe', 'mDC2', 'Agonist', 15, 'modeling', 0.73, 'Cohorte 3'],
  'HOU_ED_mDC2_G1': ['severe', 'mDC2', 'Mock', 18, 'modeling', 1.52, 'Cohorte 3'],
  'HOU_ED_mDC2_G2': ['severe', 'mDC2', 'SARS', 18, 'modeling', 1.48, 'Cohorte 3'],
  'HOU_ED_mDC2_G3': ['severe', 'mDC2', 'Agonist', 18, 'modeling', 0.76, 'Cohorte 3'],
  'HOU_ED_mDC2_H1': ['severe', 'mDC2', 'Mock', 20, 'modeling', 1.0, 'Cohorte 3'],
  'HOU_ED_mDC2_H2': ['severe', 'mDC2', 'SARS', 20, 'modeling', 1.06, 'Cohorte 3'],
  'HOU_ED_mDC2_H3': ['severe', 'mDC2', 'Agonist', 20, 'modeling', 0.55, 'Cohorte 3'],

  #'FAY_Rob_mDC2_F1': ['severe', 'mDC2', 'Mock', 12, 'bad-quality', , 'Cohorte 4'],
  #'FAY_Rob_mDC2_F2': ['severe', 'mDC2', 'SARS', 12, 'bad-quality', , 'Cohorte 4'],
  #'FAY_Rob_mDC2_G1': ['severe', 'mDC2', 'Mock', 28, 'bad-quality', , 'Cohorte 4'],
  #'FAY_Rob_mDC2_G2': ['severe', 'mDC2', 'SARS', 28, 'bad-quality', , 'Cohorte 4'],
  #'FAY_Rob_mDC2_H1': ['severe', 'mDC2', 'Mock', 35, 'bad-quality', , 'Cohorte 4'],
  #'FAY_Rob_mDC2_H2': ['severe', 'mDC2', 'SARS', 35, 'bad-quality', , 'Cohorte 4'],

  #'OZBE_mDC2_G1': ['severe', 'mDC2', 'Mock', 16, 'bad-quality', , 'Cohorte 5'],
  #'OZBE_mDC2_G2': ['severe', 'mDC2', 'SARS', 16, 'bad-quality', , 'Cohorte 5'],
  'OZBE_mDC2_H1': ['severe', 'mDC2', 'Mock', 23, 'modeling', 4.33, 'Cohorte 5'],
  'OZBE_mDC2_H2': ['severe', 'mDC2', 'SARS', 23, 'modeling', 7.61, 'Cohorte 5'],
  #'OZBE_mDC2_I1': ['severe', 'mDC2', 'Mock', 30, 'modeling', , 'Cohorte 5'],
  #'OZBE_mDC2_I2': ['severe', 'mDC2', 'SARS', 30, 'modeling', , 'Cohorte 5'],

  #'RESU_mDC2_G1': ['severe', 'mDC2', 'Mock', 36, 'bad-quality', , 'Cohorte 6'],
  #'RESU_mDC2_G2': ['severe', 'mDC2', 'SARS', 36, 'bad-quality', , 'Cohorte 6'],
  #'RESU_mDC2_H1': ['severe', 'mDC2', 'Mock', 43, 'modeling', , 'Cohorte 6'],
  #'RESU_mDC2_H2': ['severe', 'mDC2', 'SARS', 43, 'modeling', , 'Cohorte 6'],
  #'RESU_mDC2_I1': ['severe', 'mDC2', 'Mock', 50, 'modeling', , 'Cohorte 6'],
  #'RESU_mDC2_I2': ['severe', 'mDC2', 'SARS', 50, 'modeling', , 'Cohorte 6'],

  'Hu3_1_mDC2_G1': ['healthy', 'mDC2', 'Mock', 1, 'modeling', 4.03, 'Cohorte 1'],
  'Hu3_1_mDC2_G2': ['healthy', 'mDC2', 'SARS', 1, 'modeling', 4.98, 'Cohorte 1'],
  'Hu3_1_mDC2_G3': ['healthy', 'mDC2', 'Agonist', 1, 'modeling', 8.0, 'Cohorte 1'],

  'Hu3_2_mDC2_H1': ['healthy', 'mDC2', 'Mock', 11, 'modeling', 3.55, 'Cohorte 2'],
  'Hu3_2_mDC2_H2': ['healthy', 'mDC2', 'SARS', 11, 'modeling', 4.06, 'Cohorte 2'],
  'Hu3_2_mDC2_H3': ['healthy', 'mDC2', 'Agonist', 11, 'modeling', 4.29, 'Cohorte 2'],

  'Hu3_3_mDC2_I1': ['healthy', 'mDC2', 'Mock', 25, 'modeling', 4.05, 'Cohorte 3'],
  'Hu3_3_mDC2_I2': ['healthy', 'mDC2', 'SARS', 25, 'modeling', 4.14, 'Cohorte 3'],
  'Hu3_3_mDC2_I3': ['healthy', 'mDC2', 'Agonist', 25, 'modeling', 5.16, 'Cohorte 3'],

  'Hu3_4_mDC2_I1': ['healthy', 'mDC2', 'Mock', 35, 'modeling', 5.53, 'Cohorte 4'],
  'Hu3_4_mDC2_I2': ['healthy', 'mDC2', 'SARS', 35, 'modeling', 5.87, 'Cohorte 4'],
  'Hu3_4_mDC2_I3': ['healthy', 'mDC2', 'Agonist', 35, 'modeling', 11.1, 'Cohorte 4'],

  'Hu3_5_mDC2_J1': ['healthy', 'mDC2', 'Mock', 50, 'modeling', 3.94, 'Cohorte 5'],
  'Hu3_5_mDC2_J2': ['healthy', 'mDC2', 'SARS', 50, 'modeling', 4.3, 'Cohorte 5'],
  'Hu3_5_mDC2_J3': ['healthy', 'mDC2', 'Agonist', 50, 'modeling', 7.27,'Cohorte 5'],

  'Hu3_6_mDC2_J1': ['healthy', 'mDC2', 'Mock', 8, 'modeling', 2.24, 'Cohorte 6'],
  #'Hu3_6_mDC2_J2': ['healthy', 'mDC2', 'SARS', 8, 'modeling', , 'Cohorte 6'],
  'Hu3_6_mDC2_J3': ['healthy', 'mDC2', 'SARS', 8, 'modeling', 4.37, 'Cohorte 6'],

  'HD_6M20_mDC2_H1': ['healthy', 'mDC2', 'Mock', 183, 'modeling', 3.27, 'Cohorte 1'],
  'HD_6M20_mDC2_H2': ['healthy', 'mDC2', 'SARS', 183, 'modeling', 3.75, 'Cohorte 1'],
  'HD_6M20_mDC2_H3': ['healthy', 'mDC2', 'Agonist', 183, 'modeling', 8.38, 'Cohorte 1'],

  'BC_HV2_mDC2_I1': ['healthy', 'mDC2', 'Mock', 14, 'modeling', 3.64, 'Cohorte 2'],
  'BC_HV2_mDC2_I2': ['healthy', 'mDC2', 'SARS', 14, 'modeling', 4.73, 'Cohorte 2'],
  'BC_HV2_mDC2_I3': ['healthy', 'mDC2', 'Agonist', 14, 'modeling', 5.04, 'Cohorte 2'],

  'BV_HV1_mDC2_J1': ['healthy', 'mDC2', 'Mock', 27, 'modeling', 4.0, 'Cohorte 3'],
  'BV_HV1_mDC2_J2': ['healthy', 'mDC2', 'SARS', 27, 'modeling', 4.84, 'Cohorte 3'],
  'BV_HV1_mDC2_J3': ['healthy', 'mDC2', 'Agonist', 27, 'modeling', 3.85, 'Cohorte 3'],

  'HV_29_mDC2_J1': ['healthy', 'mDC2', 'Mock', 37, 'modeling', 4.44, 'Cohorte 4'],
  'HV_29_mDC2_J2': ['healthy', 'mDC2', 'SARS', 37, 'modeling', 5.55, 'Cohorte 4'],
  'HV_29_mDC2_J3': ['healthy', 'mDC2', 'Agonist', 37, 'modeling', 4.83, 'Cohorte 4'],

  'HD_3M31_mDC2_K1': ['healthy', 'mDC2', 'Mock', 15, 'modeling', 3.74, 'Cohorte 5'],
  'HD_3M31_mDC2_K2': ['healthy', 'mDC2', 'SARS', 15, 'modeling', 3.64, 'Cohorte 5'],
  'HD_3M31_mDC2_K3': ['healthy', 'mDC2', 'Agonist', 15, 'modeling', 11.4, 'Cohorte 5'],

  'HD_EF9S_mDC2_K1': ['healthy', 'mDC2', 'Mock', 22, 'modeling', 3.18, 'Cohorte 6'],
  'HD_EF9S_mDC2_K2': ['healthy', 'mDC2', 'SARS', 22, 'modeling', 3.14, 'Cohorte 6'],
  'HD_EF9S_mDC2_K3': ['healthy', 'mDC2', 'Agonist', 22, 'modeling', 2.67, 'Cohorte 6'],

  #'HV_F23_mDC2_L1': ['healthy', 'mDC2', 'Mock', 30, 'modeling', , 'Cohorte 6'],
  #'HV_F23_mDC2_L2': ['healthy', 'mDC2', 'SARS', 30, 'modeling', , 'Cohorte 6'],

  'EFS_P1_0901_mDC2_3': ['healthy', 'mDC2', 'Mock', 43, 'modeling', 3.54, 'Pilote 1'],
  'EFS_P1_0901_mDC2_4': ['healthy', 'mDC2', 'SARS', 43, 'modeling', 4.13, 'Pilote 1'],
  'EFS_P1_0901_mDC2_5': ['healthy', 'mDC2', 'Agonist', 43, 'modeling', 5.37, 'Pilote 1'],

  #'EFS_P2_0901_mDC2_3': ['healthy', 'mDC2', 'Mock', 19, 'bad-quality', , 'Pilote 2'],
  #'EFS_P2_0901_mDC2_4': ['healthy', 'mDC2', 'SARS', 19, 'modeling', , 'Pilote 2'],
  #'EFS_P2_0901_mDC2_7': ['healthy', 'mDC2', 'Agonist', 19, 'modeling', , 'Pilote 2'],

  'EFS_P1_0930_mDC2_6': ['healthy', 'mDC2', 'Mock', 32, 'modeling', 2.49, 'Pilote 1'],
  'EFS_P1_0930_mDC2_7': ['healthy', 'mDC2', 'SARS', 32, 'modeling', 2.69, 'Pilote 1'],
  'EFS_P1_0930_mDC2_8': ['healthy', 'mDC2', 'Agonist', 32, 'modeling', 4.59, 'Pilote 1'],

  #'EFS_P2_1112_mDC2_8': ['healthy', 'mDC2', 'Mock', 4, 'modeling', , 'Pilote 2'],
  #'EFS_P2_1112_mDC2_9': ['healthy', 'mDC2', 'SARS', 4, 'modeling', , 'Pilote 2'],
  #'EFS_P2_1112_mDC2_12': ['healthy', 'mDC2', 'Agonist', 4, 'modeling', , 'Pilote 2']
}
