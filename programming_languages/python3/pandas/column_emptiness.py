#!/usr/bin/env python3

import pandas as pd

# Check if a column is empty:
column_is_empty = dataframe['COLUMN'].isnull().all()

# Count all NaN elements in a column:
total_nan_column_elements = dataframe['COLUMN'].isna().sum()

# Zero-fill all NaN values only in some columns:
fill_values = {
    'COLUMN_01': 0,
    'COLUMN_02': 0
}

dataframe.fillna(
    value=fill_values,
    inplace=True
)

# Replace all empty strings in a single column:
dataframe['COLUMN'].replace(to_replace='', value=np.nan, inplace=True)

# Replace all empty strings in all columns:
for column in dataframe.columns:
    dataframe[column].replace(
        to_replace='',
        value=np.nan,
        inplace=True
    )
