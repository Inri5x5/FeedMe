from helper import *

def search_for_recipes(token, ingredients_req):
    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    # Get user id from token
    if (token != '-1'):
        user_details = decode_token(conn, token) 
    else :
        user_details = -1

    # Find recipes that have the ingredients requested
    cur.execute('''
        SELECT r.recipe_id, GROUP_CONCAT(ir.ingredient_id)
        FROM    PublicRecipes r
                JOIN ingredientInRecipe ir on ir.recipe_id = r.recipe_id
        GROUP BY r.recipe_id
    ''')
    info = cur.fetchall()
    cur.close()

    # Addd recipes to list
    recipes = []
    for i in info:
        recipe_id, ingredients = i
        ingredients_split = ingredients.split(',')
        ingredients_split_int = [int(i) for i in ingredients_split]    
       
        if set(ingredients_split_int) >= set(ingredients_req) or ingredients_req is None:
            recipe_details = get_recipe_details(conn, recipe_id, user_details)
            recipes.append(recipe_details)

    return recipes

def has_searched(ingredients_req):
    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    # Check if search combination already exists
    n_comb, search_id = check_search_combinations(conn, ingredients_req)

    # New search combination
    if n_comb:
        # Get a new search id
        search_id = get_new_search_id(conn)

        # Update Searches table
        cur.execute('INSERT INTO Searches (id, count) VALUES (?, ?)', [search_id, 1])

        # Insert rows of ingredient ids to IngredientInSearch table
        qry = '''INSERT INTO IngredientInSearch 
            (ingredient_id, search_id) VALUES (?, ?)'''
        for ingredient_id in ingredients_req:
            cur.execute(qry, [ingredient_id, search_id])

    # Existing search combination
    else:
        # Update Searches table (increment count)
        cur.execute('UPDATE Searches SET count = count + 1 WHERE id = ?', [search_id])

    conn.commit()
    cur.close()

    return

def recommendation():
    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    # Get top ingredients in recipes
    cur.execute('''
        SELECT ir.ingredient_id, COUNT(ir.ingredient_id) AS occurence, i.name
        FROM IngredientInRecipe ir
            JOIN Ingredients i on i.id = ir.ingredient_id
        GROUP BY ir.ingredient_id
        ORDER BY occurence DESC
    ''')
    info = cur.fetchall()

    # Add top ingredients to the recommendations
    ingredients = []
    rank = 1
    for i in info:
        id, count, name = i
        i_dict = {"rank": rank, "id": id, "name": name}
        ingredients.append(i_dict)

        rank += 1

    return ingredients

def no_recipes():
    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    # Create a view of ingredients (ingredient_id, name, search_id) that 
    # are in searches but not in recipes
    cur.execute('DROP VIEW IF EXISTS searches_minus_recipes')
    conn.commit()
    cur.execute('''
        CREATE VIEW searches_minus_recipes AS
        SELECT 
            iss.ingredient_id as ingredient_id, 
            i.name as ingredient_name, 
            iss.search_id as search_id
        FROM IngredientInSearch iss
            LEFT JOIN IngredientInRecipe ir on ir.ingredient_id = iss.ingredient_id
            LEFT JOIN Ingredients i on i.id = iss.ingredient_id
        WHERE ir.ingredient_id is NULL
    ''')
    conn.commit()

    # From the previous view, order the ingredients by the number of times
    # its search id occurs (descending)
    # cur.execute('''
    #     SELECT smr.search_id, s.count
    #     FROM searches_minus_recipes smr
    #         JOIN searches s on s.id = smr.search_id
    #     GROUP BY smr.search_id
    #     ORDER BY s.count DESC
    # ''')
    cur.execute('''
        SELECT smr.search_id, s.count
        FROM searches s
            JOIN searches_minus_recipes smr on s.id = smr.search_id
        GROUP BY smr.search_id
        ORDER BY s.count DESC
    ''')
    info = cur.fetchall()

    # From the search ids, get its ingredient combinations and add to return list
    ic_list = []
    rank = 1
    for i in info:
        search_id, num_searches = i
        ingredient_list = get_searched_combinations(conn, search_id)

        ic_list.append({
            "rank": rank,
            "num_searches": num_searches,
            "ingredient_list": ingredient_list
        })
        
        rank += 1

    cur.close()

    return ic_list