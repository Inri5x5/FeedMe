import sqlite3
import json

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

# TURN ON FOREIGN KEY CONSTRAINTS
cursor.execute("PRAGMA foreign_keys = ON")

# TAG CATEGORIES TABLE
drop_tag_categories_table_query = """
    DROP TABLE IF EXISTS tagCategories
"""

create_tag_categories_table_query = """
    CREATE TABLE tagCategories (
        id integer PRIMARY KEY NOT NULL,
        name text NOT NULL
)
"""

cursor.execute(drop_tag_categories_table_query)
cursor.execute(create_tag_categories_table_query)


# TAGS TABLE
drop_tags_table_query = """
    DROP TABLE IF EXISTS tags
"""

create_tags_table_query = """
    CREATE TABLE tags (
        id integer PRIMARY KEY NOT NULL,
        tag_category_id integer NOT NULL,
        name text,
        FOREIGN KEY(tag_category_id) REFERENCES tagCategories(id) ON DELETE CASCADE
)
"""

cursor.execute(drop_tags_table_query)
cursor.execute(create_tags_table_query)


# RECIPES TABLE
drop_recipes_table_query = """
    DROP TABLE IF EXISTS recipes
"""

create_recipes_table_query = """
    CREATE TABLE recipes (
        id integer PRIMARY KEY NOT NULL,
        title text NOT NULL,
        description text NOT NULL,
        image text NOT NULL,
        video text,
        time_required integer NOT NULL,
        servings integer NOT NULL,
        original_id integer
)
"""

cursor.execute(drop_recipes_table_query)
cursor.execute(create_recipes_table_query)


# TAG IN RECIPE TABLE
drop_tag_in_recipe_table_query = """
    DROP TABLE IF EXISTS tagInRecipe
"""

create_tag_in_recipe_table_query = """
    CREATE TABLE tagInRecipe (
        recipe_id interger NOT NULL,
        tag_id integer NOT NULL,
        FOREIGN KEY(recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
        FOREIGN KEY(tag_id) REFERENCES tags(id) ON DELETE CASCADE
)
"""

cursor.execute(drop_tag_in_recipe_table_query)
cursor.execute(create_tag_in_recipe_table_query)


# INGREDIENT IN RECIPE TABLE
drop_ingredient_in_recipe_table_query = """
    DROP TABLE IF EXISTS ingredientInRecipe
"""

create_ingredient_in_recipe_table_query = """
    CREATE TABLE ingredientInRecipe (
        recipe_id interger NOT NULL,
        ingredient_id integer NOT NULL,
        description text NOT NULL,
        FOREIGN KEY(recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
        FOREIGN KEY(ingredient_id) REFERENCES ingredients(id) ON DELETE CASCADE
)
"""

cursor.execute(drop_ingredient_in_recipe_table_query)
cursor.execute(create_ingredient_in_recipe_table_query)


# RECIPE STEPS TABLE
drop_steps_table_query = """
    DROP TABLE IF EXISTS steps
"""

create_steps_table_query = """
    CREATE TABLE steps (
        recipe_id interger NOT NULL,
        step_number interger NOT NULL,
        description text NOT NULL,
        image text,
        FOREIGN KEY(recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
        CONSTRAINT PK_steps PRIMARY KEY (recipe_id, step_number)
)
"""

cursor.execute(drop_steps_table_query)
cursor.execute(create_steps_table_query)


# RECIPE SAVES TABLE
drop_recipe_saves_table_query = """
    DROP TABLE IF EXISTS recipeSaves
"""

create_recipe_saves_table_query = """
    CREATE TABLE recipeSaves (
        ruser_id integer,
        contributor_id integer,
        recipe_id integer NOT NULL,
        FOREIGN KEY(ruser_id) REFERENCES rusers(id) ON DELETE CASCADE,
        FOREIGN KEY(contributor_id) REFERENCES contributors(id) ON DELETE CASCADE,
        FOREIGN KEY(recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
        CONSTRAINT PK_recipeSaves PRIMARY KEY (ruser_id, contributor_id, recipe_id)
)
"""

cursor.execute(drop_recipe_saves_table_query)
cursor.execute(create_recipe_saves_table_query)


# PERSONAL RECIPES TABLE
drop_personal_recipes_table_query = """
    DROP TABLE IF EXISTS personalRecipes
"""

create_personal_recipes_table_query = """
    CREATE TABLE personalRecipes (
        ruser_id integer,
        contributor_id integer,
        recipe_id integer NOT NULL,
        FOREIGN KEY(ruser_id) REFERENCES rusers(id) ON DELETE CASCADE,
        FOREIGN KEY(contributor_id) REFERENCES contributors(id) ON DELETE CASCADE,
        FOREIGN KEY(recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
        CONSTRAINT PK_personalRecipes PRIMARY KEY (ruser_id, contributor_id, recipe_id)
)
"""

cursor.execute(drop_personal_recipes_table_query)
cursor.execute(create_personal_recipes_table_query)


# PUBLIC RECIPES TABLE
drop_public_recipes_table_query = """
    DROP TABLE IF EXISTS publicRecipes
"""

create_public_recipes_table_query = """
    CREATE TABLE publicRecipes (
        recipe_id integer NOT NULL,
        contributor_id integer NOT NULL,
        FOREIGN KEY(recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
        FOREIGN KEY(contributor_id) REFERENCES contributors(id) ON DELETE CASCADE,
        CONSTRAINT PK_publicRecipes PRIMARY KEY (recipe_id, contributor_id)
)
"""

cursor.execute(drop_public_recipes_table_query)
cursor.execute(create_public_recipes_table_query)


# RECIPE RATINGS TABLE
drop_recipe_ratings_table_query = """
    DROP TABLE IF EXISTS recipeRatings
"""

create_recipe_ratings_table_query = """
    CREATE TABLE recipeRatings (
        ruser_id integer,
        contributor_id integer,
        recipe_id integer NOT NULL,
        rating integer NOT NULL,
        FOREIGN KEY(ruser_id) REFERENCES rusers(id) ON DELETE CASCADE,
        FOREIGN KEY(contributor_id) REFERENCES contributors(id) ON DELETE CASCADE,
        FOREIGN KEY(recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
        CONSTRAINT PK_recipeRatings PRIMARY KEY (ruser_id, contributor_id, recipe_id)
)
"""

cursor.execute(drop_recipe_ratings_table_query)
cursor.execute(create_recipe_ratings_table_query)