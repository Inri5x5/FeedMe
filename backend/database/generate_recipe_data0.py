import sqlite3
import json

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

# TURN ON FOREIGN KEY CONSTRAINTS
cursor.execute("PRAGMA foreign_keys = ON")

fp = open('./source_data/recipes.json', 'r')
recipe_data = json.load(fp)

#cursor.close()

#insert into Recipes
delete_query = """DELETE FROM recipes WHERE 1"""
cursor.execute(delete_query)

insert_query = """INSERT INTO recipes (id, title, description, image, video, time_required, servings, original_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
for recipe in recipe_data:
    cursor.execute('SELECT max(id) from recipes')
    new_id = cursor.fetchone()
    #print("THE ID IS HERE!!! " + new_id[0])
    if new_id[0] is None:
        new_id = 0
    else:
        new_id = new_id[0] + 1
    cursor = cursor.execute(insert_query, (new_id, recipe['name'], recipe['description'], recipe['image'], recipe['video'], recipe['time'], recipe['servings'], None))
    conn.commit()

# insert into Steps
delete_query = """DELETE FROM steps WHERE 1"""
cursor.execute(delete_query)
insert_query = """INSERT INTO steps (recipe_id, step_number,description,image) VALUES (?, ?, ?, ?)"""
i = 0
for recipe in recipe_data:
    j = 0
    for step in recipe['steps']:
        cursor = cursor.execute(insert_query, (i, j, step, ""))
        conn.commit()
        j += 1
    i += 1

# insert into IngredientInRecipe
delete_query = """DELETE FROM IngredientInRecipe WHERE 1"""
cursor.execute(delete_query)
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (0, 140, "200 g quinoa"),
    (0, 442, "2 limes"),
    (0, 817, "2 sweet potatoes (350g each)"),
    (0, 863, "1 pinch of dried chilli flakes"),
    (0, 868, "1 pinch of ground coriander"),
    (0, 771, "1 small pinch of ground cinnamon"),
    (0, 864, "olive oil"),
    (0, 798, "320 g broccoli"),
    (0, 664, "35 g mixed nuts such as walnuts, almonds, Brazils"),
    (0, 447, "pomegranate"),
    (0, 865, "extra virgin olive oil"),
    (0, 866, "1 splash of balsamic vinegar"),
    (0, 867, "40 g mixed sprouts"),
    (0, 541, "1 punnet of salad cress (use a mixture of varieties, if possible)"),
    (0, 517, "1 bunch of fresh coriander (30g)"),
    (0, 869, "1 fresh red chilli"),
    (0, 367, "1 ripe avocado"),
    (0, 159, "20 g feta cheese")

"""

cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()


# insert into TagCategories
delete_query = """DELETE FROM TagCategories WHERE 1"""
cursor.execute(delete_query)
categories_data = [{"category_id": 0, "name": "Culture's Cuisine"}, {"category_id": 1, "name": "Difficulty"}, {"category_id": 2, "name": "Special Diet"}, {"category_id": 3, "name": "Meal Type"}]

insert_into_tagCategories_query = """
INSERT INTO 
    tagCategories (id, name)
VALUES
    (?, ?)
"""
for category in categories_data:
    cursor = cursor.execute(insert_into_tagCategories_query, (category['category_id'], category['name']))
    conn.commit()

# insert into Tags
delete_query = """DELETE FROM Tags WHERE 1"""
cursor.execute(delete_query)
tags_data = [
    {"id": 0, "category_id": 0, "name": "Chinese"},
    {"id": 1, "category_id": 0, "name": "Italian"},
    {"id": 2, "category_id": 0, "name": "Indian"},
    {"id": 3, "category_id": 0, "name": "Japanese"},
    {"id": 4, "category_id": 0, "name": "Korean"},
    {"id": 5, "category_id": 0, "name": "French"},
    {"id": 6, "category_id": 0, "name": "Greek"},
    {"id": 7, "category_id": 0, "name": "Mexican"},
    {"id": 8, "category_id": 1, "name": "Easy peasy"},
    {"id": 9, "category_id": 1, "name": "A bit tricky"},
    {"id": 10, "category_id": 1, "name": "Challenge me!"},
    {"id": 11, "category_id": 2, "name": "Vegetarian"},
    {"id": 12, "category_id": 2, "name": "Vegan"},
    {"id": 13, "category_id": 2, "name": "Gluten-free"},
    {"id": 14, "category_id": 2, "name": "Dairy-free"},
    {"id": 15, "category_id": 2, "name": "Nut-free"},
    {"id": 16, "category_id": 3, "name": "Breakfast"},
    {"id": 17, "category_id": 3, "name": "Lunch"},
    {"id": 18, "category_id": 3, "name": "Dinner"},
    {"id": 19, "category_id": 3, "name": "Entree"},
    {"id": 20, "category_id": 3, "name": "Main"},
    {"id": 21, "category_id": 3, "name": "Dessert"},
    {"id": 22, "category_id": 3, "name": "Snack"},
    {"id": 23, "category_id": 3, "name": "Drink"},
    {"id": 24, "category_id": 3, "name": "Sides"}
]

