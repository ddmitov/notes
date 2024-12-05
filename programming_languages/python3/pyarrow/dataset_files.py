#!/usr/bin/env python3

# List all files in a PyArrow dataset under a prefix:
import pyarrow.fs as fs

paths = []

parquet_dataset_filesystem = fs.S3FileSystem(
    endpoint_override=os.environ['ENDPOINT_S3'],
    access_key=os.environ['ACCESS_KEY_ID'],
    secret_key=os.environ['SECRET_ACCESS_KEY'],
    scheme='http'
)

file_selector = fs.FileSelector(
    f'{bucket}/prefix',
    allow_not_found=True,
    recursive=True
)

for entry in parquet_dataset_filesystem.get_file_info(file_selector):
    if entry.type == fs.FileType.File:
        paths.append(entry.path)
