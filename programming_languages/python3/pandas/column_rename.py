#!/usr/bin/env python3

import pandas as pd

# Rename selected columns:
dataframe.rename(
    {
        'COLUMN_01': 'COLUMN_01_NEW',
        'COLUMN_02': 'COLUMN_02_NEW'
    },
    axis=1,
    inplace=True
)

# Rename all columns:
dataframe.columns = [
    'COLUMN_01_NEW',
    'COLUMN_02_NEW',
    'COLUMN_03_NEW'
]
