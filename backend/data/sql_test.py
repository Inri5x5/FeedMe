import sqlite3

conn = sqlite3.connect('nepka.db')

c = conn.cursor()




# c.execute("""CREATE TABLE recipe_ratings (
#             recipe_id integer,
#             ruser_id integer,
#             rating integer
#         )""")

# c.execute("""CREATE TABLE tag_in_recipe (
#             recipe_id integer,
#             tag_id integer
#         )""")

# c.execute("""CREATE TABLE ingredient_in_recipe (
#             recipe_id integer,
#             ingredient_id integer
#         )""")

# c.execute("INSERT INTO tag_in_recipe VALUES (1, 1)")
# c.execute("INSERT INTO ingredient_in_recipe VALUES (1, 1)")
# c.execute("INSERT INTO recipe_ratings VALUES (1, 1, 5)")
# c.execute("DROP TABLE tag_in_recipe")
# c.execute("""CREATE TABLE Public_Recipes (
#             recipe_id integer,
#             author_id integer
#         )""")

c.execute("DROP TABLE recipe_ratings")
c.execute("""CREATE TABLE Recipe_Ratings (             
        recipe_id integer,
        author_id integer, 
        rating integer
    )""")
c.execute("INSERT INTO Recipe_Ratings VALUES (1, 1, 3)")
c.execute("INSERT INTO Recipe_Ratings VALUES (2, 2, 2)")



conn.commit()


conn.close()