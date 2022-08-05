from helper import *

def ingredient_categories():
    conn = db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM ingredientCategories")
    data = c.fetchall()
    conn.close()

    categories = []
    for (i, j) in data:
        categories.append({"name": j, "c_id": i})
    
    return categories

def ingredient_information(ingredient):
    conn = db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM ingredients")
    data = c.fetchall()
    conn.close()

    suggestions = []
    for (i, j, k) in data:
        if ingredient.lower() in k.lower():
            suggestions.append({"name": k, "i_id": i, "c_id": j})
    
    return suggestions

def add_new_ingredient(ingredient_name, category_id):
    conn = db_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM ingredients ORDER BY id DESC LIMIT 1")
    new_ingredient_id = c.fetchone()[0]
    new_ingredient_id = new_ingredient_id + 1

    # add ingredient to "Ingredients" database
    c.execute("INSERT INTO ingredients VALUES (?, ?, ?)", (new_ingredient_id, category_id, ingredient_name))
    conn.commit()
    c.close()

    return new_ingredient_id

def valid_category_id(category_id):
    conn = db_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM ingredientCategories ORDER BY id DESC LIMIT 1")
    max_cat_id = c.fetchone()[0]
    if category_id > max_cat_id:
        return -1
    
    return 1

def ingredient_exists(ingredient_name):
    conn = db_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM ingredients WHERE name = ? COLLATE NOCASE", [ingredient_name])
    if c.fetchone() is not None:
        return -1
    
    return 1
    