import sqlite3
import json

# RUSERS TABLE
conn_rusers = sqlite3.connect("rusers.sqlite")

cursor_rusers = conn_rusers.cursor()

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

cursor_rusers.execute(drop_rusers_table_query)
cursor_rusers.execute(create_rusers_table_query)

fp1 = open('./source_data/rusers_table.json', 'r')
ruser_data = json.load(fp1)
for ruser in ruser_data:
    insert_query = """INSERT INTO rusers (id, email, username, password, profile_picture) VALUES (?, ?, ?, ?, ?)"""
    cursor_rusers = cursor_rusers.execute(insert_query, (ruser['ruser_id'], ruser['email'], ruser['username'], ruser['password'], ""))
    conn_rusers.commit()


# CONTRIBUTORS TABLE
conn_contributors = sqlite3.connect("contributors.sqlite")

cursor_contributors = conn_contributors.cursor()

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

cursor_contributors.execute(drop_contributors_table_query)
cursor_contributors.execute(create_contributors_table_query)

fp2 = open('./source_data/contributors_table.json', 'r')
contributor_data = json.load(fp2)
for contributor in contributor_data:
    insert_query = """INSERT INTO contributors (id, email, username, password, profile_picture) VALUES (?, ?, ?, ?, ?)"""
    cursor_contributors = cursor_contributors.execute(insert_query, (contributor['contributor_id'], contributor['email'], contributor['username'], contributor['password'], ""))
    conn_contributors.commit()


# TOKENS TABLE
conn_tokens = sqlite3.connect("tokens.sqlite")

cursor_tokens = conn_tokens.cursor()

drop_tokens_table_query = """
    DROP TABLE IF EXISTS tokens
"""

create_tokens_table_query = """
    CREATE TABLE tokens (
        token string PRIMARY KEY NOT NULL,
        ruser_id integer,
        contributor_id integer,
        FOREIGN KEY(ruser_id) REFERENCES ruser(id),
        FOREIGN KEY(contributor_id) REFERENCES contributor(id)
)
"""

cursor_tokens.execute(drop_tokens_table_query)
cursor_tokens.execute(create_tokens_table_query)

fp3 = open('./source_data/tokens_table.json', 'r')
token_data = json.load(fp3)
insert_query_tokens = """INSERT INTO tokens (token, ruser_id, contributor_id) VALUES (?, ?, ?)"""
for token in token_data:
    if(token['is_contributor']):
        cursor_tokens = cursor_tokens.execute(insert_query_tokens, (token['token'], None, token['user_id']))
    else:
        cursor_tokens = cursor_tokens.execute(insert_query_tokens, (token['token'], token['user_id'], None))
    conn_tokens.commit()


# INGREDIENT CATEGORIES TABLE
conn_ingredient_categories = sqlite3.connect("ingredient_category.sqlite")

cursor_ingredient_categories = conn_ingredient_categories.cursor()

drop_ingredient_categories_table_query = """
    DROP TABLE IF EXISTS ingredientCategories
"""

create_ingredient_categories_table_query = """
    CREATE TABLE ingredientCategories (
        id integer PRIMARY KEY NOT NULL,
        name text NOT NULL
)
"""

cursor_ingredient_categories.execute(drop_ingredient_categories_table_query)
cursor_ingredient_categories.execute(create_ingredient_categories_table_query)

fp4 = open('./source_data/ingredient_categories_table.json', 'r')
ingredient_category_data = json.load(fp4)
insert_query_ingredient_categories = """INSERT INTO ingredientCategories (id, name) VALUES (?, ?)"""
for ingredient_category in ingredient_category_data:
    cursor_ingredient_categories = cursor_ingredient_categories.execute(insert_query_ingredient_categories, (ingredient_category['category_id'], ingredient_category['name']))
    conn_ingredient_categories.commit()

# INGREDIENTS TABLE
conn_ingredients = sqlite3.connect("ingredients.sqlite")

cursor_ingredients = conn_ingredients.cursor()

drop_ingredients_table_query = """
    DROP TABLE IF EXISTS ingredients
"""

create_ingredients_table_query = """
    CREATE TABLE ingredients (
        id interger PRIMARY KEY NOT NULL,
        ingredient_category_id integer NOT NULL,
        name text,
        FOREIGN KEY(ingredient_category_id) REFERENCES ingredientCategories(id)
)
"""

cursor_ingredients.execute(drop_ingredients_table_query)
cursor_ingredients.execute(create_ingredients_table_query)

fp5 = open('./source_data/ingredients_table.json', 'r')
ingredient_data = json.load(fp5)
insert_query_ingredients = """INSERT INTO ingredients (id, ingredient_category_id, name) VALUES (?, ?, ?)"""
for ingredient in ingredient_data:
    cursor_ingredients = cursor_ingredients.execute(insert_query_ingredients, (ingredient['ingredient_id'], ingredient['ingredient_category_id'], ingredient['name']))
    conn_ingredients.commit()