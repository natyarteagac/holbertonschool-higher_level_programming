-- script that creates the table unique_id on your MySQL server.
-- holberton school.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT NULL UNIQUE, name VARCHAR(256)
);
