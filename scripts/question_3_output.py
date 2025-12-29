'''
Which are the top 10 pizza restaurants by rating?
'''

import sqlite3

from tabulate import tabulate

#########################################################

with sqlite3.connect('../data/takeaway.sqlite') as conn:
    
    conn.row_factory = sqlite3.Row # ! IMPORTANT: set it before calling cursor()

    cursor = conn.cursor()
    
    query = """
        SELECT DISTINCT r.*
        FROM restaurants r
        JOIN categories c
        	ON r.primarySlug = c.restaurant_id
        WHERE c.name LIKE '%pizza%'
        	AND r.ratingsNumber > 10
        ORDER BY ratings DESC
        LIMIT 10;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

#########################################################

table = [[row["name"], row["address"],row["city"]] for row in rows]

print(tabulate(
    table,
    headers=["Name", "Address","City"],
    tablefmt="github"
))
#########################################################
#########################################################

print('Job finished')    
    
