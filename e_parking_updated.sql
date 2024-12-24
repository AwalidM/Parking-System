
CREATE DATABASE IF NOT EXISTS e_parking;

CREATE USER 'Amr2221'@'localhost' IDENTIFIED BY '0000';
GRANT ALL PRIVILEGES ON e_parking.* TO 'Amr2221'@'localhost';
FLUSH PRIVILEGES;

USE e_parking;

CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(40) NOT NULL UNIQUE,
    password VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL UNIQUE,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    date_joined DATETIME NOT NULL,
    last_login DATETIME
);

CREATE TABLE ParkingSlot (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40) NOT NULL UNIQUE,
    is_available BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE Reservation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    parking_slot_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (parking_slot_id) REFERENCES ParkingSlot(id) ON DELETE CASCADE
);
