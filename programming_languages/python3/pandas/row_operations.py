#!/usr/bin/env python3

import pandas as pd

dataframe = None

# Drop all empty rows:
dataframe = dataframe.dropna(how='all')

# Insert a single row - technically adding a new dataframe:
columns = [
    'COLUMN_01',
    'COLUMN_02'
]

dataframe = pd.DataFrame(columns=columns)

column_01_value = 1234
column_02_value = 5678

dataframe = pd.concat(
    [
        dataframe,
        pd.DataFrame(
            {
                'COLUMN_01': column_01_value,
                'COLUMN_02': column_02_value
            }
        )
    ],
    ignore_index=True
)

# Iterate all rows:
for index, row in dataframe.iterrows():
    for column in row.iteritems():
        cell_heading = column[0]
        cell_value = column[1]
        print(cell_heading + ' : ' + cell_value)

# Apply function to all rows in a dataframe to produce a new column:
def totals_calculator(row):
    value_01 = int(row['COLUMN_01'])
    value_02 = int(row['COLUMN_02'])
    total = value_01 + value_02

    return total


dataframe['TOTAL'] = dataframe.apply(
    lambda row: totals_calculator(row),
    axis=1
)

# Show the duplicated rows in a dataframe:
column_list = None

duplicated_rows_dataframe = dataframe[
    dataframe.duplicated(
        ['COLUMN_01', 'COLUMN_02'],
        keep='first'
    )
]

# Dataframe rows to a list of dictionaries using a lambda function:
import json

json_list = dataframe.apply(
    lambda row: json.loads(row.to_json(force_ascii=False)),
    axis=1
).tolist()
