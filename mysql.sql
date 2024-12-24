CREATE DATABASE IF NOT EXISTS e_parking;

-- Create user and grant permissions
CREATE USER IF NOT EXISTS 'Amr2221'@'localhost' IDENTIFIED BY '0000';
GRANT ALL PRIVILEGES ON e_parking.* TO 'Amr2221'@'localhost';
FLUSH PRIVILEGES;

-- Use the database
USE e_parking;

-- Create the User table
CREATE TABLE IF NOT EXISTS User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(40) NOT NULL UNIQUE,
    password VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL UNIQUE,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    date_joined DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Default value added
    last_login DATETIME DEFAULT NULL -- Allows NULL values for last login
);

-- Create the ParkingSlot table
CREATE TABLE IF NOT EXISTS ParkingSlot (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40) NOT NULL UNIQUE,
    is_available BOOLEAN NOT NULL DEFAULT TRUE -- Default value ensures availability
);

-- Create the Reservation table
CREATE TABLE IF NOT EXISTS Reservation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    parking_slot_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE, -- Ensures cleanup of reservations if user is deleted
    FOREIGN KEY (parking_slot_id) REFERENCES ParkingSlot(id) ON DELETE CASCADE -- Ensures cleanup of reservations if slot is deleted
);

-- Verify user creation
SELECT User, Host FROM mysql.user WHERE User = 'Amr2221';

-- Ensure permissions are applied
GRANT ALL PRIVILEGES ON e_parking.* TO 'Amr2221'@'localhost';
FLUSH PRIVILEGES;
