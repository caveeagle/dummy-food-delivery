#######################
#######################

SELECT DISTINCT r.*
FROM restaurants r
JOIN categories c
  ON r.primarySlug = c.restaurant_id
WHERE c.name LIKE '%sushi%';

#######################
#######################

SELECT
    r.*,
    m.avg_price
FROM restaurants r
JOIN (
    SELECT
        it.primarySlug,
        AVG(it.price) AS avg_price
    FROM menuItems it
    WHERE it.primarySlug IN (
        SELECT DISTINCT restaurant_id
        FROM categories
        WHERE name LIKE '%sushi%'
    )
    GROUP BY it.primarySlug
) m
ON r.primarySlug = m.primarySlug;

#######################
#######################

SELECT
    r.*,
    (
        ( (r.latitude  - 51.048) * 111.0 ) *
        ( (r.latitude  - 51.048) * 111.0 ) +
        ( (r.longitude - 3.73)   * 111.0 * 0.63 ) *
        ( (r.longitude - 3.73)   * 111.0 * 0.63 )
    ) AS distance_km_sq
FROM restaurants r
WHERE distance_km_sq <1
ORDER BY distance_km_sq

# Gent Zuid = 51.048, 3.73
# SQLite does not provide the SQRT() function !

#######################
#######################

SELECT
    r.*,
    m.avg_price,
    (
        ( (r.latitude  - 51.048) * 111.0 ) *
        ( (r.latitude  - 51.048) * 111.0 ) +
        ( (r.longitude - 3.73)   * 111.0 * 0.63 ) *
        ( (r.longitude - 3.73)   * 111.0 * 0.63 )
    ) AS distance_km_sq
FROM restaurants r
JOIN (
    SELECT
        it.primarySlug,
        AVG(it.price) AS avg_price
    FROM menuItems it
    WHERE it.primarySlug IN (
        SELECT DISTINCT restaurant_id
        FROM categories
        WHERE name LIKE '%sushi%'
    )
    GROUP BY it.primarySlug
) m
ON r.primarySlug = m.primarySlug
WHERE
    (
        ( (r.latitude  - 51.048) * 111.0 ) *
        ( (r.latitude  - 51.048) * 111.0 ) +
        ( (r.longitude - 3.73)   * 111.0 * 0.63 ) *
        ( (r.longitude - 3.73)   * 111.0 * 0.63 )
    ) < 1
ORDER BY distance_km_sq;

#######################
#######################



