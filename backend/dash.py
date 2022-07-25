from helper import *

def statistics(contributor_id):
    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    qry = '''
        SELECT r.id, 
            SUM(CASE WHEN rr.rating = 1 THEN 1 ELSE 0 END) AS one_rating,
            SUM(CASE WHEN rr.rating = 2 THEN 1 ELSE 0 END) AS two_rating,
            SUM(CASE WHEN rr.rating = 3 THEN 1 ELSE 0 END) AS three_rating,
            SUM(CASE WHEN rr.rating = 4 THEN 1 ELSE 0 END) AS four_rating,
            SUM(CASE WHEN rr.rating = 5 THEN 1 ELSE 0 END) AS five_rating
        FROM recipes r
            LEFT JOIN publicRecipes pr ON pr.recipe_id = r.id
            LEFT JOIN recipeRatings rr ON rr.recipe_id = r.id
        WHERE pr.contributor_id = ?
        GROUP BY r.id
    '''
    cur.execute(qry, [contributor_id])
    info = cur.fetchall()
    statistics_list = [] 

    for i in info:
        # Recipe id and number of ratings
        recipe_id, one_rating, two_rating, three_rating, four_rating, five_rating = i

        # Average rating = sum of ratings/total number of ratings
        num_ratings = one_rating + two_rating + three_rating + four_rating + five_rating
        sum_ratings = (one_rating + two_rating * 2 + three_rating * 3 + four_rating * 4 + five_rating * 5)

        if num_ratings == 0:
            avg_rating = 0
        else:
            avg_rating = sum_ratings/num_ratings

        # Number of recipe saves
        cur.execute('SELECT COUNT(*) FROM recipeSaves WHERE recipe_id = ?', [recipe_id])
        info = cur.fetchone()
        if not info:
            num_saves = 0
        else:
            num_saves = info

        recipe_stats = {
            "recipe_id": recipe_id,
            "stats": {
                "one star": one_rating,
                "two star": two_rating,
                "three star": three_rating,
                "four star": four_rating,
                "five star": five_rating,
                "avg rating": avg_rating,
                "num saves": num_saves,
                "num ratings": num_ratings
            }
        }

        statistics_list.append(recipe_stats)

    cur.close()

    return statistics_list

def saved_recipes(token):
    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    # Decode token to get user details
    user = decode_token(conn, token)
    cur = conn.cursor()
    if user["is_contributor"]:  # Contributor
        cur.execute('SELECT recipe_id FROM recipeSaves WHERE contributor_id = ?', [user["user_id"]])
    else: # RUser
        cur.execute('SELECT recipe_id FROM recipeSaves WHERE ruser_id = ?', [user["user_id"]])
    info = cur.fetchall()

    recipes = []
    for i in info:
        recipe_details = get_recipe_details(conn, i[0], user)
        recipes.append(recipe_details)
    
    cur.close()

    return recipes

def rated_recipes(token):
    # Connect to database
    conn = db_connection()
    cur = conn.cursor()

    # Decode token to get user details
    user = decode_token(conn, token)

    cur = conn.cursor()
    if user["is_contributor"]:  # Contributor
        cur.execute('''SELECT recipe_id, rating FROM recipeRatings
            WHERE contributor_id = ?''', [user["user_id"]])
    else: # RUser
        cur.execute('''SELECT recipe_id, rating FROM recipeRatings
            WHERE ruser_id = ?''', [user["user_id"]])
    info = cur.fetchall()
    cur.close()

    # Create recipes list
    one_star_recipes = []
    two_star_recipes = []
    three_star_recipes = []
    four_star_recipes = []
    five_star_recipes = []
    for i in info:
        recipe_id, rating = i
        if rating == 1:
            one_star_recipes.append(get_recipe_details(conn, recipe_id, user))
        elif rating == 2:
            two_star_recipes.append(get_recipe_details(conn, recipe_id, user))
        elif rating == 3:
            three_star_recipes.append(get_recipe_details(conn, recipe_id, user))
        elif rating == 4:
            four_star_recipes.append(get_recipe_details(conn, recipe_id, user))
        else: # rating == 5
            five_star_recipes.append(get_recipe_details(conn, recipe_id, user))

    return one_star_recipes, two_star_recipes, three_star_recipes, four_star_recipes, five_star_recipes