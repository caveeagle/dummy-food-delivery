'''
What is the distribution of restaurants per location?
'''

import sqlite3

import geopandas as gpd
from shapely.geometry import Point


#########################################################

rows = []

with sqlite3.connect('../data/takeaway.sqlite') as conn:
    
    conn.row_factory = sqlite3.Row 

    cursor = conn.cursor()
    
    #####################
    
    cursor.execute('SELECT latitude AS lat, longitude AS lon FROM restaurants')
    
    rows = cursor.fetchall()
    
#########################################################
#########################################################

gdf_points = gpd.GeoDataFrame(
    rows,
    geometry=[Point(row["lon"], row["lat"]) for row in rows],
    crs="EPSG:4326"
)


#########################################################
#########################################################

gdf_map = gpd.read_file("../data/belgium_map.geojson")

if(1):
    
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 10))
    
    gdf_map.plot(
        ax=ax,
        color="lightgrey",
        edgecolor="black"
    )
    
    gdf_points.plot(
        ax=ax,
        color="red",
        markersize=5,
        alpha=0.6
    )
    
    ax.set_xlim(2.5, 6.4)
    ax.set_ylim(49.5, 51.6)
    
    ax.set_axis_off()
    plt.show()
    
    ax.set_title("Restaurants in Belgium")
    ax.set_axis_off()
    
    plt.show()    
    
#########################################################
#########################################################

print('Job finished')    
    
