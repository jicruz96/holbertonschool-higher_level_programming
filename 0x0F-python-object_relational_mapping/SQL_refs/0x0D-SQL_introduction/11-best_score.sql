-- SQL INTRO 11
-- Lists name and score of all records in second_table. Sorted by score
SELECT
    score, name
FROM
    second_table
WHERE
    score >= 10
ORDER BY
    score DESC;
