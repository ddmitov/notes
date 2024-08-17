CREATE USER 'username' IDENTIFIED WITH AWSAuthenticationPlugin as 'RDS';
GRANT ALL PRIVILEGES ON test.* TO 'username'@'%';
GRANT SELECT ON *.* TO 'username'@'%';
FLUSH PRIVILEGES;

SHOW GRANTS FOR 'username';
