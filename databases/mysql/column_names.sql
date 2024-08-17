-- Find column by partial name:
SELECT
    TABLE_NAME,
    COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'SCHEMA_NAME'
    AND COLUMN_NAME LIKE '%COLUMN_NAME%';

-- Show all columns in a table:
DESCRIBE SCHEMA_NAME.TABLE_NAME;
SHOW COLUMNS FROM SCHEMA_NAME.TABLE_NAME;
