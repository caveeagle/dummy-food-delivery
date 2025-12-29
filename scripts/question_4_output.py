'''
Which are the top 10 pizza restaurants by rating?
'''
import math
import sqlite3

from tabulate import tabulate

#########################################################

with sqlite3.connect('../data/takeaway.sqlite') as conn:
    
    conn.row_factory = sqlite3.Row # ! IMPORTANT: set it before calling cursor()

    cursor = conn.cursor()
    
    query = """
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
    """

    cursor.execute(query)
    rows = cursor.fetchall()

#########################################################

table = [
    [
        row["name"],
        row["address"],
        round(row["avg_price"],0),
        round(math.sqrt(row["distance_km_sq"]), 2)
    ]
    for row in rows
]

print(tabulate(
    table,
    headers=["Name", "Address","Avg. price, Euro","Distance, km"],
    tablefmt="github"
))
#########################################################
#########################################################

print('Job finished')    
    
