#!/bin/sh

aws rds generate-db-auth-token \
--hostname test.something.region.rds.amazonaws.com \
--port 3306 \
--username username

mysql \
--host=test.something.region.rds.amazonaws.com \
--port=3306 \
--enable-cleartext-plugin \
--user=username \
--password='token'
