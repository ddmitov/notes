#! /usr/bin/env python3

from minio import Minio


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
