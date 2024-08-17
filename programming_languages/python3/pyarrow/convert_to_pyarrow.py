#!/usr/bin/env python3

# PyArrow table from a Parquet dataset in object storage:
import pyarrow.fs as fs
import pyarrow.parquet as pq

s3_filesystem = fs.S3FileSystem()

pandas_dataframe = pq.ParquetDataset(
    parquet_pathname_list,
    filesystem=s3_filesystem,
    filters=[
        # Logical AND:
        ('COLUMN_01', '==', 'string_criteria_01'),
        ('COLUMN_02', 'in', criteria_list_01),
        ('COLUMN_03', 'not in', criteria_list_02)
        # Logical OR:
        [('COLUMN_04', '==', 'string_criteria_02')],
        [('COLUMN_05', '==', 'string_criteria_03')]
    ]
).read(
    columns=[
        'COLUMN_01',
        'COLUMN_02',
        'COLUMN_03',
        'COLUMN_04',
        'COLUMN_05'
    ],
    use_threads=True
)

# PyArrow table from a Parquet file in object storage:
import pyarrow.fs as fs
import pyarrow.parquet as pq

s3_filesystem = fs.S3FileSystem()

pyarrow_table = pq.read_table(
    filename,
    filesystem=s3_filesystem
)

# PyArrow table from a NDJSON file:
import pyarrow

pyarrow_table = pyarrow.json.read_json(
    processed_ndjson_filepath,
    parse_options=pyarrow.json.ParseOptions(
        newlines_in_values=True
    )
)

# PyArrow table from a pandas dataframe:
import pyarrow as pa

pyarrow_fields = [
    pa.field('COLUMN_01', pa.date32()),
    pa.field('COLUMN_02', pa.string()),
    pa.field('COLUMN_03', pa.int64()),
    pa.field('COLUMN_04', pa.float64()),
    pa.field('COLUMN_05', pa.timestamp('us'))
]

pyarrow_schema = pa.schema(pyarrow_fields)
# or
pyarrow_schema = pa.Schema.from_pandas(pandas_dataframe)

pyarrow_table = pa.Table.from_pandas(
    pandas_dataframe,
    schema=pyarrow_schema,
    preserve_index=False
)
