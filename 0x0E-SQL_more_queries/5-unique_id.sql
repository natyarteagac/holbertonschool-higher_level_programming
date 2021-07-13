-- script that creates the table unique_id on your MySQL server holberton school.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NULL DEFAULT UNIQUE, name VARCHAR(256)
);
