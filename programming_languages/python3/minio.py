#! /usr/bin/env python3

import os
from   pathlib import Path
from   minio   import Minio

# MinIO client:
minio_local_client = Minio(
    'minio:9000',
    access_key = os.environ['LOCAL_ACCESS_KEY_ID'],
    secret_key = os.environ['LOCAL_SECRET_ACCESS_KEY'],
    secure     = False
)

# Create bucket if it does not exist:
if not minio_local_client.bucket_exists('BUCKET'):
    minio_local_client.make_bucket('BUCKET')


# Object storage file cleaner:
def file_cleaner(
    client:      Minio,
    bucket_name: str,
    prefix:      str
) -> True:
    files_to_delete = client.list_objects(
        bucket_name,
        prefix    = prefix,
        recursive = True
    )

    for file_object in files_to_delete:
        client.remove_object(bucket_name, file_object.object_name)

        print(str(file_object.object_name), flush=True)

    return True


def file_uploader(
    object_storage_client: Minio,
    bucket_name:           str,
    prefix:                str,
    root_directory:        str,
    file_paths:            list
) -> True:
    file_number = 0

    for file_path in file_paths:
        file_number += 1

        object_name = str(file_path).replace(f'{root_directory}/', '')

        try:
            object_storage_client.fput_object(
                bucket_name,
                prefix + '/' + object_name,
                file_path,
                part_size = 100 * 1024 * 1024 # 100 MB
            )

            message = (
                f'{str(file_number)}/{str(len(file_paths))} - {object_name}'
            )

            print(message, flush=True)

        except Exception as exception:
            print(exception, flush=True)

    return True
