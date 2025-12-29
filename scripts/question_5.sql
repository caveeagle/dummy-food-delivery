
SELECT
    primarySlug,
    AVG(price) AS avg_price
FROM menuItems
GROUP BY primarySlug
ORDER BY avg_price DESC

###########################
###########################

SELECT
    r.*,
    t.avg_price
FROM restaurants r
LEFT JOIN (
    SELECT
        primarySlug,
        AVG(price) AS avg_price
    FROM menuItems
    GROUP BY primarySlug
) t
ON r.primarySlug = t.primarySlug;

###########################
###########################

SELECT
    r.*,
    t.avg_price,
    CASE
        WHEN r.ratings = 0 OR r.ratings IS NULL THEN NULL
        ELSE t.avg_price / r.ratings
    END AS price_per_rating
FROM restaurants r
LEFT JOIN (
    SELECT primarySlug, AVG(price) AS avg_price
    FROM menuItems
    GROUP BY primarySlug
) t
ON r.primarySlug = t.primarySlug
WHERE price_per_rating IS NOT NULL
ORDER BY price_per_rating;
LIMIT 1

###########################
###########################
