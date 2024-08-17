-- Get the SERVER_ID number:
SELECT @@SERVER_ID;

-- Check BINLOG settings:
SHOW GLOBAL VARIABLES LIKE 'log_bin';
SHOW GLOBAL VARIABLES LIKE 'binlog_format';

-- Get the BINLOG sequence number (LSN):
SHOW MASTER STATUS;
