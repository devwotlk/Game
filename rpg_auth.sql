-- Create the rpg_auth database (if you haven't created it yet)
CREATE DATABASE IF NOT EXISTS rpg_auth;

-- Use the rpg_auth database
USE rpg_auth;

-- Create the accounts table
CREATE TABLE IF NOT EXISTS accounts (
    acc_id INT AUTO_INCREMENT PRIMARY KEY,
    acc_name VARCHAR(80) NOT NULL,
    acc_password_hash VARCHAR(128) NOT NULL,
    acc_email VARCHAR(120) NOT NULL UNIQUE,
    creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);
