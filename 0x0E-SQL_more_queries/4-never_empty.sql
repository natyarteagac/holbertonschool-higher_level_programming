-- script that creates the table id_not_null on your MySQL server.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NULL, name VARCHAR(256)
);
UPDATE id_not_null SET id = 1 WHERE id = NULL;
