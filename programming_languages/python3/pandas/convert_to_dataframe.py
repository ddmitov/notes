#!/usr/bin/env python3

import pandas as pd

# Empty dataframe from code:
dataframe_columns = [
    'COLUMN_01',
    'COLUMN_02'
]

dataframe = pd.DataFrame(columns=dataframe_columns)

# Non-empty dataframe from code:
dataframe = pd.DataFrame(
    {
        'COLUMN_01': ['One', 'Two'],
        'COLUMN_02': [1, 2]
    }
)

# Dataframe from the results of a MySQL query:
import pymysql

db_connection = pymysql.connect(
    host='HOST',
    user='USER',
    passwd='PASSWORD',
    database='DATABASE'  # optional
)

query = '''
    SELECT column
    FROM database.table;
'''

dataframe = pd.read_sql(
    query,
    db_connection
)

# Sequence of dataframes from the results of a MySQL query:
import pymysql

CHUNK_SIZE = 100

db_connection = pymysql.connect(
    host='',
    user='',
    passwd='',
    database=''
)

query = '''
    SELECT column
    FROM database.table;
'''

for partial_dataframe in pd.read_sql(query, db_connection, chunksize=CHUNK_SIZE):
    print(partial_dataframe.head())

# Dataframe from a CSV file:
dataframe = pd.read_csv(
    'data_file.csv',
    index_col=0,
    header=0
)

# Dataframe from a TSV file:
dataframe = pd.read_csv(
    'data_file.tsv',
    sep='\t',
    index_col=0,
    header=0
)

# Dataframe from an NDJSON file:
dataframe = pd.read_json(
    'ndjson_filepath',
    encoding='utf-8',
    lines=True,
    engine='pyarrow'
)

# Dataframe from an Excel file:
dataframe = pd.read_excel(
    'data_file.xlsx',
    sheet_name='Sheet1',
    usecols=[
        'COLUMN_NAME_01',
        'COLUMN_NAME_02'
    ]
)

# Dataframe from a Parquet file:
dataframe = pd.read_parquet('data_file.parquet.gz')
