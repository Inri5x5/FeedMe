import sqlite3
import json

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

# TURN ON FOREIGN KEY CONSTRAINTS
cursor.execute("PRAGMA foreign_keys = ON")

# RUSERS TABLE
drop_rusers_table_query = """
    DROP TABLE IF EXISTS rusers
"""

create_rusers_table_query = """
    CREATE TABLE rusers (
        id integer PRIMARY KEY NOT NULL,
        email text UNIQUE NOT NULL,
        username text NOT NULL,
        password text NOT NULL,
        profile_picture text
)
"""

cursor.execute(drop_rusers_table_query)
cursor.execute(create_rusers_table_query)

fp1 = open('./source_data/rusers_table.json', 'r')
ruser_data = json.load(fp1)
for ruser in ruser_data:
    insert_query = """INSERT INTO rusers (id, email, username, password, profile_picture) VALUES (?, ?, ?, ?, ?)"""
    cursor = cursor.execute(insert_query, (ruser['ruser_id'], ruser['email'], ruser['username'], ruser['password'], ""))
    conn.commit()


# CONTRIBUTORS TABLE
drop_contributors_table_query = """
    DROP TABLE IF EXISTS contributors
"""

create_contributors_table_query = """
    CREATE TABLE contributors (
        id integer PRIMARY KEY NOT NULL,
        email text UNIQUE NOT NULL,
        username text NOT NULL,
        password text NOT NULL,
        profile_picture text
)
"""

cursor.execute(drop_contributors_table_query)
cursor.execute(create_contributors_table_query)

fp2 = open('./source_data/contributors_table.json', 'r')
contributor_data = json.load(fp2)
for contributor in contributor_data:
    insert_query = """INSERT INTO contributors (id, email, username, password, profile_picture) VALUES (?, ?, ?, ?, ?)"""
    cursor = cursor.execute(insert_query, (contributor['contributor_id'], contributor['email'], contributor['username'], contributor['password'], ""))
    conn.commit()


# TOKENS TABLE
drop_tokens_table_query = """
    DROP TABLE IF EXISTS tokens
"""

create_tokens_table_query = """
    CREATE TABLE tokens (
        token string PRIMARY KEY NOT NULL,
        ruser_id integer,
        contributor_id integer,
        FOREIGN KEY(ruser_id) REFERENCES rusers(id) ON DELETE CASCADE,
        FOREIGN KEY(contributor_id) REFERENCES contributors(id) ON DELETE CASCADE
)
"""

cursor.execute(drop_tokens_table_query)
cursor.execute(create_tokens_table_query)

fp3 = open('./source_data/tokens_table.json', 'r')
token_data = json.load(fp3)
insert_query_tokens = """INSERT INTO tokens (token, ruser_id, contributor_id) VALUES (?, ?, ?)"""
for token in token_data:
    if(token['is_contributor']):
        cursor = cursor.execute(insert_query_tokens, (token['token'], None, token['user_id']))
    else:
        cursor = cursor.execute(insert_query_tokens, (token['token'], token['user_id'], None))
    conn.commit()


# INGREDIENT CATEGORIES TABLE
drop_ingredient_categories_table_query = """
    DROP TABLE IF EXISTS ingredientCategories
"""

create_ingredient_categories_table_query = """
    CREATE TABLE ingredientCategories (
        id integer PRIMARY KEY NOT NULL,
        name text NOT NULL
)
"""

cursor.execute(drop_ingredient_categories_table_query)
cursor.execute(create_ingredient_categories_table_query)

fp4 = open('./source_data/ingredient_categories_table.json', 'r')
ingredient_category_data = json.load(fp4)
insert_query_ingredient_categories = """INSERT INTO ingredientCategories (id, name) VALUES (?, ?)"""
for ingredient_category in ingredient_category_data:
    cursor = cursor.execute(insert_query_ingredient_categories, (ingredient_category['category_id'], ingredient_category['name']))
    conn.commit()

# INGREDIENTS TABLE
drop_ingredients_table_query = """
    DROP TABLE IF EXISTS ingredients
"""

create_ingredients_table_query = """
    CREATE TABLE ingredients (
        id interger PRIMARY KEY NOT NULL,
        ingredient_category_id integer NOT NULL,
        name text,
        FOREIGN KEY(ingredient_category_id) REFERENCES ingredientCategories(id) ON DELETE CASCADE
)
"""

cursor.execute(drop_ingredients_table_query)
cursor.execute(create_ingredients_table_query)

fp5 = open('./source_data/ingredients_table.json', 'r')
ingredient_data = json.load(fp5)
insert_query_ingredients = """INSERT INTO ingredients (id, ingredient_category_id, name) VALUES (?, ?, ?)"""
for ingredient in ingredient_data:
    cursor = cursor.execute(insert_query_ingredients, (ingredient['ingredient_id'], ingredient['ingredient_category_id'], ingredient['name']))
    conn.commit()
