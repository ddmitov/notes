#!/usr/bin/env python3

import pandas as pd

# Extract one dataframe as a subset of another dataframe:
subset_dataframe = dataframe[['COLUMN_01', 'COLUMN_02']]

# Extract one dataframe from another using equality operators:
criterion_01 = 'criterion_01'
criterion_02 = 'criterion_02'

extracted_dataframe = dataframe[dataframe['COLUMN'] == 'CRITERION']

extracted_dataframe = dataframe[
    (dataframe['COLUMN'] == 'CRITERION_01') |
    (dataframe['COLUMN'] == 'CRITERION_02')
]

extracted_dataframe = dataframe.loc[
    (dataframe['CRITERION_COLUMN_01'] == criterion_01) &
    (dataframe['CRITERION_COLUMN_02'] < criterion_02),
    [
        'WANTED_COLUMN_01',
        'WANTED_COLUMN_02'
    ]
]

# Extract one dataframe from another using regular expression on a column:
search_mask = dataframe[['COLUMN']].apply(
    lambda x: x.str.contains(
        'regex_expression',
        regex=True
    )
).any(axis=1)

results_dataframe = dataframe[search_mask]

# Extract one dataframe from another using string keyword search in a column:
extracted_dataframe = dataframe.loc[
    dataframe['CRITERION_COLUMN'].str.contains(
        'CRITERION_KEYWORD',
        regex=False
    ),
    [
        'WANTED_COLUMN_01',
        'WANTED_COLUMN_02'
    ]
]

# Extract one dataframe from another based on criteria list:
original_dataframe = None

criterion_list = ['criterion_01', 'criterion_01']

extracted_dataframe = original_dataframe.loc[
    (original_dataframe['CRITERION_COLUMN'].isin(criterion_list)),
    [
        'WANTED_COLUMN_ONE',
        'WANTED_COLUMN_TWO'
    ]
]

# Positive filter set:
filter_set = set([1, 2, 3])

filtered_dataframe = dataframe[dataframe['score'].isin(filter_set)]

# Negative filter set:
filter_set = set([1, 2, 3])

filtered_dataframe = dataframe[dataframe['score'].isin(filter_set) == False]

# Extract single element value based on the value of another element:
criterion_value = None

wanted_value = dataframe.loc[
    dataframe['CRITERION_COLUMN'] == criterion_value,
    'WANTED_COLUMN'
].iloc[0]
