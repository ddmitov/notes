#!/usr/bin/env python3

# Parquet file from a PyArrow table:
import pyarrow.parquet as pq

pq.write_table(
    pyarrow_table,
    'data.parquet',
    compression_level=None
)

# Write a PyArrow dataset from a PyArrow table or
# append data to an existing dataset:
from datetime import datetime

pyarrow_table = pa.Table.from_pandas(pandas_dataframe)

unique_ids = len(pandas_dataframe['id'].nunique().tolist())

date_time_now = datetime.now()
date_time_string = (date_time_now.strftime('%Y-%m-%d--%H-%M-%S').strip())

pq.write_to_dataset(
    pyarrow_table,
    filesystem=minio,
    root_path=f'{bucket}/prefix',
    partitioning=['id'],
    basename_template='part-{{i}}--{}.parquet'.format(date_time_string),
    existing_data_behavior='overwrite_or_ignore',
    max_partitions=unique_ids
)
