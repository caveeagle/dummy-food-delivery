# STAR

## 1. Situation

We had a database of restaurants and menus stored in SQLite.  
As part of an analytical task, we needed to answer a set of business questions, some of which required spatial analysis.

### 1a. Problems

However, SQLite does not provide built-in support for geospatial data or spatial operations.  
In addition, there was no database description, and the graphical schema of table relationships contained errors.

## 2. Task

Initially, it was necessary to analyze the database structure and understand which tables corresponded to which datasets.  
This also included identifying the relationships between tables.

After that, the task was to answer a set of questions using SQL queries and to visualize the results.

The questions included:

- What is the price distribution of menu items?
- What is the distribution of restaurants per location?
- Which are the top 10 pizza restaurants by rating?
- Get the addresses of restaurants that offer sushi and are located near me (within 1 km).  
  Sort the addresses by distance from my home.  
  For each restaurant, include the average order price in the results.
- Which restaurants in Flanders have the best price-to-rating ratio?

## 3. Action

For each question, a dedicated SQL query was written to retrieve the required data from the database.

For more complex cases, both the main queries used to produce the final answers and intermediate queries were saved in a separate `.sql` file for clarity and reuse.

Next, for each question, a Python script was developed to process the query results and present the answers in an appropriate form, such as numerical output, tables, or visualizations.

## 4. Result

The outputs of the scripts containing the answers were saved in a dedicated directory as text or graphical files.

The final conclusions derived from the analysis were documented in a separate file titled: **[Conclusions.md](Conclusions.md)**.
