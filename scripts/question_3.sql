SELECT restaurant_id FROM categories WHERE name LIKE '%pizza%'

#######################
#######################

SELECT DISTINCT r.*
FROM restaurants r
JOIN categories c
  ON r.primarySlug = c.restaurant_id
WHERE c.name LIKE '%pizza%';

#######################
#######################

SELECT DISTINCT r.*
FROM restaurants r
JOIN categories c
	ON r.primarySlug = c.restaurant_id
WHERE c.name LIKE '%pizza%'
	AND r.ratingsNumber > 10
ORDER BY ratings DESC
LIMIT 10;

