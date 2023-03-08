-- Script that creates a user in MySql server
-- Query to create the user 'user_0d_1' in MySQL server
CREATE USER IF NOT EXISIS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1' @'localhost';
