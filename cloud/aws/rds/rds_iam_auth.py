#!/usr/bin/env python3

import boto3
import pymysql

# Get token:
client = boto3.client(
    'rds',
    region_name='region'
)

token = client.generate_db_auth_token(
    'test.something.region.rds.amazonaws.com',
    3306,
    'username'
)

# Define SSL certificate:
ssl = {
    'ca': 'rds-combined-ca-bundle.pem'
}

# Connect to the database:
connection = pymysql.connect(
    host='test.something.region.rds.amazonaws.com',
    port=3306,
    user='username',
    password=token,
    ssl=ssl
)

# Execute a testing query:
query = 'SHOW DATABASES;'

cursor = connection.cursor()

cursor.execute(query)
database_data = cursor.fetchall()
connection.close()

for database in database_data:
    print(database[0])
