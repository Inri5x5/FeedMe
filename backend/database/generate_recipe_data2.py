import sqlite3
import json

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

# TURN ON FOREIGN KEY CONSTRAINTS
cursor.execute("PRAGMA foreign_keys = ON")

fp = open('./source_data/recipes.json', 'r')
recipe_data = json.load(fp)

# Tables to insert into (see other python files for examples)
# IngredientInRecipe (add new ingredients to Ingredients where necessary)
# TagInRecipe
# SkillVideoInRecipe (add new videos to SkillVideos where necessary)


fp.close()
cursor.close()