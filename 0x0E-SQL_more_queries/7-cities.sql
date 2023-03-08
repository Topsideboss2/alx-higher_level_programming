-- Script that creates a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa; -- Query to create a database
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities ( -- Query to create cities in hbtn_0d_usa database
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	PRIMARY KEY (id), FOREIGN KEY (state_id) REFERENCES states(id));
