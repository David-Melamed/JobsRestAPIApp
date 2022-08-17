-- create database
CREATE DATABASE IF NOT EXISTS BookJobsApplication;

-- create the user
CREATE USER 'admin' IDENTIFIED BY 'password';
GRANT CREATE, ALTER, INDEX, LOCK TABLES, REFERENCES, UPDATE, DELETE, DROP, SELECT, INSERT ON `BookJobsApplication`.* TO 'admin'@'%';

FLUSH PRIVILEGES;