import sqlite3
import json

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

# insert into RecipeSaves
delete_query = """DELETE FROM RecipeSaves WHERE 1"""
cursor.execute(delete_query)
insert_into_recipeSaves_query = """
INSERT INTO 
    recipeSaves (ruser_id, contributor_id, recipe_id)
VALUES
    (0, null, 0),
    (0, null, 1),
    (0, null, 2),
    (0, null, 3),
    (0, null, 7),
    (0, null, 8),
    (0, null, 9),
    (null, 0, 0),
    (null, 0, 4),
    (null, 0, 5),
    (null, 0, 6)
"""

cursor = cursor.execute(insert_into_recipeSaves_query)
conn.commit()

# insert into personalRecipes
delete_query = """DELETE FROM personalRecipes WHERE 1"""
cursor.execute(delete_query)
insert_into_personalRecipes_query = """
INSERT INTO 
    personalRecipes (ruser_id, contributor_id, recipe_id)
VALUES
    (null, 0, 0),
    (null, 0, 1),
    (null, 0, 2),
    (null, 0, 3),
    (null, 0, 4),
    (null, 0, 5),
    (null, 0, 6),
    (null, 0, 7),
    (null, 0, 8),
    (null, 0, 9)
"""

cursor = cursor.execute(insert_into_personalRecipes_query)
conn.commit()

# insert into publicRecipes
delete_query = """DELETE FROM PublicRecipes WHERE 1"""
cursor.execute(delete_query)
insert_into_PublicRecipes_query = """
INSERT INTO 
    PublicRecipes (recipe_id, contributor_id)
VALUES
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (5, 0),
    (6, 0),
    (7, 0),
    (8, 0),
    (9, 0)
"""

cursor = cursor.execute(insert_into_PublicRecipes_query)
conn.commit()

# insert into recipeRatings
delete_query = """DELETE FROM recipeRatings WHERE 1"""
cursor.execute(delete_query)
insert_into_recipeRatings_query = """
INSERT INTO 
    recipeRatings (ruser_id, contributor_id, recipe_id, rating)
VALUES
    (null, 0, 0, 5),
    (null, 0, 1, 5),
    (null, 0, 2, 5),
    (null, 0, 3, 5),
    (null, 0, 4, 5),
    (0, null, 0, 5),
    (0, null, 1, 4),
    (0, null, 2, 3),
    (0, null, 3, 2),
    (0, null, 9, 1)
"""

cursor = cursor.execute(insert_into_recipeRatings_query)
conn.commit()