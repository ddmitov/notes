#!/usr/bin/env python3

import pandas as pd

# Sort dataframe by selected columns in ascending order:
dataframe.sort_values(
    by=[
        'COLUMN_01',
        'COLUMN_02'
    ],
    ascending=True,
    inplace=True
)

# Sort dataframe by selected columns in different orders
dataframe.sort_values(
    by=[
        'COLUMN_01',
        'COLUMN_02'
    ],
    ascending=[
        True,
        False
    ],
    inplace=True
)
