import sqlite3
import json

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

# TURN ON FOREIGN KEY CONSTRAINTS
cursor.execute("PRAGMA foreign_keys = ON")

# SEARCHES TABLE
drop_searches_table_query = """
    DROP TABLE IF EXISTS searches
"""

create_searches_table_query = """
    CREATE TABLE searches (
        id integer PRIMARY KEY NOT NULL,
        count integer NOT NULL
)
"""

cursor.execute(drop_searches_table_query)
cursor.execute(create_searches_table_query)


# INGREDIENT IN SEARCH TABLE
drop_ingredientInSearch_table_query = """
    DROP TABLE IF EXISTS ingredientInSearch
"""

create_ingredientInSearch_table_query = """
    CREATE TABLE ingredientInSearch (
        search_id integer NOT NULL,
        ingredient_id integer NOT NULL,
        FOREIGN KEY(search_id) REFERENCES searches(id) ON DELETE CASCADE,
        FOREIGN KEY(ingredient_id) REFERENCES ingredients(id) ON DELETE CASCADE
)
"""

cursor.execute(drop_ingredientInSearch_table_query)
cursor.execute(create_ingredientInSearch_table_query)


# SKILL VIDEOS TABLE
drop_skillVideos_table_query = """
    DROP TABLE IF EXISTS skillVideos
"""

create_skillVideos_table_query = """
    CREATE TABLE skillVideos (
        id integer PRIMARY KEY NOT NULL,
        contributor_id integer NOT NULL,
        title text NOT NULL,
        link text NOT NULL,
        FOREIGN KEY(contributor_id) REFERENCES contributors(id) ON DELETE CASCADE
)
"""

cursor.execute(drop_skillVideos_table_query)
cursor.execute(create_skillVideos_table_query)


# SKILL VIDEO IN RECIPE TABLE
drop_skillVideoInRecipe_table_query = """
    DROP TABLE IF EXISTS skillVideoInRecipe
"""

create_skillVideoInRecipe_table_query = """
    CREATE TABLE skillVideoInRecipe (
        recipe_id integer NOT NULL,
        skill_video_id integer NOT NULL,
        FOREIGN KEY(recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
        FOREIGN KEY(skill_video_id) REFERENCES skillVideos(id) ON DELETE CASCADE
)
"""

cursor.execute(drop_skillVideoInRecipe_table_query)
cursor.execute(create_skillVideoInRecipe_table_query)


# SKILL VIDEO SAVES TABLE
drop_skillVideoSaves_table_query = """
    DROP TABLE IF EXISTS skillVideoSaves
"""

create_skillVideoSaves_table_query = """
    CREATE TABLE skillVideoSaves (
        ruser_id integer NOT NULL,
        skill_video_id integer NOT NULL,
        FOREIGN KEY(ruser_id) REFERENCES rusers(id) ON DELETE CASCADE,
        FOREIGN KEY(skill_video_id) REFERENCES skillVideos(id) ON DELETE CASCADE
)
"""

cursor.execute(drop_skillVideoSaves_table_query)
cursor.execute(create_skillVideoSaves_table_query)