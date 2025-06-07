-- Create database
CREATE DATABASE IF NOT EXISTS alagappa_db;
USE alagappa_db;
-- Table for student registrations
CREATE TABLE registrations (
    reg_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    course_id VARCHAR(50) NOT NULL,
    gender VARCHAR(10),
    phone_number VARCHAR(15),
    Aadhar_no VARCHAR(12),

    Tamil INT,
    English INT,
    CS_Bio INT,
    Mathematics INT,
    Chemistry INT,
    Physics INT,

    cutoff INT
);


-- Table for admin login
CREATE TABLE IF NOT EXISTS admins (
  admin_id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(100) NOT NULL
);

-- Sample admin (email: admin@alagappa.edu, password: admin123)
INSERT INTO admins (email, password) VALUES ('admin@alagappa.edu', 'admin123');

select *from registrations;
drop table registrations;
