#!/usr/bin/env python3

import pandas as pd

# Set a column as index:
dataframe.set_index('COLUMN')

# Insert a new column with a value or
# assign a value to all elements of an existing column:
dataframe['COLUMN'] = 'value'

# Set column type:
dataframe['COLUMN'] = dataframe['COLUMN'].astype(int)

dataframe = dataframe.astype(
    {
        'COLUMN_01': 'int64',
        'COLUMN_02': 'int64'
    }
)

# Drop duplicates in a column:
dataframe.drop_duplicates(
    subset='COLUMN',
    keep=False,
    inplace=True
)

# Reorder columns:
dataframe = dataframe[
    list(
        (
            'COLUMN_01',
            'COLUMN_02'
        )
    )
]

# Replace a substring in a column using a regular expression:
dataframe['COLUMN'] = (
    dataframe['COLUMN'].str.replace(
        'regex',
        '',
        regex=True
    )
)

# Change one column based on another column:
dataframe.loc[
    dataframe['CRITERION_COLUMN'] == 'keyword',
    ['COLUMN_THAT_HAS_TO_BE_CHANGED']
] = 'new value'

# Create a pandas timestamp column from a string column:
dataframe['TIMESTAMP_COLUMN'] = (
    pd.to_datetime(
        dataframe['STRING_COLUMN'],
        infer_datetime_format=True
    )
)

# Drop column:
dataframe = dataframe.drop(['COLUMN'], axis=1)
