'''
What is the price distribution of menu items?
'''

import sqlite3

import pandas as pd
import matplotlib.pyplot as plt

#########################################################

prices = []

with sqlite3.connect('../data/takeaway.sqlite') as conn:
    
    conn.row_factory = sqlite3.Row # ! IMPORTANT: set it before calling cursor()

    cursor = conn.cursor()
    
    #####################
    
    cursor.execute('SELECT price FROM menuItems')
    
    for row in cursor:
        if row['price'] is not None:
            prices.append(float(row['price']))
        

print(f'Number of items:{len(prices)}')
    
#########################################################
#########################################################

df = pd.DataFrame(prices, columns=["price"])

mean_price = df["price"].mean()
median_price = df["price"].median()
min_price = df["price"].min()
max_price = df["price"].max()

# Mode:
mode_price = df["price"].mode().iloc[0]

summary = {
    "mean": mean_price,
    "median": median_price,
    "min": min_price,
    "max": max_price,
    "mode": mode_price
}

print("Summary statistics:")
print(f"Mean: {mean_price:.2f}")
print(f"Median: {median_price}")
print(f"Minimum: {min_price}")
print(f"Maximum: {max_price}")
print(f"Mode (peak value): {mode_price}")

min_price_non_zero = df.loc[df["price"] > 0, "price"].min()
print(f"Minimum (non-zero): {min_price_non_zero:.2f}")

#########################################################
#########################################################

if(1):
    
    N = 300
    
    max_value = 60
    
    plt.figure(figsize=(8, 5))
    plt.hist(df["price"], bins=N)
    plt.xlim(0, max_value)
    plt.xlabel("Price")
    plt.ylabel("Count")
    plt.title(f"Price distribution ({N} bins)")
    plt.tight_layout()
    plt.show()

#########################################################
#########################################################

print('Job finished')    
    
