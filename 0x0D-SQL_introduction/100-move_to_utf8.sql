-- Script to convert the database hbtn_0c_0 and its components to UTF8 (utf8mb4, utf8mb4_unicode_ci)
-- This includes the database, table first_table, and field name in first_table

-- Convert the database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Use the database to ensure subsequent commands apply
USE hbtn_0c_0;

-- Convert the table first_table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field in first_table to UTF8
ALTER TABLE first_table
MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
