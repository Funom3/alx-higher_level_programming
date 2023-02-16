-- Script that list all the records of the table second_table if name is not
-- NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
