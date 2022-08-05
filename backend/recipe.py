from helper import *

def update_recipe(recipe_id, user_details, req):
    conn = db_connection()
    c = conn.cursor()
    print("PLEASE WORK")
    print(recipe_id)
    if recipe_id == -1: #If user adds a new recipe or edits a public recipe for the first time
        print("recipe id = -1")
        c.execute("SELECT * FROM recipes ORDER BY id DESC LIMIT 1")
        recipe_id = c.fetchone()[0]
        recipe_id = recipe_id + 1
        insert_recipe_details(conn, user_details, recipe_id, req)
    elif recipe_id != -1 and req['public_state'] == "public" and req["original_id"] is not None: # If a user publishes a recipe that has been published before
        print("original id is not null")
        c.execute("DELETE FROM Recipes WHERE id=?", [recipe_id])
        original_id = req["original_id"]
        req["original_id"] = None
        update_recipe_details(conn, user_details, original_id, req)
        conn.commit()
    else:
        print("everything")
        update_recipe_details(conn, user_details, recipe_id, req)
    
    return {}

def delete_recipe(recipe_id):
    conn = db_connection()
    cur = conn.cursor()

    cur.execute('DELETE FROM recipes WHERE id = ?', [recipe_id])
    conn.commit()
    cur.close()

    return {}

def recipe_save(recipe_id, user_details):
    conn = db_connection()
    c = conn.cursor()

    id = user_details["user_id"]

    if has_saved_recipe(conn, recipe_id, user_details) == False:
        if user_details['is_contributor'] == False:
            c.execute("INSERT INTO recipeSaves(ruser_id, recipe_id) VALUES (?, ?)", (id, recipe_id))
        else:
            c.execute("INSERT INTO recipeSaves(contributor_id, recipe_id) VALUES (?, ?)", (id, recipe_id))
    else:
        if user_details["is_contributor"] == False:
            c.execute("DELETE FROM recipeSaves WHERE ruser_id = ? AND recipe_id = ?", [id, recipe_id])
        else:
            c.execute("DELETE FROM recipeSaves WHERE contributor_id = ? AND recipe_id = ?", [id, recipe_id])
    
    conn.commit()
    c.close()

    return {}

def recipe_rate(recipe_id, user_details, rating):
    conn = db_connection()
    id = user_details["user_id"]

    c = conn.cursor()
    if user_details["is_contributor"] == False:
        c.execute("SELECT * FROM recipeRatings WHERE recipe_id = ? AND ruser_id = ?", [recipe_id, id])
        if has_rated(conn, recipe_id, user_details) == True:
            c.execute("DELETE FROM recipeRatings WHERE recipe_id = ? AND ruser_id = ?", [recipe_id, id])
            c.execute("INSERT INTO recipeRatings(ruser_id, recipe_id, rating) VALUES (?, ?, ?)", (id, recipe_id, rating))
        else:
            c.execute("INSERT INTO recipeRatings(ruser_id, recipe_id, rating) VALUES (?, ?, ?)", (id, recipe_id, rating))
    else:
        c.execute("SELECT * FROM recipeRatings WHERE recipe_id = ? AND contributor_id = ?", [recipe_id, id])
        if has_rated(conn, recipe_id, user_details) == True:
            c.execute("DELETE FROM recipeRatings WHERE recipe_id = ? AND contributor_id = ?", [recipe_id, id])
            c.execute("INSERT INTO recipeRatings(contributor_id, recipe_id, rating) VALUES (?, ?, ?)", (id, recipe_id, rating))
        else:
            c.execute("INSERT INTO recipeRatings(contributor_id, recipe_id, rating) VALUES (?, ?, ?)", (id, recipe_id, rating))

    conn.commit()
    c.close()

    return {}