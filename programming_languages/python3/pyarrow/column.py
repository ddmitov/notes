#!/usr/bin/env python3

# Append a new column with one unique value to a PyArrow table:
import pyarrow as pa

column_value = 42

arrow_table = arrow_table.append_column(
    'column_name',
    pa.array([column_value] * arrow_table.num_rows, pa.int64())
)

# Drop a column from a PyArrow table:
import pyarrow

pyarrow_table = pyarrow_table.drop(['COLUMN'])
