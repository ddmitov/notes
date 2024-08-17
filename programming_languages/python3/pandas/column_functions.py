#!/usr/bin/env python3

import pandas as pd

# Apply a lambda function to a column:
dataframe['COLUMN'] = (
    dataframe['COLUMN'].apply(
        lambda value: round(value, 0)
    )
)

# Apply a named function to a column:
def multiplier(value, multiplier):
    final_value = value * multiplier

    return final_value


dataframe['COLUMN'] = (
    dataframe['COLUMN']
    .apply(lambda value: multiplier(value, 5))
)
