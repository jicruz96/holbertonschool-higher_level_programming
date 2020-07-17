-- Subquery
-- lists all California cities found in hbtn_0d_usa database
SELECT id, name
FROM  cities
WHERE state_id IN (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
