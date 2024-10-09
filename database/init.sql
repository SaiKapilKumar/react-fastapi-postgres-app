-- database/init.sql

-- Create the database 'customer_db_main'
CREATE DATABASE customer_db_main;

-- Create a user 'customer_user' with password 'customer_password'
CREATE USER customer_user WITH PASSWORD 'customer_password';

-- Grant all privileges on the database 'customer_db_main' to 'customer_user'
GRANT ALL PRIVILEGES ON DATABASE customer_db_main TO customer_user;

-- (Optional) Create extensions if needed
-- Connect to the database
\c customer_db_main

-- Uncomment the following line if you need the UUID extension
-- CREATE EXTENSION IF NOT EXISTS "uuid-ossp";