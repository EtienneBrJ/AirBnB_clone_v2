-- Script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'172.18.0.1' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'172.18.0.1';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'172.18.0.1';
