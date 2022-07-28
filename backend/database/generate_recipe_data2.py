# recipe id 32 - 60
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

############### 32: Buddy's Bolognese ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (32, 879, "2 free-range pork sausages"),
        (32, 864, "olive oil"),
        (32, 880, "500 g lean beef mince"),
        (32, 796, "2 onions"),
        (32, 522, "2 cloves of garlic"),
        (32, 815, "1 large carrot"),
        (32, 770, "1 stick of celery"),
        (32, 875, "1 courgette"),
        (32, 866, "2 tablespoons thick balsamic vinegar"),
        (32, 811, "2 x 400 g tins of plum tomatoes"),
        (32, 860, "1 heaped teaspoon tomato puree"),
        (32, 35, "450 g dried spaghetti"),
        (32, 165, "Parmesan cheese to serve")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (32, 1),
        (32, 9),
        (32, 18),
        (32, 20)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (32, 115)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 33: Rotolo of spinach, squash & ricotta ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (33, 35, "450 g fresh egg pasta dough"),
        (33, 474, "Half a butternut squash"),
        (33, 864, "olive oil"),
        (33, 861, "1 teaspoon coriander seeds"),
        (33, 881, "1 teaspoon fennel seeds"),
        (33, 869, "Half a dried red chilli"),
        (33, 778, "1 handful of fresh marjoram or oregano"),
        (33, 522, "2 cloves of garlic"),
        (33, 828, "800 g spinach"),
        (33, 148, "250 g unsalted butter"),
        (33, 777, "1 whole nutmeg for grating"),
        (33, 182, "150 g crumbly ricotta cheese"),
        (33, 165, "50 g Parmesan cheese plus extra for serving"),
        (33, 528, "20 fresh sage leaves")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (33, 1),
        (33, 9),
        (33, 18),
        (33, 20)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (33, 115),
        (33, 250)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 34: Quick Seafood Pasta ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (34, 35, "300 g dried linguine"),
        (34, 742, "250 g squid gutted, cleaned, from sustainable sources"),
        (34, 882, "250 g mussels scrubbed, debearded, from sustainable sources"),
        (34, 729, "250 g cockles or clams scrubbed, from sustainable sources"),
        (34, 738, "4 scallops with roe attached from sustainable sources"),
        (34, 522, "1 clove of garlic"),
        (34, 779, "1 bunch of fresh flat-leaf parsley (30g)"),
        (34, 441, "1 lemon"),
        (34, 869, "1 fresh red chilli optional"),
        (34, 864, "olive oil"),
        (34, 538, "1 tablespoon baby capers"),
        (34, 883, "1 handful of samphire optional"),
        (34, 811, "1 x 400 g tin of quality plum tomatoes"),
        (34, 165, "20 g Parmesan cheese"),
        (34, 865, "extra virgin olive oil")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (34, 1),
        (34, 9),
        (34, 18),
        (34, 20)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (34, 115),
        (34, 110),
        (34, 7),
        (34, 8),
        (34, 110),
        (34, 49)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 35: Epic Vegan Lasagne ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (35, 499, "20 g dried porcini mushrooms"),
        (35, 830, "2 large red onions"),
        (35, 522, "6 cloves of garlic"),
        (35, 815, "2 carrots"),
        (35, 770, "2 sticks of celery"),
        (35, 527, "2 sprigs of fresh rosemary"),
        (35, 864, "olive oil"),
        (35, 863, "1 teaspoon dried chilli flakes"),
        (35, 876, "2 fresh bay leaves"),
        (35, 111, "100 ml vegan Chianti wine"),
        (35, 572, "1 x 400 g tin of green lentils"),
        (35, 811, "2 x 400 g tins of quality plum tomatoes"),
        (35, 499, "750 g mixed wild mushrooms"),
        (35, 532, "Half a bunch of fresh thyme (15g)"),
        (35, 139, "2 slices of sourdough (100g)"), 
        (35, 153, "70 g vegan Cheddar cheese"), 
        (35, 528, "Half a bunch of fresh sage (15g)"), 
        (35, 865, "extra virgin olive oil"), 
        (35, 145, "400 g durum wheat flour or fine semolina flour, plus extra for dusting"), 
        (35, 146, "4 heaped tablespoons plain flour"), 
        (35, 893, "800 ml almond milk")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (35, 1),
        (35, 9),
        (35, 18),
        (35, 20),
        (35, 11),
        (35, 12)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (35, 115),
        (35, 46),
        (35, 19),
        (35, 11)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 36: Potato Gnocchi ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (36, 820, "1 kg floury potatoes such as Maris Piper, King Edward"),
        (36, 146, "100 g Tipo 00 flour plus extra for dusting"),
        (36, 777, "1 whole nutmeg for grating")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (36, 1),
        (36, 9)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (36, 193)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 37: Ultimate Mushroom Risotto ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (37, 796, "1 onion"),
        (37, 770, "2 sticks of celery"),
        (37, 864, "olive oil"),
        (37, 532, "1 bunch of fresh thyme (30g)"),
        (37, 499, "20 g dried porcini mushrooms"),
        (37, 499, "350 g mixed mushrooms such as chestnut, button, wild, shiitake"),
        (37, 886, "1.2 litres organic vegetable stock"),
        (37, 129, "300 g Arborio risotto rice"),
        (37, 117, "125 ml white wine"),
        (37, 165, "40 g Parmesan or vegetarian hard cheese"),
        (37, 148, "20 g unsalted butter"),
        (37, 645, "30 g blanched hazelnuts"),
        (37, 441, "1 lemon"),
        (37, 180, "4 tablespoons natural yoghurt"), 
        (37, 865, "extra virgin olive oil"), 
        (37, 828, "100 g baby spinach")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (37, 1),
        (37, 9),
        (37, 20),
        (37, 11),
        (37, 13),
        (37, 18)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (37, 100),
        (37, 61),
        (37, 194)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 38: Sausage Pasta Bake ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (38, 522, "3 cloves of garlic"),
        (38, 153, "50 g mature Cheddar cheese"),
        (38, 29, "50 g stale bread"),
        (38, 778, "2 teaspoons dried oregano"),
        (38, 864, "olive oil"),
        (38, 879, "4 higher-welfare sausages"),
        (38, 863, "1 pinch of dried chilli flakes"),
        (38, 811, "3 x 400 g tins of quality plum tomatoes"),
        (38, 35, "400 g dried rigatoni")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (38, 1),
        (38, 8),
        (38, 20)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (38, 115),
        (38, 336),
        (38, 212)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 39: Chicken Paella ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (39, 888, "400 g quality chorizo"),
        (39, 796, "1 small onion"),
        (39, 889, "50 g jarred piquillo peppers"),
        (39, 779, "Half a bunch of fresh flat-leaf parsley"),
        (39, 594, "22 free-range chicken drumettes"),
        (39, 865, "2 tablespoons extra virgin olive oil"),
        (39, 890, "1 teaspoon smoked paprika"),
        (39, 860, "2 tablespoon tomato puree"),
        (39, 129, "400 g Bomba paella rice"),
        (39, 117, "120 ml white wine"),
        (39, 887, "750 ml organic chicken stock"),
        (39, 565, "200 g frozen peas"),
        (39, 441, "1 lemon")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (39, 9),
        (39, 20),
        (39, 14)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (39, 49),
        (39, 19)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 40: Spaghetti Aglio Olio & Spring Greens ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (40, 522, "2 cloves of garlic"),
        (40, 869, "1 fresh red chilli"),
        (40, 828, "1 head of spring greens"),
        (40, 35, "400 g dried spaghetti"),
        (40, 865, "extra virgin olive oil"),
        (40, 441, "1 large unwaxed lemon"),
        (40, 165, "Parmesan cheese")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (40, 1),
        (40, 8),
        (40, 20), 
        (40, 11)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (40, 336),
        (40, 115),
        (40, 194)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 41: Spaghetti Carbonara ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (41, 591, "3 large free-range egg yolks"),
        (41, 165, "40 g Parmesan cheese plus extra to serve"),
        (41, 599, "1 x 150 g piece of higher-welfare pancetta"),
        (41, 35, "200 g dried spaghetti"),
        (41, 522, "1 clove of garlic"),
        (41, 865, "extra virgin olive oil")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (41, 8),
        (41, 1), 
        (41, 20)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (41, 15),
        (41, 115),
        (41, 323)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 42: Vegan Mac and Cheese ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (42, 682, "350 g dried macaroni"),
        (42, 3, "sea salt"),
        (42, 780, "freshly ground black pepper"),
        (42, 796, "1 onion"),
        (42, 68, "1 litre unsweetened organic soya milk"),
        (42, 21, "100 g dairy-free margarine"),
        (42, 146, "85 g plain flour"),
        (42, 803, "1 heaped teaspoon English mustard"),
        (42, 892, "1\u00bd tablespoons nutritional yeast flakes"),
        (42, 150, "50 g vegan cheese optional (available from specialist stores)"),
        (42, 522, "5 cloves of garlic"),
        (42, 532, "\u00bd a bunch of fresh thyme"),
        (42, 864, "olive oil"), 
        (42, 29, "40 g fresh breadcrumbs")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (42, 8),
        (42, 12), 
        (42, 11),
        (42, 14)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (42, 336),
        (42, 61),
        (42, 115)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 43: Meatballs and Pasta ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (43, 36, "12 Jacob's cream crackers"),
        (43, 527, "4 sprigs of fresh rosemary"),
        (43, 803, "2 heaped teaspoons Dijon mustard"),
        (43, 880, "500 g quality minced beef, pork, or a mixture of the two"),
        (43, 778, "1 heaped tablespoon dried oregano"),
        (43, 591, "1 large free-range egg"),
        (43, 864, "olive oil"),
        (43, 513, "1 bunch of fresh basil"),
        (43, 796, "1 medium onion"),
        (43, 522, "2 cloves of garlic"),
        (43, 869, "\u00bd a fresh or dried red chilli"),
        (43, 811, "2 x 400 g tin of plum tomatoes"),
        (43, 866, "2 tablespoons balsamic vinegar"), 
        (43, 35, "400 g dried spaghetti or penne"),
        (43, 165, "Parmesan cheese")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (43, 1),
        (43, 9),
        (43, 18),
        (43, 20)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (43, 46),
        (43, 258),
        (43, 115)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 44: Pasta with Aubergine and Tomato Sauce ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (44, 796, "1 small onion"),
        (44, 522, "2 cloves of garlic"),
        (44, 513, "\u00bd a bunch of fresh basil"),
        (44, 827, "2 aubergines"),
        (44, 864, "4-6 tablespoons olive oil"),
        (44, 811, "1 x 400 g tin of quality chopped tomatoes"),
        (44, 35, "500 g dried rigatoni"),
        (44, 182, "80 g ricotta cheese")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (44, 1),
        (44, 9),
        (44, 18),
        (44, 11)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (44, 336),
        (44, 258),
        (44, 245),
        (44, 19),
        (44, 115)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 45: Chicken, Sausage, & Prawn Jambalaya ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (45, 594, "4 free-range chicken thighs skin on"),
        (45, 594, "4 free-range chicken drumsticks skin on"),
        (45, 789, "cayenne pepper"),
        (45, 864, "olive oil"),
        (45, 879, "300 g quality smoked sausage, such as andouille or fresh iberico chorizo skin removed, cut into 1cm thick slices"),
        (45, 796, "1 large onion peeled and roughly chopped"),
        (45, 809, "1 green pepper deseeded and roughly chopped"),
        (45, 809, "1 red pepper deseeded and roughly chopped"),
        (45, 770, "4 sticks celery trimmed and roughly chopped"),
        (45, 876, "4 bay leaves"),
        (45, 532, "4 sprigs fresh thyme"),
        (45, 522, "6 cloves garlic peeled and sliced"),
        (45, 869, "1-2 fresh red chillies deseeded and finely chopped"), 
        (45, 811, "400 g tinned chopped tomatoes"),
        (45, 887, "1.5 litres organic chicken stock"),
        (45, 129, "700 g long-grain rice"),
        (45, 737, "16-20 raw king prawns from sustainable sources, ask your fishmonger, peeled and deveined"),
        (45, 779, "1 handful fresh curly parsley")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (45, 1),
        (45, 8),
        (45, 18),
        (45, 20),
        (45, 14),
        (45, 13)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (45, 336),
        (45, 91),
        (45, 92)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

cursor.close()