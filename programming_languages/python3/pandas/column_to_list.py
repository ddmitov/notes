#!/usr/bin/env python3

import pandas as pd

# Column to list with only unique values and no NaNs:
item_list = dataframe['COLUMN'].nunique().tolist()
