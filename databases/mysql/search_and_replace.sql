UPDATE TABLE_NAME
SET COLUMN_NAME = REPLACE(
    COLUMN_NAME,
    'STRING_TO_FIND',
    'STRING_TO_REPLACE'
)
WHERE COLUMN_NAME LIKE '%STRING_TO_FIND%';
