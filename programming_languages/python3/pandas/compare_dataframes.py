#!/usr/bin/env python3

import pandas as pd

# Compare two dataframes for equality:
dataframes_equality_boolean = dataframe_01.equals(dataframe_02)

# Get the differences between two dataframes:
comparison_dataframe = dataframe_01.compare(
    dataframe_02,
    align_axis=0
)
