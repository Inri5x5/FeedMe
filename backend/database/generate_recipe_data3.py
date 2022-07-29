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

################################# RECIPE ID = 69 = Lamb with Gravy #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (69, 596, "2.5-3 kg leg of lamb"),
    (69, 830, "4 red onions"),
    (69, 522, "2 bulbs of garlic"),
    (69, 148, "100 g unsalted butter"),
    (69, 532, "\u00bd a bunch of fresh thyme"),
    (69, 527, "\u00bd a bunch of fresh rosemary"),
    (69, 146, "3 tablespoons plain flour"),
    (69, 110, "port"),
    (69, 887, "1 litre hot organic chicken stock"),
    (69, 913 "1 celeriac"),
    (69, 820, "1 kg potatoes"),
    (69, 865, "extra virgin olive oil"),
    (69, 777, "1 whole nutmeg for grating"),
    (69, 525, "1 big bunch of fresh mint"),
    (69, 687, "2 tablespoons red wine vinegar"),
    (69, 4, "1 tablespoon soft brown sugar")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (69, 1),
    (69, 17),
    (69, 20),
    (69, 10)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (69, 322),
    (69, 227),
    (69, 46),
    (69, 193)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 70 = Porchetta #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (70, 599, "4-5 kg boneless jacket of pork, loin and belly attached"),
    (70, 104, "50 ml vin santo or other sweet dessert wine"),
    (70, 815, "6 large carrots"),
    (70, 117, "200 ml white wine"),
    (70, 796, "3 onions"),
    (70, 522, "4 cloves of garlic"),
    (70, 914, "200 g free-range chicken livers"),
    (70, 527, "4 sprigs of fresh rosemary"),
    (70, 532, "4 sprigs of fresh thyme"),
    (70, 29, "250 g fresh breadcrumbs"),
    (70, 864, "olive oil"),
    (70, 897, "400 g higher-welfare minced pork belly"),
    (70, 528, "10 fresh sage leaves"),
    (70, 104, "120 ml vin santo or other sweet dessert wine"),
    (70, 908, "25 g pine nuts"),
    (70, 915, "40 g sultanas"),
    (70, 146, "3 heaped tablespoons plain flour"),
    (70, 117, "120 ml white wine"),
    (70, 887, "1.5 litres organic chicken stock")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (70, 1),
    (70, 17),
    (70, 20),
    (70, 10)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (70, 90),
    (70, 318),
    (70, 46),
    (70, 61)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 71 = Green Tea Fish #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description),
VALUES
    (71, 147, "150 g brown rice"),
    (71, 243, "1 x 500 g salmon tail, skin on, scaled, bone in, from sustainable sources"),
    (71, 63, "1 green tea bag"),
    (71, 650, "sesame oil"),
    (71, 522, "1 clove of garlic"),
    (71, 813, "320 g mixed salad veg, such as carrots, cucumber, tomato, chicory"),
    (71, 392, "1 small ripe mango"),
    (71, 442, "1 lime"),
    (71, 665, "low-salt soy sauce"),
    (71, 869, "1 fresh red chilli"),
    (71, 774, "1 x 3cm piece of ginger"),
    (71, 650, "1 teaspoon sesame seeds"),
    (71, 541, "\u00bd a punnet of cress")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (71, 0),
    (71, 3),
    (71, 18),
    (71, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (71, 90),
    (71, 318),
    (71, 46)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 72 = Roast Onions #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description),
VALUES
    (72, 796, "6 large white onions peeled"),
    (72, 865, "5 tablespoons extra-virgin olive oil"),
    (72, 905, "1 teaspoon cumin seeds lightly crushed"),
    (72, 861, "1 tablespoon coriander seeds lightly crushed"),
    (72, 131, "100 g white basmati rice"),
    (72, 572, "100 g brown lentils"),
    (72, 917, "1/2 teaspoon ground tumeric"),
    (72, 783, "1 teaspoon ground allspice"),
    (72, 771, "1 teaspoon cinnamon"),
    (72, 916, "400 ml vegetable stock"),
    (72, 640, "50 g flaked almonds lightly toasted, plus extra to garnish"),
    (72, 779, "1 large handful of flat-leaf parsley chopped"),
    (72, 687, "2 tablespoons red wine vinegar"),
    (72, 4, "1 pinch of caster sugar"),
    (72, 540, "rocket salad to serve")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (72, 11),
    (72, 12),
    (72, 14),
    (72, 20),
    (72, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (72, 153),
    (72, 162),
    (72, 195),
    (72, 49)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 73 = Roast Goose #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description),
VALUES
    (73, 613, "1 x 4 kg whole goose (ask your butcher for the giblets, too)"),
    (73, 864, "olive oil"),
    (73, 443, "1 clementine"),
    (73, 527, "\u00bd a bunch of fresh rosemary (15g)"),
    (73, 796, "2 onions"),
    (73, 815, "3 carrots"),
    (73, 770, "3 sticks of celery"),
    (73, 876, "1 handful of fresh bay leaves"),
    (73, 110, "1 lug of port"),
    (73, 146, "2 heaped tablespoons plain flour"),
    (73, 887, "1 litre organic chicken stock"),
    (73, 447, "1 pomegranate"),
    (73, 766, "90 g star anise"),
    (73, 882, "90 g fennel seeds"),
    (73, 517, "75 g coriander seeds"),
    (73, 780, "30 g Sichuan pepper"),
    (73, 772, "15 g cloves"),
    (73, 771, "60 g cinnamon sticks"),
    (73, 781, "1 large pinch of saffron"),
    (73, 4, "90 g soft brown sugar"),
    (73, 3, "60 g sea salt"),
    (73, 780, "30 g whole black peppercorns")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (73, 9),
    (73, 20),
    (73, 19),
    (73, 14)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (73, 195),
    (73, 261),
    (73, 226),
    (73, 13)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

cursor.close()