insert_into_tags_query = """
INSERT INTO 
    tags (id, tag_category_id, name)
VALUES
    (?, ?, ?)
"""
for tag in tags_data:
    cursor = cursor.execute(insert_into_tags_query, (tag['id'], tag['category_id'], tag['name']))
    conn.commit()

# SUPERFOOD SALAD
#insert into IngredientInRecipe
delete_query = """DELETE FROM IngredientInRecipe WHERE 1"""
cursor.execute(delete_query)
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (0, 140, "200 g quinoa"),
    (0, 442, "2 limes"),
    (0, 817, "2 sweet potatoes (350g each)"),
    (0, 863, "1 pinch of dried chilli flakes"),
    (0, 868, "1 pinch of ground coriander"),
    (0, 771, "1 small pinch of ground cinnamon"),
    (0, 864, "olive oil"),
    (0, 798, "320 g broccoli"),
    (0, 664, "35 g mixed nuts such as walnuts, almonds, Brazils"),
    (0, 447, "pomegranate"),
    (0, 865, "extra virgin olive oil"),
    (0, 866, "1 splash of balsamic vinegar"),
    (0, 867, "40 g mixed sprouts"),
    (0, 541, "1 punnet of salad cress (use a mixture of varieties, if possible)"),
    (0, 517, "1 bunch of fresh coriander (30g)"),
    (0, 869, "1 fresh red chilli"),
    (0, 367, "1 ripe avocado"),
    (0, 159, "20 g feta cheese")

"""

cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()



# insert into TagInRecipe
delete_query = """DELETE FROM TagInRecipe WHERE 1"""
cursor.execute(delete_query)
insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (0, 13),
    (0, 11),
    (0, 9),
    (0, 20),
    (0, 17),
    (0, 18)
"""

cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()


# PEA SOUP
# insert into IngredientInRecipe
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (1, 870, "1 bunch of spring onions"),
    (1, 565, "300 g frozen peas"),
    (1, 828, "300 g frozen chopped spinach"),
    (1, 871, "100 g higher-welfare smoked ham"),
    (1, 525, "\u00bd a bunch of fresh mint (15g)"),
    (1, 35, "300 g dried wholewheat fusilli"),
    (1, 159, "50 g feta cheese")

"""

cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()



# insert into TagInRecipe
insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (1, 8),
    (1, 15),
    (1, 18),
    (1, 20)
"""

cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()


# VEGGIE LASAGNA
# insert into IngredientInRecipe
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (2, 793, "1 leek"),
    (2, 148, "50 g unsalted butter"),
    (2, 673, "olive oil"),
    (2, 818, "500 g asparagus"),
    (2, 146, "50 g plain flour"),
    (2, 803, "2 teaspoons English mustard"),
    (2, 179, "800 ml semi-skimmed milk"),
    (2, 565, "300 g fresh or frozen peas"),
    (2, 790, "300 g fresh or frozen broad beans"),
    (2, 525, "\u00bd a bunch of fresh mint (15g)"),
    (2, 165, "80 g Parmesan cheese plus extra to serve"),
    (2, 153, "80 g mature Cheddar cheese"),
    (2, 872, "250 g fresh lasagne sheets"),
    (2, 640, "50 g blanched almonds"),
    (2, 441, "1 lemon optional"),
    (2, 873, "green pesto optional")

"""

cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

# insert into TagInRecipe
insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (2, 1),
    (2, 11),
    (2, 18),
    (2, 20)
"""

cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()