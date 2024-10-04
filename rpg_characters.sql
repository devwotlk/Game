-- Create the rpg_characters database
CREATE DATABASE IF NOT EXISTS rpg_characters;

-- Use the rpg_characters database
USE rpg_characters;

-- Create the characters table
CREATE TABLE IF NOT EXISTS characters (
    char_id INT AUTO_INCREMENT PRIMARY KEY,          -- Character ID, primary key
    acc_id INT NOT NULL,                             -- Account ID (Foreign key in practice)
    name VARCHAR(100) NOT NULL,                      -- Character name
    class VARCHAR(50) NOT NULL,                      -- Character class (e.g., warrior, mage, etc.)
    gender TINYINT(1) NOT NULL,                      -- Gender: 0 for male, 1 for female
    level INT DEFAULT 1,                             -- Character level, default starting level is 1
    xp BIGINT DEFAULT 0,                             -- Experience points, default 0
    money BIGINT DEFAULT 0,                          -- In-game currency, default 0
    online TINYINT(1) DEFAULT 0,                     -- Online status: 0 for offline, 1 for online
    last_login DATETIME DEFAULT CURRENT_TIMESTAMP,   -- Last login date, default is current timestamp
    time_played BIGINT DEFAULT 0,                    -- Total time played in seconds, default 0
    FOREIGN KEY (acc_id) REFERENCES accounts(acc_id) -- Foreign key to the accounts table
);
