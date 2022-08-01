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
    (61, 864, "olive oil"),
    (61, 879, "250 g pork sausage"),
    (61, 520, "small bulbs of fennel"),
    (61, 830, "2 red onions"),
    (61, 139, "250 g sourdough bread"),
    (61, 596, "3 kg lamb shoulder bone in"),
    (61, 522, "1 bulb of garlic"),
    (61, 146, "2 heaped tablespoons plain flour"),
    (61, 436, "1 tablespoon jam of choice"),
    (61, 687, "red wine vinegar"),
    (61, 258, "1 bunch of sage")
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
    (61, 26),
    (61, 318),
    (61, 322)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 60 = Farmhouse roast chicken #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (62, 864, "olive oil"),
    (62, 594, "1 x 1.5 kg free-range whole chicken"),
    (62, 520, "small bulbs of fennel"),
    (62, 687, "red wine vinegar"),
    (62, 874, "3 rashers of bacon"),
    (62, 499, "650 g mixed mushrooms"),
    (62, 828, "250 g baby spinach"),
    (62, 572, "2 x 400 g tins of green lentils"),
    (62, 885, "100 g half-fat cre\u0300me frai\u0302che"),
    (62, 531, "\u00bd a bunch of tarragon (10g)")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (62, 13),
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
    (62, 132),
    (62, 134),
    (62, 116),
    (62, 193),
    (62, 88),
    (62, 93)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 61 = Perfect Pork Belly #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (63, 897, "4 kg piece of pork belly bone in"),
    (63, 876, "6 bay leaves"),
    (63, 3, "2 tablespoons sea salt"),
    (63, 861, "2 tablespoons coriander seeds"),
    (63, 882, "2 tablespoons fennel seeds"),
    (63, 780, "2 tablespoons black peppercorns"),
    (63, 796, "4 onions"),
    (63, 108, "300 ml dry cider"),
    (63, 815, "4 carrots"),
    (63, 820, "4 potatoes"),
    (63, 770, "4 sticks of celery"),
    (63, 520, "2 bulbs of fennel"),
    (63, 527, "4 sprigs of fresh rosemary"),
    (63, 522, "1 bulb of garlic")
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
    (63, 35),
    (63, 46),
    (63, 236),
    (63, 322)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 62 = Roast Topside of Beef #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (64, 864, "olive oil"),
    (64, 592, "3 kg topside of beef"),
    (64, 796, "1 onion"),
    (64, 815, "2 carrots"),
    (64, 770, "A head of celery"),
    (64, 527, "3 sprigs of fresh rosemary"),
    (64, 522, "1 bulb of garlic"),
    (64, 876, "3 fresh bay leaves"),
    (64, 436, "1 tablespoon jam of choice"),
    (64, 111, "125 ml red wine"),
    (64, 898, "1 litre organic beef stock")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (64, 14),
    (64, 18),
    (64, 9),
    (64, 1)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (64, 203),
    (64, 322),
    (64, 207),
    (64, 215)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 63 = Roasted Salmon & Artichokes #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (65, 864, "olive oil"),
    (65, 243, "2 x 1 kg sides of salmon skin on, scaled, pin-boned"),
    (65, 640, "blanched almonds"),
    (65, 441, "2 lemons"),
    (65, 29, "100 g stale ciabatta"),
    (65, 842, "2 fresh baby Italian artichokes"),
    (65, 522, "2 cloves of garlic"),
    (65, 354, "1 x 280 g jar of artichoke hearts in oil"),
    (65, 525, "1 bunch of fresh mint (30g)"),
    (65, 874, "12 rashers of smoked streaky bacon"),
    (65, 532, "1 bunch of fresh thyme (30g)")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (65, 14),
    (65, 18),
    (65, 9),
    (65, 1)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (65, 247),
    (65, 227),
    (65, 39)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 64 = Sweet Chicken Surprise #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (66, 594, "2 x 200 g free-range chicken legs"),
    (66, 522, "1 bulb of garlic"),
    (66, 384, "250 g mixed-colour seedless grapes"),
    (66, 121, "100 ml red vermouth"),
    (66, 531, "4 sprigs of fresh tarragon")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (66, 14),
    (66, 18),
    (66, 17),
    (66, 9),
    (66, 13)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (66, 108),
    (66, 92),
    (66, 93),
    (66, 11)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 65 = Balsamic Lamb #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (67, 864, "olive oil"),
    (67, 596, "2.5 kg higher-welfare lamb shoulder"),
    (67, 830, "4 red onions"),
    (67, 527, "\u00bd a bunch of fresh rosemary (15g)"),
    (67, 777, "1 whole nutmeg for grating"),
    (67, 866, "200 ml balsamic vinegar"),
    (67, 522, "1 bulb of garlic"),
    (67, 525, "1 bunch of fresh mint (30g)"),
    (67, 146, "1 heaped tablespoon plain flour")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (67, 17),
    (67, 20),
    (67, 1),
    (67, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (67, 46),
    (67, 227),
    (67, 239),
    (67, 300)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 66 = Roasted Salmon and Veg #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (68, 864, "olive oil"),
    (68, 820, "400 g baby potatoes"),
    (68, 790, "200 g green beans"),
    (68, 513, "1 bunch of fresh basil"),
    (68, 459, "200 g cherry tomatoes"),
    (68, 673, "10 black olives (stone in)"),
    (68, 441, "1\u00bd lemons"),
    (68, 522, "\u00bd a small clove of garlic"),
    (68, 803, "\u00bd teaspoon Dijon mustard"),
    (68, 899, "4 tablespoons Greek yoghurt"),
    (68, 865, "extra virgin olive oil")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (68, 18),
    (68, 20),
    (68, 1),
    (68, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (68, 247),
    (68, 258),
    (68, 81),
    (68, 121)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 67 = Spiced Sea Bass #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (69, 864, "olive oil"),
    (69, 520, "3 bulbs of fennel"),
    (69, 148, "40 g butter"),
    (69, 900, "2 whole seabass gutted and scaled"),
    (69, 869, "1 fresh red chilli"),
    (69, 441, "1 lemon"),
    (69, 522, "1 clove of garlic")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (69, 18),
    (69, 13),
    (69, 0),
    (69, 8)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (69, 81),
    (69, 121),
    (69, 35)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 68 = Roast Quail #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (70, 629, "8 quail"),
    (70, 901, "2 teaspoons za\u2019atar"),
    (70, 44, "4 Arab-style flatbread"),
    (70, 794, "2 little gem lettuces"),
    (70, 540, "1 handful of rocket leaves"),
    (70, 865, "6 tablespoons extra-virgin olive oil"),
    (70, 19, "4 tablespoons pomegranate molasses"),
    (70, 861, "1 tablespoon coriander seeds"),
    (70, 773, "1 tablespoon ground cumin"),
    (70, 774, "1 tablespoon ground ginger"),
    (70, 781, "1 teaspoon saffron threads")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (70, 18),
    (70, 20),
    (70, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (70, 335),
    (70, 22)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 69 = Lamb with Gravy #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (71, 596, "2.5-3 kg leg of lamb"),
    (71, 830, "4 red onions"),
    (71, 522, "2 bulbs of garlic"),
    (71, 148, "100 g unsalted butter"),
    (71, 532, "\u00bd a bunch of fresh thyme"),
    (71, 527, "\u00bd a bunch of fresh rosemary"),
    (71, 146, "3 tablespoons plain flour"),
    (71, 110, "port"),
    (71, 887, "1 litre hot organic chicken stock"),
    (71, 913, "1 celeriac"),
    (71, 820, "1 kg potatoes"),
    (71, 865, "extra virgin olive oil"),
    (71, 777, "1 whole nutmeg for grating"),
    (71, 525, "1 big bunch of fresh mint"),
    (71, 687, "2 tablespoons red wine vinegar"),
    (71, 4, "1 tablespoon soft brown sugar")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (71, 1),
    (71, 17),
    (71, 20),
    (71, 10)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (71, 322),
    (71, 227),
    (71, 46),
    (71, 193)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 70 = Porchetta #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (72, 599, "4-5 kg boneless jacket of pork, loin and belly attached"),
    (72, 104, "50 ml vin santo or other sweet dessert wine"),
    (72, 815, "6 large carrots"),
    (72, 117, "200 ml white wine"),
    (72, 796, "3 onions"),
    (72, 522, "4 cloves of garlic"),
    (72, 914, "200 g free-range chicken livers"),
    (72, 527, "4 sprigs of fresh rosemary"),
    (72, 532, "4 sprigs of fresh thyme"),
    (72, 29, "250 g fresh breadcrumbs"),
    (72, 864, "olive oil"),
    (72, 897, "400 g higher-welfare minced pork belly"),
    (72, 528, "10 fresh sage leaves"),
    (72, 104, "120 ml vin santo or other sweet dessert wine"),
    (72, 908, "25 g pine nuts"),
    (72, 915, "40 g sultanas"),
    (72, 146, "3 heaped tablespoons plain flour"),
    (72, 117, "120 ml white wine"),
    (72, 887, "1.5 litres organic chicken stock")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (72, 1),
    (72, 17),
    (72, 20),
    (72, 10),
    (72, 18)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (72, 90),
    (72, 318),
    (72, 46),
    (72, 61)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 71 = Green Tea Fish #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (73, 147, "150 g brown rice"),
    (73, 243, "1 x 500 g salmon tail, skin on, scaled, bone in, from sustainable sources"),
    (73, 63, "1 green tea bag"),
    (73, 650, "sesame oil"),
    (73, 522, "1 clove of garlic"),
    (73, 813, "320 g mixed salad veg, such as carrots, cucumber, tomato, chicory"),
    (73, 392, "1 small ripe mango"),
    (73, 442, "1 lime"),
    (73, 665, "low-salt soy sauce"),
    (73, 869, "1 fresh red chilli"),
    (73, 774, "1 x 3cm piece of ginger"),
    (73, 650, "1 teaspoon sesame seeds"),
    (73, 541, "\u00bd a punnet of cress")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (73, 0),
    (73, 3),
    (73, 18),
    (73, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (73, 90),
    (73, 318),
    (73, 46)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 72 = Roast Onions #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (74, 796, "6 large white onions peeled"),
    (74, 865, "5 tablespoons extra-virgin olive oil"),
    (74, 905, "1 teaspoon cumin seeds lightly crushed"),
    (74, 861, "1 tablespoon coriander seeds lightly crushed"),
    (74, 131, "100 g white basmati rice"),
    (74, 572, "100 g brown lentils"),
    (74, 782, "1/2 teaspoon ground tumeric"),
    (74, 783, "1 teaspoon ground allspice"),
    (74, 771, "1 teaspoon cinnamon"),
    (74, 916, "400 ml vegetable stock"),
    (74, 640, "50 g flaked almonds lightly toasted, plus extra to garnish"),
    (74, 779, "1 large handful of flat-leaf parsley chopped"),
    (74, 687, "2 tablespoons red wine vinegar"),
    (74, 4, "1 pinch of caster sugar"),
    (74, 540, "rocket salad to serve")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (74, 11),
    (74, 12),
    (74, 14),
    (74, 20),
    (74, 9),
    (74, 18)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (74, 153),
    (74, 162),
    (74, 195),
    (74, 49)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 73 = Roast Goose #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (75, 613, "1 x 4 kg whole goose (ask your butcher for the giblets, too)"),
    (75, 864, "olive oil"),
    (75, 917, "1 clementine"),
    (75, 527, "\u00bd a bunch of fresh rosemary (15g)"),
    (75, 796, "2 onions"),
    (75, 815, "3 carrots"),
    (75, 770, "3 sticks of celery"),
    (75, 876, "1 handful of fresh bay leaves"),
    (75, 110, "1 lug of port"),
    (75, 146, "2 heaped tablespoons plain flour"),
    (75, 887, "1 litre organic chicken stock"),
    (75, 447, "1 pomegranate"),
    (75, 766, "90 g star anise"),
    (75, 882, "90 g fennel seeds"),
    (75, 517, "75 g coriander seeds"),
    (75, 780, "30 g Sichuan pepper"),
    (75, 772, "15 g cloves"),
    (75, 771, "60 g cinnamon sticks"),
    (75, 781, "1 large pinch of saffron"),
    (75, 4, "90 g soft brown sugar"),
    (75, 3, "60 g sea salt"),
    (75, 780, "30 g whole black peppercorns")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (75, 9),
    (75, 20),
    (75, 19),
    (75, 14)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (75, 195),
    (75, 261),
    (75, 226),
    (75, 13)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 74 = Clementine Roast Carrots #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (76, 815, "1 kg small mixed-colour carrots"),
    (76, 864, "olive oil"),
    (76, 527, "2 sprigs of fresh rosemary"),
    (76, 917, "2 clementines")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (76, 11),
    (76, 12),
    (76, 13),
    (76, 14),
    (76, 8),
    (76, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (76, 215),
    (76, 226),
    (76, 226),
    (76, 229)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 75 = Homemade Pickles #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (77, 801, "400 g cauliflower"), 
    (77, 687, "250 ml vinegar such as white wine, red wine or cider"), 
    (77, 3, "1 tablespoon sea salt"), 
    (77, 4, "1 tablespoon caster sugar"), 
    (77, 519, "fresh dill optional"), 
    (77, 903, "mustard seeds optional") 
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (77, 11),
    (77, 12),
    (77, 13),
    (77, 14),
    (77, 8),
    (77, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (77, 228),
    (77, 3)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 76 = Chorizo pear cabbage #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (78, 888, "150 g quality chorizo"),
    (78, 882, "2 teaspoons fennel seeds"),
    (78, 830, "1 red onion"),
    (78, 800, "1 red cabbage (1kg)"),
    (78, 404, "1 x 410 g tin of sliced pears in natural juice") 
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (78, 1),
    (78, 13),
    (78, 14),
    (78, 9),
    (78, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (78, 151),
    (78, 3),
    (78, 164)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 77 = Courgettes #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (79, 864, "olive oil"),
    (79, 522, "1 clove of garlic"),
    (79, 599, "50 g piece of guanciale (cured pig\u2019s cheek) or smoked pancetta"),
    (79, 875, "4 firm courgettes"),
    (79, 459, "200 g ripe cherry tomatoes on the vine"),
    (79, 779, "4 sprigs of fresh flat-leaf parsley")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (79, 1),
    (79, 13),
    (79, 14),
    (79, 9),
    (79, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (79, 49),
    (79, 290),
    (79, 27)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 78 = Roast Root Veg #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (80, 820, "3 kg Maris Piper potatoes"),
    (80, 815, "16 carrots"),
    (80, 816, "12 parsnips"),
    (80, 522, "1 bulb of garlic"),
    (80, 527, "\u00bd a bunch of fresh rosemary (15g)")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (80, 11),
    (80, 13),
    (80, 14),
    (80, 12),
    (80, 9), 
    (80, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (80, 272),
    (80, 215),
    (80, 226)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 79 = Creamed Spinach #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (81, 795, "2 onions"), 
    (81, 521, "2 cloves of garlic"), 
    (81, 864, "olive oil"), 
    (81, 778, "2 teaspoons dried oregano"), 
    (81, 777, "1 whole nutmeg for grating"), 
    (81, 828, "1 kg frozen chopped spinach"), 
    (81, 148, "100 g unsalted butter (cold)"), 
    (81, 153, "100 g Cheddar cheese"), 
    (81, 146, "100 g plain flour"), 
    (81, 128, "100 g rolled oats"), 
    (81, 885, "250 ml cr\u00e8me fra\u00eeche")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (81, 11),
    (81, 9), 
    (81, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (81, 273),
    (81, 11),
    (81, 184)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 80 = Pot Roast Cauliflower #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (82, 796, "3 onions"),
    (82, 864, "olive oil"),
    (82, 328, "6 anchovy fillets in oil from sustainable sources"),
    (82, 522, "6 cloves of garlic"),
    (82, 672, "6 large green olives (stone in)"),
    (82, 117, "500 ml Gavi di Gavi white wine"),
    (82, 781, "1 small pinch of saffron (optional)"),
    (82, 801, "1 large head of cauliflower with leaves")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (82, 1),
    (82, 9),
    (82, 13),
    (82, 14), 
    (82, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (82, 228),
    (82, 300),
    (82, 336)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 81 = balsamic Potato #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (83, 820, "2.5 kg Maris Piper potatoes"),
    (83, 865, "extra virgin olive oil"),
    (83, 830, "4 red onions"),
    (83, 522, "4 cloves of garlic"),
    (83, 866, "200 ml cheap balsamic vinegar"),
    (83, 148, "50 g unsalted butter"),
    (83, 532, "\u00bd a bunch of fresh thyme (15g)"),
    (83, 540, "35 g rocket")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (83, 8),
    (83, 13),
    (83, 14), 
    (83, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (83, 272),
    (83, 11),
    (83, 336)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 82 = Mint Peas #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (84, 525, "\u00bd a bunch of fresh mint (15g)"),
    (84, 562, "200 g fresh podded or frozen broad beans"),
    (84, 565, "200 g fresh podded or frozen peas"),
    (84, 869, "1 fresh red chilli"),
    (84, 441, "1 lemon")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (84, 9),
    (84, 13),
    (84, 14),
    (84, 11),
    (84, 12), 
    (84, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (84, 227),
    (84, 131),
    (84, 0)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 83 = raisins #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (85, 828, "300 g frozen spinach (or 800g fresh spinach)"), 
    (85, 522, "1 small clove of garlic"), 
    (85, 180, "500 g Greek yoghurt"), 
    (85, 899, "sunflower oil"), 
    (85, 414, "40 g raisins"), 
    (85, 865, "extra virgin olive oil") 
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (85, 9),
    (85, 13),
    (85, 11),
    (85, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (85, 273),
    (85, 196),
    (85, 11)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 84 = raisins #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (86, 818, "16 asparagus spears"),
    (86, 562, "25 g broad beans"),
    (86, 153, "40 g Cheddar cheese"),
    (86, 500, "1 tablespoon truffle oil"),
    (86, 540, "1 handful of watercress or rocket"),
    (86, 499, "200 g button mushrooms"),
    (86, 866, "\u00bd tablespoon balsamic vinegar"),
    (86, 918, "40 g mayonnaise made using free-range eggs")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (86, 8),
    (86, 13),
    (86, 19),
    (86, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (86, 9),
    (86, 222),
    (86, 202)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 85 = roast potato #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (87, 820, "500 g Jersey Royal potato"),
    (87, 522, "1 handful of wild garlic leaves"),
    (87, 864, "olive oil"),
    (87, 527, "a few sprigs of fresh rosemary")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (87, 8),
    (87, 13),
    (87, 11),
    (87, 12),
    (87, 14), 
    (87, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (87, 260),
    (87, 11),
    (87, 300), 
    (87, 336)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 86 = winter salad #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (88, 800, "\u00bd a red cabbage"),
    (88, 800, "\u00bd a white cabbage"),
    (88, 815, "2 large carrots"),
    (88, 870, "4 spring onions"),
    (88, 843, "a few shoots from kale"),
    (88, 174, "300 ml milk"),
    (88, 328, "4 anchovies, from sustainable sources"),
    (88, 522, "6 cloves of garlic"),
    (88, 687, "2 tablespoons white wine vinegar"),
    (88, 865, "6 tablespoons extra virgin olive oil"),
    (88, 919, "1 teaspoon Dijon mustard"),
    (88, 650, "1 handful of sesame seeds"),
    (88, 525, "\u00bd a bunch of fresh mint (15g)")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (88, 8),
    (88, 24),
    (88, 17),
    (88, 18)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (88, 227),
    (88, 151),
    (88, 164)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 87 = Raw Spring Salad #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (89, 818, "1 bunch of asparagus"),
    (89, 804, "1 bunch of radishes"),
    (89, 875, "4 baby courgettes"),
    (89, 525, "\u00bd a bunch of fresh mint (15g)"),
    (89, 519, "\u00bd a bunch of fresh dill (15g)"),
    (89, 441, "1 lemon"),
    (89, 864, "extra virgin olive oil")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (89, 8),
    (89, 24),
    (89, 11),
    (89, 12),
    (89, 13),
    (89, 14)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (89, 202),
    (89, 222),
    (89, 246),
    (89, 227)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 132 = Gluten-free one-cup pancakes #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (132, 591, "1 large free-range egg"),
    (132, 920, "1 heaped cup of gluten-free self-raising flour (250g)"),
    (132, 174, "1 cup of milk (300ml)"),
    (132, 864, "olive oil")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (132, 11),
    (132, 13),
    (132, 16),
    (132, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (132, 43),
    (132, 44),
    (132, 316),
    (132, 324)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 133 = Apple & pear overnight oats #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (133, 128, "100 g rolled oats"),
    (133, 911, "200 g Granola Dust"),
    (133, 771, "ground cinnamon"),
    (133, 174, "500 ml semi-skimmed milk"),
    (133, 364, "2 apples"),
    (133, 404, "2 pears"),
    (133, 180, "natural yoghurt to serve")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (133, 11),
    (133, 16),
    (133, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (133, 211),
    (133, 205)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 134 = One-pan breakfast #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (134, 874, "3 rashers of smoked streaky bacon"),
    (134, 879, "4 sausages"),
    (134, 864, "olive oil"),
    (134, 811, "160 g ripe tomatoes"),
    (134, 591, "4 large free-range eggs"),
    (134, 29, "3 slices of bread")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (134, 14),
    (134, 16),
    (134, 8)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (134, 43),
    (134, 285),
    (134, 85),
    (134, 27)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 135 = Eggy bread muffins #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (135, 875, "400 g courgette"),
    (135, 843, "150 g kale"),
    (135, 17, "25 ml vegetable oil"),
    (135, 29, "400 g white or brown stale bread"),
    (135, 591, "8 free-range eggs"),
    (135, 174, "350 ml milk"),
    (135, 150, "125 g hard cheese")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (135, 11),
    (135, 16),
    (135, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (135, 43),
    (135, 44),
    (135, 17),
    (135, 56)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 136 = Roll-and-go omelette wrap #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (136, 591, "2 large free-range eggs"),
    (136, 864, "olive oil"),
    (136, 153, "10 g mature Cheddar cheese"),
    (136, 44, "1 wholegrain seeded tortilla wrap"),
    (136, 513, "\u00bd a bunch of fresh basil"),
    (136, 916, "chilli sauce"),
    (136, 811, "200 g ripe tomatoes"),
    (136, 540, "30 g rocket")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (136, 11),
    (136, 16),
    (136, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (136, 43),
    (136, 44),
    (136, 258),
    (136, 27)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 137 = Fig yogurt #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (137, 383, "8 ripe figs"),
    (137, 771, "\u00bc teaspoon cinnamon"),
    (137, 396, "4 tablespoons fresh unsweetened orange juice"),
    (137, 681, "4 tablespoons runny honey"),
    (137, 423, "150 g blackberries"),
    (137, 180, "600 g Greek yoghurt"),
    (137, 911, "4 tablespoons granola"),
    (137, 655, "2 tabelspoons unsalted pistachio nuts")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (137, 11),
    (137, 16),
    (137, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (137, 114),
    (137, 195),
    (137, 80)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 138 = One-cup pancakes with blueberries #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (138, 591, "1 large free-range egg"),
    (138, 146, "1 cup of self-raising flour"),
    (138, 174, "1 cup of milk"),
    (138, 424, "200 g blueberries"),
    (138, 864, "olive oil"),
    (138, 180, "4 tablespoons natural yoghurt")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (138, 11),
    (138, 16),
    (138, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (138, 316),
    (138, 324),
    (138, 43)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 139 = Cardamom clementine morning buns #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (139, 146, "500 g plain flour plus extra for dusting"),
    (139, 4, "50 g caster sugar"),
    (139, 510, "2 x 7 g sachets of dried yeast"),
    (139, 174, "300 ml whole milk"),
    (139, 148, "250 g unsalted butter (cold)"),
    (139, 768, "1 tablespoon ground cardamom"),
    (139, 771, "1 tablespoon ground cinnamon"),
    (139, 4, "100 g light brown muscovado sugar"),
    (139, 4, "90 g caster sugar plus 3 tablespoons"),
    (139, 917, "8 clementines"),
    (139, 148, "50 g unsalted butter")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (139, 11),
    (139, 16),
    (139, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (139, 208),
    (139, 293),
    (139, 43)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 140 = Roasted stone fruit #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (140, 396, "6 oranges"),
    (140, 866, "1 tablespoon balsamic vinegar"),
    (140, 446, "1 vanilla pod"),
    (140, 435, "150 g ripe strawberies"),
    (140, 379, "200 g Medjool dates"),
    (140, 128, "360 g porridge oats"),
    (140, 374, "80 g unsweetened desiccated coconut flakes"),
    (140, 865, "extra virgin olive oil"),
    (140, 403, "2 kg peaches"),
    (140, 180, "1 tablespoon natural yoghurt")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (140, 11),
    (140, 16),
    (140, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (140, 25),
    (140, 129),
    (140, 145)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 141 = Crumpets #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (141, 174, "400 ml milk"),
    (141, 510, "1 tablespoon dried yeast"),
    (141, 4, "1 teaspoon caster sugar"),
    (141, 146, "300 g strong white flour"),
    (141, 896, "\u00bd teaspoon bicarbonate of soda"),
    (141, 17, "vegetable oil for greasing"),
    (141, 184, "350 ml double cream")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (141, 11),
    (141, 16),
    (141, 9)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (141, 208),
    (141, 188)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 142 = Hollandaise sauce #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (142, 148, "150 g unsalted butter"),
    (142, 591, "2 large free-range egg yolks"),
    (142, 687, "1 dessert spoon white wine vinegar"),
    (142, 441, "1 lemon")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (142, 5),
    (142, 16),
    (142, 17),
    (142, 18),
    (142, 10)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (142, 15),
    (142, 231)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 143 = Simple cheese omelette #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (143, 591, "2 large free-range eggs"),
    (143, 864, "olive oil"),
    (143, 153, "10 g Cheddar cheese")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (143, 11),
    (143, 16),
    (143, 8),
    (143, 13)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (143, 43),
    (143, 44),
    (143, 188)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 144 = Quick Mexican breakfast #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (144, 811, "3 ripe tomatoes"),
    (144, 809, "2 roasted red peppers from a jar"),
    (144, 870, "4 spring onions"),
    (144, 442, "\u00bd\u20131 lime"),
    (144, 865, "extra virgin olive oil"),
    (144, 562, "1 x 400 g tin of black beans"),
    (144, 864, "olive oil"),
    (144, 44, "8 small flour or corn tortillas"),
    (144, 591, "4 large free-range eggs"),
    (144, 148, "1 knob of butter")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (144, 11),
    (144, 16),
    (144, 8),
    (144, 7)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (144, 43),
    (144, 285),
    (144, 25)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 145 = Charred avo & eggs #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (145, 809, "1 red pepper"),
    (145, 870, "4 spring onions"),
    (145, 367, "\u00bd a ripe avocado"),
    (145, 864, "olive oil"),
    (145, 817, "1 sweet potato"),
    (145, 591, "2 large free-range eggs"),
    (145, 155, "2 tablespoons cottage cheese"),
    (145, 869, "\u00bd a fresh red chilli"),
    (145, 517, "a few sprigs of coriander")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (145, 11),
    (145, 16),
    (145, 8),
    (145, 13)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (145, 43),
    (145, 308),
    (145, 317),
    (145, 287)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 146 = Mushroom Bruschettas #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (146, 499, "2 portobello mushrooms"),
    (146, 864, "olive oil"),
    (146, 522, "2 cloves of garlic"),
    (146, 148, "20 g unsalted butter"),
    (146, 29, "2 slices of sourdough bread"),
    (146, 499, "200 g mixed wild mushrooms cleaned"),
    (146, 918, "2 tablespoons fresh mayonnaise"),
    (146, 531, "2 sprigs of fresh tarragon")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (146, 11),
    (146, 16),
    (146, 8)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (146, 201),
    (146, 339),
    (146, 188),
    (146, 206)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 147 = Omelette aux fines herbes #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (147, 591, "2 large free-range eggs at room temperature"),
    (147, 779, "a few sprigs of parsley"),
    (147, 148, "1 large knob of butter")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (147, 11),
    (147, 13),
    (147, 16),
    (147, 8)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (147, 43),
    (147, 44),
    (147, 188)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 148 = Irish potato cakes #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (148, 146, "80 g plain flour plus extra for dusting"),
    (148, 820, "250 g leftover boiled, steamed or baked potatoes"),
    (148, 591, "1 large free-range egg yolk"),
    (148, 791, "\u00bd a bunch of chives (15g)"),
    (148, 802, "7cm piece of fresh horseradish or 2 teaspoons from a jar"),
    (148, 885, "4 tablespoons half-fat cr\u00e8me fra\u00eeche"),
    (148, 441, "1 lemon"),
    (148, 865, "extra virgin olive oil"),
    (148, 864, "olive oil"),
    (148, 242, "240 g smoked salmon"),
    (148, 679, "1 handful of watercress")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (148, 16),
    (148, 9),
    (148, 19)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (148, 272),
    (148, 193),
    (148, 293)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 149 = Brilliant breakfast waffles #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (149, 146, "150 g self-raising flour"),
    (149, 22, "1 teaspoon baking powder"),
    (149, 4, "1 teaspoon sugar"),
    (149, 591, "1 large free-range egg"),
    (149, 174, "240 ml semi-skimmed milk"),
    (149, 396, "1 orange optional"),
    (149, 446, "vanilla extract optional")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (149, 16),
    (149, 8),
    (149, 11)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (149, 43),
    (149, 44),
    (149, 231)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 150 = Green eggs & ham #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (150, 148, "1 small knob of unsalted butter"),
    (150, 864, "\u00bd tablespoon olive oil"),
    (150, 595, "160 g cooked sliced ham"),
    (150, 591, "2 large free-range eggs"),
    (150, 869, "2 small green chillies"),
    (150, 791, "a few sprigs of chives"),
    (150, 864, "6 tablespoons olive oil"),
    (150, 688, "1 teaspoon cider vinegar"),
    (150, 442, "\u00bd a lime")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (150, 16),
    (150, 8),
    (150, 1)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (150, 43),
    (150, 285),
    (150, 204)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 151 = Dippy Eggs #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (151, 818, "1 bunch of asparagus"),
    (151, 591, "4 large free-range eggs"),
    (151, 3, "sea salt"),
    (151, 780, "freshly ground black pepper"),
    (151, 29, "crusty bread")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (151, 16),
    (151, 8),
    (151, 11)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (151, 186),
    (151, 9),
    (151, 222)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

################################# RECIPE ID = 152 = Giant veg rosti #################################
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (152, 820, "600 g potatoes"),
    (152, 815, "3 large carrots"),
    (152, 919, "\u00bd teaspoon Dijon mustard"),
    (152, 441, "\u00bd a lemon"),
    (152, 865, "extra virgin olive oil"),
    (152, 864, "olive oil"),
    (152, 565, "100 g frozen peas"),
    (152, 828, "100 g baby spinach"),
    (152, 591, "4 large free-range eggs"),
    (152, 159, "50 g feta cheese")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (152, 16),
    (152, 9),
    (152, 11)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (152, 272),
    (152, 5),
    (152, 337)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()

cursor.close()