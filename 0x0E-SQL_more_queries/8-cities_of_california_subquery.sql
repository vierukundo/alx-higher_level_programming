-- 8-cities_of_california_subquery.sql
-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- You are not allowed to use the JOIN keyword
SELECT id, name
FROM cities
WHERE state_id = 
(
	SELECT id
	FROM states
	WHERE name = "California"
)
ORDER BY id ASC;
