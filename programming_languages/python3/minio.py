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
