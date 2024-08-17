#!/usr/bin/env python3

import pandas as pd

# Split one dataframe into a number of smaller dataframes:
# the number of rows per smaller dataframe
# depends on the size of the big dataframe and
# the number of smaller dataframes is fixed.

import numpy as np

number_of_parts = 10

partial_dataframes_list = np.array_split(dataframe, number_of_parts)

# Split one dataframe into a number of smaller dataframes:
# the number of rows per smaller dataframe is fixed and
# the number of smaller dataframes depends on
# the size of the original dataframe.

rows_per_part = 100

partial_dataframes_list = [
    dataframe[index : index + rows_per_part]
    for index in range(0, len(dataframe), rows_per_part)
]
