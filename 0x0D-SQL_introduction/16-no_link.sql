-- SQL INTRO 16
-- lists all records of second_table with a name
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
