#!/usr/bin/env python3

import pandas as pd

# Dataframe to a CSV File
dataframe.to_csv(
    'file.csv',
    encoding='utf-8',
    header=True,
    index=False,
    lineterminator='\n',
    sep=',',
    quotechar='"',
    escapechar='\\',
    quoting=1
)

# Dataframe to a CSV as a string:
import io

with io.StringIO() as csv_buffer:
    dataframe.to_csv(
        csv_buffer,
        encoding='utf-8',
        header=True,
        index=True
    )

    csv_bytes = csv_buffer.getvalue()

# Dataframe to a TSV file:
dataframe.to_csv(
    'file.tsv',
    sep='\t',
    encoding='utf-8',
    header=True
)

# Dataframe to a Parquet file:
dataframe.to_parquet(
    'file.parquet',
    compression='gzip'
)

# Single dataframe to an Excel file.
# 'openpyxl' or 'xlsxwriter' are implicit dependency.
dataframe.to_excel(
    'file.xlsx',
    sheet_name='Sheet-Name',
    index=False,
    header=True
)

# Many dataframes to many Worksheets of a single Excel file.
# 'openpyxl' or 'xlsxwriter' are implicit dependency.
dataframe_01 = None
dataframe_02 = None

writer = pd.ExcelWriter('file.xlsx')

dataframe_01.to_excel(writer, 'Sheet-01', index=False)
dataframe_02.to_excel(writer, 'Sheet-02', index=False)

writer.save()
