# recipe id 61 - 89
import sqlite3
import json

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

# TURN ON FOREIGN KEY CONSTRAINTS
cursor.execute("PRAGMA foreign_keys = ON")

# For each recipe
# 1. clean up the recipes.json data for that recipe (add video if there is
# one, clean up the servings and time so they are integers)
# 2. write an insert into IngredientInRecipe query (use ingredients_table.json
# as the source data, and see line 48 in generate_recipe_data0.py for an example)
# 3. write an insert into TagInRecipe query (use generate_recipe_data0.py line 95 
# as the source data, and see line 168 in generate_recipe_data0.py for an example)
# 4. write an insert into SkillVideoInRecipe query (use generate_video_data.py line 14 
# as the source data, see generate_video_data.py line 372 as an example)

################################# RECIPE ID = 59 = SLOW-ROASTED LAMB #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (59, 864, "olive oil"),
    (59, 879, "250 g pork sausage"),
    (59, 520, "small bulbs of fennel"),
    (59, 830, "2 red onions"),
    (59, 139, "250 g sourdough bread"),
    (59, 596, "3 kg lamb shoulder bone in"),
    (59, 522, "1 bulb of garlic"),
    (59, 146, "2 heaped tablespoons plain flour"),
    (59, 436, "1 tablespoon jam of choice"),
    (59, 687, "red wine vinegar"),
    (59, 258, "1 bunch of sage")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (59, 14),
    (59, 18),
    (59, 9),
    (59, 1)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (59, 35),
    (59, 26),
    (59, 318),
    (59, 322)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 60 = Farmhouse roast chicken #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (60, 864, "olive oil"),
    (60, 594, "1 x 1.5 kg free-range whole chicken"),
    (60, 520, "small bulbs of fennel"),
    (60, 687, "red wine vinegar"),
    (60, 874, "3 rashers of bacon"),
    (60, 499, "650 g mixed mushrooms"),
    (60, 828, "250 g baby spinach"),
    (60, 572, "2 x 400 g tins of green lentils"),
    (60, 885, "100 g half-fat cre\u0300me frai\u0302che"),
    (60, 531, "\u00bd a bunch of tarragon (10g)"),

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (60, 13),
    (60, 18),
    (60, 9),
    (60, 1)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (60, 132),
    (60, 134),
    (60, 116),
    (60, 193),
    (60, 88),
    (60, 93)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 61 = Perfect Pork Belly #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (61, 897, "4 kg piece of pork belly bone in"),
    (61, 876, "6 bay leaves"),
    (61, 3, "2 tablespoons sea salt"),
    (61, 861, "2 tablespoons coriander seeds"),
    (61, 882, "2 tablespoons fennel seeds"),
    (61, 780, "2 tablespoons black peppercorns"),
    (61, 796, "4 onions"),
    (61, 108, "300 ml dry cider"),
    (61, 815, "4 carrots"),
    (61, 820, "4 potatoes"),
    (61, 770, "4 sticks of celery"),
    (61, 520, "2 bulbs of fennel"),
    (61, 527, "4 sprigs of fresh rosemary"),
    (61, 522, "1 bulb of garlic")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (61, 14),
    (61, 18),
    (61, 9),
    (61, 1)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (61, 35),
    (61, 46),
    (61, 236),
    (61, 322)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 62 = Roast Topside of Beef #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (62, 864, "olive oil"),
    (62, 592, "3 kg topside of beef"),
    (62, 796, "1 onion"),
    (62, 815, "2 carrots"),
    (62, 770, "A head of celery"),
    (62, 527, "3 sprigs of fresh rosemary"),
    (62, 522, "1 bulb of garlic"),
    (62, 876, "3 fresh bay leaves"),
    (62, 436, "1 tablespoon jam of choice"),
    (62, 111, "125 ml red wine"),
    (62, 898, "1 litre organic beef stock")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (62, 14),
    (62, 18),
    (62, 9),
    (62, 1)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (62, 203),
    (62, 322),
    (62, 207),
    (62, 215)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 63 = Roasted Salmon & Artichokes #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (63, 864, "olive oil"),
    (63, 243, "2 x 1 kg sides of salmon skin on, scaled, pin-boned"),
    (63, 640, "blanched almonds"),
    (63, 441, "2 lemons"),
    (63, 29, "100 g stale ciabatta"),
    (63, 842, "2 fresh baby Italian artichokes"),
    (63, 522, "2 cloves of garlic"),
    (63, 354, "1 x 280 g jar of artichoke hearts in oil"),
    (63, 525, "1 bunch of fresh mint (30g)"),
    (63, 874, "12 rashers of smoked streaky bacon"),
    (63, 532, "1 bunch of fresh thyme (30g)")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (63, 14),
    (63, 18),
    (63, 9),
    (63, 1)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (63, 247),
    (63, 227),
    (63, 39)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 64 = Sweet Chicken Surprise #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (64, 594, "2 x 200 g free-range chicken legs"),
    (64, 522, "1 bulb of garlic"),
    (64, 384, "250 g mixed-colour seedless grapes"),
    (64, 121, "100 ml red vermouth"),
    (64, 531, "4 sprigs of fresh tarragon")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (64, 14),
    (64, 18),
    (64, 17),
    (64, 9),
    (64, 13)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (64, 108),
    (64, 92),
    (64, 93),
    (64, 11)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 65 = Balsamic Lamb #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (65, 864, "olive oil"),
    (65, 596, "2.5 kg higher-welfare lamb shoulder"),
    (65, 830, "4 red onions"),
    (65, 527, "\u00bd a bunch of fresh rosemary (15g)"),
    (65, 777, "1 whole nutmeg for grating"),
    (65, 866, "200 ml balsamic vinegar"),
    (65, 522, "1 bulb of garlic"),
    (65, 525, "1 bunch of fresh mint (30g)"),
    (65, 146, "1 heaped tablespoon plain flour")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (65, 17),
    (65, 20),
    (65, 1),
    (65, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (65, 46),
    (65, 227),
    (65, 239),
    (65, 300)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 66 = Roasted Salmon and Veg #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (66, 864, "olive oil"),
    (66, 820, "400 g baby potatoes"),
    (66, 790, "200 g green beans"),
    (66, 513, "1 bunch of fresh basil"),
    (66, 459, "200 g cherry tomatoes"),
    (66, 673, "10 black olives (stone in)"),
    (66, 441, "1\u00bd lemons"),
    (66, 522, "\u00bd a small clove of garlic"),
    (66, 803, "\u00bd teaspoon Dijon mustard"),
    (66, 899, "4 tablespoons Greek yoghurt"),
    (66, 865, "extra virgin olive oil")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (66, 18),
    (66, 20),
    (66, 1),
    (66, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (66, 247),
    (66, 258),
    (66, 81),
    (66, 121)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 67 = Spiced Sea Bass #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (67, 864, "olive oil"),
    (67, 520, "3 bulbs of fennel"),
    (67, 148, "40 g butter"),
    (67, 900, "2 whole seabass gutted and scaled"),
    (67, 869, "1 fresh red chilli"),
    (67, 441, "1 lemon"),
    (67, 522, "1 clove of garlic")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (67, 18),
    (67, 13),
    (67, 0),
    (67, 8)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (67, 81),
    (67, 121),
    (67, 35)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 68 = Roast Quail #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (68, 629, "8 quail"),
    (68, 901, "2 teaspoons za\u2019atar"),
    (68, 44, "4 Arab-style flatbread"),
    (68, 794, "2 little gem lettuces"),
    (68, 540, "1 handful of rocket leaves"),
    (68, 865, "6 tablespoons extra-virgin olive oil"),
    (68, 19, "4 tablespoons pomegranate molasses"),
    (68, 861, "1 tablespoon coriander seeds"),
    (68, 773, "1 tablespoon ground cumin"),
    (68, 774, "1 tablespoon ground ginger"),
    (68, 781, "1 teaspoon saffron threads"),
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (68, 18),
    (68, 20),
    (68, 9),
    (68, 18)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (68, 335),
    (68, 22)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


cursor.close()