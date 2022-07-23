import sqlite3
import json

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

# TURN ON FOREIGN KEY CONSTRAINTS
cursor.execute("PRAGMA foreign_keys = ON")

# insert into Searches
delete_query = """DELETE FROM searches WHERE 1"""
cursor.execute(delete_query)

insert_into_searches_query = """
INSERT INTO 
    searches (id, count)
VALUES
    (0, 30),
    (1, 1),
    (2, 9),
    (3, 15),
    (4, 15),
    (5, 12)
"""

cursor = cursor.execute(insert_into_searches_query)
conn.commit()


# insert into IngredientInSearch
delete_query = """DELETE FROM IngredientInSearch WHERE 1"""
cursor.execute(delete_query)

insert_into_IngredientInSearch_query = """
INSERT INTO 
    IngredientInSearch (search_id, ingredient_id)
VALUES
    (0, 594),
    (1, 592),
    (1, 585),
    (2, 771),
    (3, 513),
    (3, 35),
    (3, 811),
    (4, 800),
    (5, 789)
"""

cursor = cursor.execute(insert_into_IngredientInSearch_query)
conn.commit()