#!/usr/bin/env python3

import pandas as pd

# Count all column rows:
total_column_elements = dataframe['COLUMN'].count()

# Count all occurences of a selected column element:
number_of_elements = dataframe[dataframe['COLUMN'] == 'criterion'].shape[0]
