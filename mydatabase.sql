CREATE DATABASE IF NOT EXISTS mydatabase;

USE mydatabase;

CREATE TABLE Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(1000) NOT NULL,
    apellido VARCHAR(1000) NOT NULL,
    email VARCHAR(1000) NOT NULL UNIQUE,
    passwordd VARCHAR(1000) NOT NULL
);

INSERT INTO Usuario (nombre, apellido, email, passwordd)
VALUES ('maria', 'andrade', 'marandrade@gmail.com', 'marmarmar');

SELECT * FROM Usuario;

CREATE USER 'maria'@'localhost' IDENTIFIED BY '111';
GRANT ALL PRIVILEGES ON mydatabase.* TO 'maria'@'localhost';
FLUSH PRIVILEGES;

drop database mydatabase;
drop user 'maria'@'localhost';