#!/usr/bin/env python3

import pandas as pd

dataframe = None

# Group by Date
aggregated_dataframe = (
    dataframe.groupby(
        dataframe['DATE'].dt.date,
        as_index=False
    ).agg(
        {
            'DATE': ['first'],
            'COLUMN_02': ['nunique'],  # number of non-null and unique values
            'COLUMN_03': ['sum']
        }
    )
).reset_index()

# 'first', 'nunique', 'sum'
aggregated_dataframe = (
    dataframe.groupby(
        [
            'COLUMN_01',
            'COLUMN_02'
        ]
    ).agg(
        {
            'COLUMN_03': ['first'],
            'COLUMN_04': ['nunique'],
            'COLUMN_05': ['sum']
        }
    )
).reset_index()

# Query, Group and Aggregation
dataframe.query(
    'COLUMN_01 == "filter"'
).groupby(
    ['COLUMN_02']
).agg(
    {'COLUMN_03': 'sum'}
)

# Aggregation with Standard and Custom Functions
def custom_agg_function(group):
    return_value = None
    # pandas.Series transformation code goes here.
    return return_value


aggregated_dataframe = (
    dataframe.groupby(
        [
            'COLUMN_01'
        ]
    ).agg(
        {
            'COLUMN_02': ['nunique'],
            'COLUMN_03': ['count'],
            'COLUMN_03': [custom_agg_function, 'min', 'mean', 'max']
        }
    )
).reset_index()

# Aggregation with 'min', 'mean' and 'max' Time Intervals between Events
# 'TIMESTAMP_COLUMN' is of the 'datetime64' type.                       


def custom_min(group_series):
    return group_series.sort_values().diff().min()


def custom_mean(group_series):
    return group_series.sort_values().diff().mean().round('1s')


def custom_max(group_series):
    return group_series.sort_values().diff().max()


aggregated_dataframe = (
    dataframe.groupby(
        [
            'COLUMN_01',
            'COLUMN_02'
        ]
    ).agg(
        {
            'COLUMN_03': ['nunique'],
            'COLUMN_04': ['sum'],
            'TIMESTAMP_COLUMN': [
                custom_min,
                custom_mean,
                custom_max
            ]
        }
    )
).reset_index()

# Pandas Analogs of the GROUP_CONCAT() MySQL Function
aggregated_dataframe = (
    dataframe
    .groupby(
        [
            'COLUMN_01',
            'COLUMN_02',
        ]
    ).agg(
        {
            'GROUP_CONCAT_COLUMN': lambda values: ', '.join(
                sorted(set(values))
            )
        }
    )
).reset_index()

aggregated_dataframe = (
    dataframe.groupby(
        ['COLUMN_01']
    ).agg(
        {
            'COLUMN_02': ['first'],
            'COLUMN_03': ['count'],
            'COLUMN_04': ['sum'],
            'COLUMN_05': ['nunique'],
            # Join together with comma and space only        
            # sorted and unique values having non-zero length
            # using lambda function and list comprehension:  
            'GROUP_CONCAT_COLUMN': lambda values: ', '.join(
                sorted(
                    set(
                        value for value in values if len(value) > 0)
                    )
                )
        }
    )
).reset_index()

# Count All Elements of an Aggregation Matching Given Criteria
aggregated_dataframe = (
    dataframe.groupby(
        ['COLUMN_01']
    )['COLUMN_02'].apply(
        lambda values: len(
            set(value for value in values if len(value) > 0)
        )
    )
).reset_index()

# Mont-by-Month Pivot Dataframe
dataframe['MONTH'] = (
    pd
    .to_datetime(dataframe['DATE'])
    .dt.to_period('M')
)

pivot_dataframe = pd.pivot_table(
    dataframe,
    index='INDEX_COLUMN',
    columns='MONTH',
    values='VALUE_COLUMN',
    aggfunc='sum',
    margins=True,
    margins_name='TOTAL_VALUES',
    fill_value=0
)

pivot_dataframe.columns = (
    pivot_dataframe.columns.get_level_values(0)
)

# Convert MultiIndex to Regular Columns:
pivot_dataframe.reset_index(inplace=True)

# Week-by-Week Pivot Dataframe with MultiIndex
dataframe['WEEK'] = (
    pd
    .to_datetime(dataframe['DATE'])
    .dt.to_period(freq='W')  # e.g. 2021-01-04/2021-01-10
)

dataframe['WEEK'] = (
    pd
    .to_datetime(dataframe['DATE'])
    .dt.isocalendar().week  # e.g. 1, 2 ... 52, 53
)

pivot_dataframe = pd.pivot_table(
    dataframe,
    index=[
        'INDEX_COLUMN_01',
        'INDEX_COLUMN_02'
    ],
    columns='WEEK',
    values='VALUE_COLUMN',
    aggfunc='sum',
    margins=True,
    margins_name='TOTAL_VALUES',
    fill_value=0
)

pivot_dataframe.columns = (
    pivot_dataframe.columns.get_level_values(0)
)

pivot_dataframe = (
    pivot_dataframe.reset_index()  # convert MultiIndex to Regular Columns
)

# Mont-by-Month Pivot Dataframe with
# MultiIndex and Two Value Columns to Aggregate
pivot_dataframe = pd.pivot_table(
    dataframe,
    index=[
        'INDEX_COLUMN_01',
        'INDEX_COLUMN_02'
    ],
    columns='MONTH',
    values=[
        'VALUE_COLUMN_01',
        'VALUE_COLUMN_02'
    ],
    aggfunc='sum',
    margins=True,
    margins_name='TOTAL_VALUES',
    fill_value=0
)

# Flatten MultiIndex Pivot Dataframe before Excel File Generation
pivot_dataframe.columns = pivot_dataframe.columns.get_level_values(1)

pivot_dataframe = pivot_dataframe.reset_index()
