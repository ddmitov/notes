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

# Convert a PyArrow table column to list:
python_list = arrow_table.column('column_name').to_pylist()

# Convert a list to a PyArrow table column:
new_arrow_table = arrow_table.set_column(
    3, # column number starting from zero
    'column_name',
    pa.array(python_list)
)
