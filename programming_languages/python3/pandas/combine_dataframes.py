#!/usr/bin/env python3

import pandas as pd

# Merge a list of dataframes on their index:
dataframes_list = None

combined_dataframe = pd.concat(dataframes_list, axis=1)

# Merge one after the other identical dataframes:
combined_dataframe = pd.concat(
    [
        dataframe_01,
        dataframe_02
    ],
    ignore_index=True
)

combined_dataframe.reset_index()

# Left join of different dataframes on a column with common elements:
combined_dataframe = pd.merge(
    dataframe_01,
    dataframe_02,
    on='COLUMN_WITH_COMMON_VALLUES',
    how='left'
)

combined_dataframe = combined_dataframe.merge(
    dataframe_02,
    on='COLUMN_WITH_COMMON_VALLUES',
    how='left'
)

# Left join of different dataframes on several columns with common elements:
combined_dataframe = pd.merge(
    dataframe_01,
    dataframe_02,
    how='left',
    left_on=[
        'COLUMN_WITH_COMMON_VALLUES_01',
        'COLUMN_WITH_COMMON_VALLUES_02',
        'COLUMN_WITH_COMMON_VALLUES_03'
    ],
    right_on=[
        'COLUMN_WITH_COMMON_VALLUES_01',
        'COLUMN_WITH_COMMON_VALLUES_02',
        'COLUMN_WITH_COMMON_VALLUES_03'
    ]
)

combined_dataframe = pd.merge(
    dataframe_01,
    dataframe_02,
    how='left',
    on=[
        'COLUMN_WITH_COMMON_VALLUES_01',
        'COLUMN_WITH_COMMON_VALLUES_02',
        'COLUMN_WITH_COMMON_VALLUES_03'
    ]
)

# Inner join of different dataframes on a column with common elements:
combined_dataframe = pd.merge(
    dataframe_01,
    dataframe_02,
    on='COLUMN_WITH_COMMON_VALLUES',
    how='inner'
)

# Combine two dataframes by
# filling the NaN elements in the first dataFrame
# with the non-NaN elements from the second dataframe:
dataframe_01.combine_first(dataframe_02)

# Combine two dataframes by
# replacing columns in the first dataframe
# with the same columns from the second dataframe:
dataframe_01.update(dataframe_02)
