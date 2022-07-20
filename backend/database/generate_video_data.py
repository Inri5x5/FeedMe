import sqlite3
import json

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

# TURN ON FOREIGN KEY CONSTRAINTS
cursor.execute("PRAGMA foreign_keys = ON")

# insert into skillVideos
delete_query = """DELETE FROM skillVideos WHERE 1"""
cursor.execute(delete_query)


# insert into skillVideoInRecipe
delete_query = """DELETE FROM skillVideoInRecipe WHERE 1"""
cursor.execute(delete_query)


# insert into skillVideoSaves
delete_query = """DELETE FROM skillVideoSaves WHERE 1"""
cursor.execute(delete_query)