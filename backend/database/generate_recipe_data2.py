# recipe id 32 - 60 
# recipe id 111 - 131

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
        (43, 919, "2 heaped teaspoons Dijon mustard"),
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

############### 46: Spring Chicken Stew ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (46, 864, "olive oil"),
        (46, 874, "2 rashers of higher-welfare smoked streaky bacon"),
        (46, 527, "2 sprigs of fresh rosemary"),
        (46, 796, "2 onions"),
        (46, 815, "2 carrots"),
        (46, 820, "400 g new potatoes"),
        (46, 125, "100 g pearl barley"),
        (46, 146, "1 heaped tablespoon plain wholemeal flour"),
        (46, 887, "500 ml organic chicken stock"),
        (46, 179, "500 ml semi-skimmed milk"),
        (46, 875, "2 courgettes"),
        (46, 818, "1 bunch of asparagus (350g)"),
        (46, 790, "200 g green beans"), 
        (46, 594, "4 x 120 g free-range skinless chicken breasts"),
        (46, 525, "1 tablespoon mint sauce")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (46, 9),
        (46, 18),
        (46, 20)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (46, 116),
        (46, 272),
        (46, 215)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 47: Beef Brisket with Red Wine & Shallots ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (47, 797, "12 shallots"),
        (47, 522, "6 cloves of garlic"),
        (47, 865, "2 tablespoons extra virgin olive oil"),
        (47, 592, "1.5 kg brisket of beef rolled and tied"),
        (47, 777, "1 whole nutmeg for grating"),
        (47, 811, "1 x 400 g tin of chopped tomatoes"),
        (47, 860, "2 tablespoons tomato pur\u00e9e"),
        (47, 111, "250 ml red wine"),
        (47, 876, "2 fresh bay leaves"),
        (47, 771, "1 stick of cinnamon"),
        (47, 673, "1 small handful of black olives"),
        (47, 778, "1 teaspoon dried oregano"),
        (47, 532, "a few sprigs of fresh thyme"), 
        (47, 687, "2 tablespoons red wine vinegar")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (47, 9),
        (47, 18),
        (47, 20)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (47, 11)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 48: Curried Fish Stew ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (48, 870, "6 spring onions"),
        (48, 869, "1 fresh red chilli"),
        (48, 774, "5 cm piece of ginger"),
        (48, 864, "olive oil"),
        (48, 534, "1 handful of curry leaves"),
        (48, 903, "1 teaspoon black mustard seeds"),
        (48, 782, "1 level teaspoon ground turmeric"),
        (48, 904, "\u00bd teaspoon chilli powder"),
        (48, 905, "\u00bd teaspoon cumin seeds"),
        (48, 882, "\u00bd teaspoon fennel seeds"),
        (48, 737, "12 large raw shell-on king prawns from sustainable sources"),
        (48, 147, "300 g brown rice"),
        (48, 459, "250 g ripe mixed-colour cherry tomatoes"), 
        (48, 77, "1 x 400 g tin of light coconut milk"),
        (48, 238, "6 x 100 g white fish fillets such as bream or haddock, skin on, scaled and pin-boned, from sustainable sources"),
        (48, 78, "1 lemon"),
        (48, 906, "12 uncooked poppadoms")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (48, 2),
        (48, 9),
        (48, 18),
        (48, 20)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (48, 302),
        (48, 16),
        (48, 18),
        (48, 121)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 49: Sweet and Sour Rabbit ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (49, 626, "1 whole rabbit (1.2kg) skinned, jointed, with offal"),
        (49, 864, "olive oil"),
        (49, 830, "1 red onion"),
        (49, 459, "5 ripe cherry tomatoes"),
        (49, 869, "1 fresh red chilli"),
        (49, 876, "5 fresh bay leaves"),
        (49, 908, "50 g pine nuts"),
        (49, 640, "50 g blanched almonds"),
        (49, 772, "\u00bd teaspoon ground cloves"),
        (49, 111, "150 ml full-bodied Sicilian red wine"),
        (49, 866, "100 ml thick balsamic vinegar"),
        (49, 681, "1 tablespoon runny honey")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (49, 1),
        (49, 9),
        (49, 18),
        (49, 13),
        (49, 14)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (49, 131),
        (49, 27)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 50: Mushroom Bourguignon ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (50, 797, "12 shallots"),
        (50, 499, "25 g dried porcini mushrooms"),
        (50, 499, "4 portobello mushrooms"),
        (50, 499, "120 g shiitake mushrooms"),
        (50, 499, "200 g chestnut mushrooms"),
        (50, 148, "25 g unsalted butter"),
        (50, 815, "2 large carrots"),
        (50, 522, "2 cloves of garlic"),
        (50, 532, "6 sprigs of fresh thyme"),
        (50, 876, "2 fresh bay leaves"),
        (50, 111, "500 ml red wine"),
        (50, 860, "1 tablespoon tomato pur\u00e9e")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (50, 5),
        (50, 9),
        (50, 18),
        (50, 11),
        (50, 13)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (50, 152),
        (50, 201),
        (50, 24),
        (50, 215)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 51: Balinese Pork Stew ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (51, 897, "750 g skinless boneless higher-welfare pork belly cut into finger-length strips"),
        (51, 897, "750 g higher-welfare pork belly ribs halved"),
        (51, 864, "olive oil"),
        (51, 790, "300 g Chinese long beans or green beans"),
        (51, 472, "300 g pattypan squash"),
        (51, 800, "\u00bd a Chinese cabbage"),
        (51, 213, "7 lime leaves"),
        (51, 77, "2 x 400 g tins of light coconut milk"),
        (51, 129, "500 g jasmine rice"),
        (51, 442, "4 limes"),
        (51, 782, "20 g fresh turmeric"),
        (51, 774, "80 g galangal or ginger"),
        (51, 797, "500 g small Thai shallots"), 
        (51, 522, "1 bulb of garlic"),
        (51, 869, "4 fresh red bird's-eye chillies"),
        (51, 869, "3 fresh red chillies"),
        (51, 646, "5 candlenuts or macadamia nuts"),
        (51, 780, "1 tablespoon each of black and white peppercorns"),
        (51, 4, "50 g palm sugar"),
        (51, 912, "1 teaspoon shrimp paste"),
        (51, 211, "2 sticks lemongrass"),
        (51, 498, "coconut oil")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (51, 9),
        (51, 20),
        (51, 13),
        (51, 14)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (51, 259),
        (51, 126),
        (51, 217),
        (51, 291),
        (51, 131)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 52: Morrocan Lamb Stew ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (52, 527, "1 bunch of fresh rosemary"),
        (52, 774, "10 cm piece of ginger"),
        (52, 905, "\u00bd teaspoon cumin seeds"),
        (52, 861, "1 tablespoon coriander seeds"),
        (52, 882, "1 teaspoon fennel seeds"),
        (52, 869, "3-4 small dried chillies"),
        (52, 865, "extra virgin olive oil"),
        (52, 596, "4 small quality lamb neck fillets"),
        (52, 817, "4 sweet potatoes"),
        (52, 830, "2 red onions"),
        (52, 522, "4 cloves of garlic"),
        (52, 811, "12 ripe plum tomatoes"),
        (52, 771, "1 cinnamon stick"), 
        (52, 876, "2 bay leaves"),
        (52, 366, "1 handful of dried apricots"),
        (52, 923, "350 g couscous"),
        (52, 687, "red or white wine vinegar"),
        (52, 517, "1 big bunch of fresh coriander"),
        (52, 180, "4 tablespoons fat-free natural yoghurt")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (52, 9),
        (52, 20),
        (52, 17)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (52, 46),
        (52, 206),
        (52, 125)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 53: Beef Stroganoff ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (53, 830, "1 red onion"),
        (53, 522, "1 clove of garlic"),
        (53, 441, "1 lemon"),
        (53, 499, "2 handfuls of wild mushrooms"),
        (53, 779, "2-3 sprigs of fresh flat-leaf parsley"),
        (53, 592, "500 g fillet steak"),
        (53, 890, "1 teaspoon paprika"),
        (53, 864, "olive oil"),
        (53, 148, "1 knob of unsalted butter"),
        (53, 83, "1 small glass of brandy"),
        (53, 184, "50 ml sour cream")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (53, 8),
        (53, 18),
        (53, 20),
        (53, 13)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (53, 336),
        (53, 338),
        (53, 331)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 54: Oxtail Stew ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (54, 146, "50 g plain flour"),
        (54, 627, "2.5 kg quality trimmed oxtail, cut into rounds (ask your butcher to do this)"),
        (54, 797, "500 g shallots"),
        (54, 522, "4 cloves of garlic"),
        (54, 774, "5-6 5cm pieces of ginger"),
        (54, 864, "olive oil"),
        (54, 772, "1 teaspoon ground cloves"),
        (54, 777, "1 whole nutmeg for grating"),
        (54, 396, "1 large orange or 2-3 strips of dried orange peel"),
        (54, 379, "1 punnet of dates (soft, such as medjool, or semi-dried work best)"),
        (54, 866, "balsamic or sherry vinegar"),
        (54, 843, "1 large bunch of kale"),
        (54, 874, "3 thick slices of streaky bacon"),
        (54, 869, "1 fresh red chilli or to taste")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (54, 10),
        (54, 18),
        (54, 17),
        (54, 14)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (54, 217),
        (54, 291)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 55: Mexican-style roasted veg ragu ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (55, 817, "2 sweet potatoes"),
        (55, 474, "300 g butternut squash or pumpkin"),
        (55, 815, "2 carrots"),
        (55, 588, "150 g frozen sweetcorn"),
        (55, 861, "1 tablespoon coriander seeds"),
        (55, 778, "\u00bd tablespoon dried oregano"),
        (55, 864, "olive oil"),
        (55, 796, "2 onions"),
        (55, 522, "2 cloves of garlic"),
        (55, 869, "1 fresh red chilli"),
        (55, 809, "1 green pepper"),
        (55, 770, "2 sticks of celery"),
        (55, 562, "2 x 400 g tins of black beans"),
        (55, 811, "1 x 400 g tin of quality plum tomatoes"),
        (55, 525, "1 bunch of fresh mint (30g)"),
        (55, 870, "8 spring onions"),
        (55, 442, "4 limes"),
        (55, 916, "1-2 teaspoons chipotle Tabasco sauce"),
        (55, 147, "300 g brown rice")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (55, 9),
        (55, 11),
        (55, 12),
        (55, 13),
        (55, 14),
        (55, 20)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (55, 287),
        (55, 281),
        (55, 250),
        (55, 227),
        (55, 317),
        (55, 336)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 56: Sweetcorn and mussel chowder ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (56, 864, "olive oil"),
        (56, 874, "2 rashers higher-welfare bacon chopped"),
        (56, 796, "1 small white onion finely chopped"),
        (56, 770, "2 sticks celery finely chopped"),
        (56, 869, "1 fresh red chilli deseeded and finely chopped"),
        (56, 588, "4 ears sweetcorn"),
        (56, 820, "2 medium potatoes peeled and chopped"),
        (56, 886, "900 ml organic vegetable or fish stock hot"),
        (56, 883, "1 handful fresh, live mussels from sustainable sources, ask your fishmonger, cleaned and drained"),
        (56, 184, "4 tablespoons single cream"),
        (56, 779, "1 small handful chopped fresh parsley")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (56, 8),
        (56, 13),
        (56, 18)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (56, 261),
        (56, 131),
        (56, 272),
        (56, 260),
        (56, 110)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 57: Incredible Sicilian aubergine stew (Caponata) ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (57, 827, "2 large aubergines"),
        (57, 830, "1 small red onion"),
        (57, 522, "2 cloves of garlic"),
        (57, 779, "\u00bd a bunch fresh flat-leaf parsley (15g)"),
        (57, 538, "2 tablespoons salted capers"),
        (57, 673, "1 handful of green olives"),
        (57, 811, "5 large ripe tomatoes"),
        (57, 864, "olive oil"),
        (57, 778, "1 heaped teaspoon dried oregano"),
        (57, 687, "2-3 tablespoons best-quality herb vinegar"),
        (57, 640, "2 tablespoons slivered almonds")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (57, 8),
        (57, 1),
        (57, 11),
        (57, 12),
        (57, 13),
        (57, 14),
        (57, 20),
        (57, 18)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (57, 49),
        (57, 19),
        (57, 338),
        (57, 27),
        (57, 336)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 58: Jools simple chicken and veg stew ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (58, 793, "2 medium leeks"),
        (58, 815, "2 carrots"),
        (58, 770, "2 sticks of celery"),
        (58, 522, "2 cloves of garlic"),
        (58, 532, "3 sprigs of fresh thyme"),
        (58, 874, "3 rashers of higher-welfare smoked streaky bacon"),
        (58, 864, "olive oil"),
        (58, 913, "200 g celeriac"),
        (58, 816, "2 parsnips"),
        (58, 820, "6 new potatoes"),
        (58, 594, "8 free-range chicken thighs skin off, bone out"),
        (58, 921, "1 heaped teaspoon Marmite"),
        (58, 886, "600 ml organic vegetable stock")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (58, 9),
        (58, 14),
        (58, 17)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (58, 8),
        (58, 215),
        (58, 226),
        (58, 261)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 59: Simon Pegg's lamb tagine ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (59, 781, "1 large pinch of saffron"),
        (59, 922, "8 dried prunes (stone in)"),
        (59, 796, "2 onions"),
        (59, 522, "2 cloves of garlic"),
        (59, 774, "1 teaspoon ground ginger"),
        (59, 864, "olive oil"),
        (59, 771, "1 stick of cinnamon"),
        (59, 596, "750 g diced lamb shoulder"),
        (59, 875, "12 mixed-colour baby courgettes"),
        (59, 815, "300 g mixed-colour baby carrots"),
        (59, 474, "\u00bd a butternut squash (600g)"),
        (59, 923, "250 g couscous"),
        (59, 772, "2 cloves"),
        (59, 112, "2 tablespoons rose harissa"),
        (59, 180, "250 g natural yoghurt"),
        (59, 525, "\u00bd a bunch of fresh mint (15g)")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (59, 10),
        (59, 18),
        (59, 20)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (59, 328),
        (59, 291),
        (59, 215),
        (59, 250),
        (59, 333)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 60: Jools sausage & smoky bean casserole ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (60, 599, "12 higher-welfare pork chipolatas"),
        (60, 793, "2 medium leeks"),
        (60, 770, "2 sticks of celery"),
        (60, 522, "2 cloves of garlic"),
        (60, 809, "2 red peppers"),
        (60, 864, "olive oil"),
        (60, 890, "2 teaspoons sweet smoked paprika"),
        (60, 773, "1 teaspoon ground cumin"),
        (60, 459, "12 ripe cherry tomatoes"),
        (60, 687, "1 tablespoon red wine vinegar"),
        (60, 860, "500 ml passata"),
        (60, 4, "1 teaspoon demerara sugar optional"),
        (60, 919, "1 teaspoon Dijon mustard"),
        (60, 562, "2 x 400 g tins of mixed beans"),
        (60, 779, "a few sprigs of fresh flat-leaf parsley optional")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (60, 9),
        (60, 17),
        (60, 18),
        (60, 14)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (60, 8),
        (60, 261),
        (60, 91),
        (60, 336),
        (60, 49)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 111: Super Green Smoothie ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (111, 369, "1 ripe banana"),
        (111, 364, "1 apple"),
        (111, 828, "80 g baby spinach"),
        (111, 128, "60 g porridge oats"),
        (111, 179, "300 ml semi-skimmed milk"),
        (111, 684, "2 tablespoons almond butter or peanut butter"),
        (111, 924, "1 handful of ice cubes")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (111, 23),
        (111, 11),
        (111, 8)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (111, 60),
        (111, 50)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 112: Almond, banana & passion fruit smoothie ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (112, 369, "1 large ripe banana"),
        (112, 893, "500 ml almond milk"),
        (112, 640, "1 teaspoon almond essence optional"),
        (112, 400, "4 ripe passion fruit")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (112, 23),
        (112, 11),
        (112, 14),
        (112, 8)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (112, 50)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 113: Grapefruit, carrot & apple juice ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (113, 439, "\u00bd a grapefruit"),
        (113, 364, "1 apple"),
        (113, 815, "3 medium carrots")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (113, 23),
        (113, 11),
        (113, 12),
        (113, 13),
        (113, 14),
        (113, 8)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (113, 50),
        (113, 215)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 114: Grapefruit, carrot & apple juice ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (114, 435, "500 g strawberries"),
        (114, 525, "1 sprig of fresh mint"),
        (114, 924, "ice cubes"),
        (114, 441, "1 lemon"),
        (114, 4, "1 teaspoon golden caster suger")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (114, 23),
        (114, 11),
        (114, 12),
        (114, 13),
        (114, 14),
        (114, 8)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (114, 145)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 115: Mango Lassi ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (115, 768, "6 green cardamom pods optional"),
        (115, 392, "2 ripe mangos"),
        (115, 180, "500 g low-fat natural yoghurt"),
        (115, 924, "100 g ice cubes"),
        (115, 681, "runny honey optional")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (115, 23),
        (115, 11),
        (115, 13),
        (115, 8)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

# insert_SkillVideoInRecipe_qry = '''
#     INSERT INTO
#         SkillVideoInRecipe(recipe_id, skill_video_id)
#     VALUES
#         ()
# '''
# cursor.execute(insert_SkillVideoInRecipe_qry)
# conn.commit()

############### 116: Oat, pear & cardamom smoothie ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (116, 404, "2 pears"),
        (116, 768, "6 cardamom pods"),
        (116, 925, "500 ml oat milk"),
        (116, 180, "100 g natural yoghurt"),
        (116, 681, "2 teaspoons runny honey")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (116, 23),
        (116, 11),
        (116, 8)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (116, 251),
        (116, 266)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 117: Super smoothie ice lollies ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (117, 369, "1 small ripe banana"),
        (117, 926, "1 mug of fresh or frozen berries (150g)"),
        (117, 174, "1 mug of milk (300ml)"),
        (117, 180, "3 tablespoons natural yoghurt"),
        (117, 681, "1 tablespoon runny honey"),
        (117, 525, "6 mint leaves")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (117, 23),
        (117, 11),
        (117, 13),
        (117, 9)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (117, 50)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 118: Kiwi fruit, ginger and banana smoothie ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (118, 388, "3 kiwi fruit"),
        (118, 128, "4 tablespoons organic porridge oats"),
        (118, 369, "1 banana"),
        (118, 924, "8 ice cubes"),
        (118, 174, "200 ml organic milk"),
        (118, 180, "250 g organic fat-free natural yoghurt"),
        (118, 774, "\u00bd cm piece fresh ginger finely grated"),
        (118, 681, "honey optional")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (118, 23),
        (118, 11),
        (118, 8)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (118, 50)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 119: Pomegranate, ginger & lime flavoured water ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (119, 447, "\u00bd pomegranate"),
        (119, 774, "2cm piece of ginger"),
        (119, 442, "1 lime"),
        (119, 924, "ice cubes")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (119, 23),
        (119, 11),
        (119, 12),
        (119, 13),
        (119, 14),
        (119, 8)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (119, 13),
        (119, 71)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 120: Frozen fruit smoothies ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (120, 369, "1 ripe banana"),
        (120, 926, "1 glass frozen fruit"),
        (120, 180, "2 heaped tablespoons natural yoghurt"),
        (120, 128, "1 small handful of oats"),
        (120, 664, "1 small handful of mixed nuts"),
        (120, 68, "1 glass of organic soya milk, skimmed milk or apple juice"),
        (120, 681, "honey to taste, optional")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (120, 23),
        (120, 11),
        (120, 8)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

insert_SkillVideoInRecipe_qry = '''
    INSERT INTO
        SkillVideoInRecipe(recipe_id, skill_video_id)
    VALUES
        (120, 78)
'''
cursor.execute(insert_SkillVideoInRecipe_qry)
conn.commit()

############### 121: Pink pepper negroni ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (121, 95, "25 ml Bombay Sapphire gin"),
        (121, 121, "25 ml Martini Rosso (red vermouth)"),
        (121, 927, "25 ml Campari or bitter liqueur"),
        (121, 780, "5 whole pink peppercorns"),
        (121, 396, "1 blood orange or regular orange")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (121, 23),
        (121, 11),
        (121, 12),
        (121, 14),
        (121, 9)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

# insert_SkillVideoInRecipe_qry = '''
#     INSERT INTO
#         SkillVideoInRecipe(recipe_id, skill_video_id)
#     VALUES
#         ()
# '''
# cursor.execute(insert_SkillVideoInRecipe_qry)
# conn.commit()

############### 122: Limoncello ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (122, 441, "3 Amalfi lemons"),
        (122, 69, "250 ml 95% pure gain alcohol"),
        (122, 4, "250 g granulated sugar")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (122, 23),
        (122, 11),
        (122, 12),
        (122, 13),
        (122, 14),
        (122, 9)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

# insert_SkillVideoInRecipe_qry = '''
#     INSERT INTO
#         SkillVideoInRecipe(recipe_id, skill_video_id)
#     VALUES
#         ()
# '''
# cursor.execute(insert_SkillVideoInRecipe_qry)
# conn.commit()

############### 123: Hot rummy lemonade ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (123, 774, "300 g ginger"),
        (123, 441, "6 lemons"),
        (123, 497, "1.5 litres fresh cloudy apple juice"),
        (123, 681, "runny honey"),
        (123, 96, "15 x 25 ml shots of Bacardi Oro")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (123, 23),
        (123, 9)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

# insert_SkillVideoInRecipe_qry = '''
#     INSERT INTO
#         SkillVideoInRecipe(recipe_id, skill_video_id)
#     VALUES
#         ()
# '''
# cursor.execute(insert_SkillVideoInRecipe_qry)
# conn.commit()

############### 124: Dry passion fruit daiquiri ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (124, 4, "caster sugar"),
        (124, 96, "50 ml Bacardi Superior rum"),
        (124, 442, "1 lime"),
        (124, 927, "10 ml Campari"),
        (124, 400, "1 passion fruit plus extra to serve")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (124, 23),
        (124, 9)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

# insert_SkillVideoInRecipe_qry = '''
#     INSERT INTO
#         SkillVideoInRecipe(recipe_id, skill_video_id)
#     VALUES
#         ()
# '''
# cursor.execute(insert_SkillVideoInRecipe_qry)
# conn.commit()

############### 125: Spiced Chai ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (125, 62, "4 English breakfast tea bags"),
        (125, 771, "2 cinnamon sticks"),
        (125, 772, "4 cloves"),
        (125, 774, "1 teaspoon ground ginger"),
        (125, 174, "600ml milk"),
        (125, 777, "1 whole nutmeg for grating"),
        (125, 681, "honey or maple or agave syrup")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (125, 23),
        (125, 11),
        (125, 13),
        (125, 8)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

# insert_SkillVideoInRecipe_qry = '''
#     INSERT INTO
#         SkillVideoInRecipe(recipe_id, skill_video_id)
#     VALUES
#         ()
# '''
# cursor.execute(insert_SkillVideoInRecipe_qry)
# conn.commit()

############### 126: Mulled Pear Ginger ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (126, 497, "2 litres cloudy apple juice"),
        (126, 774, "2 thumb-sized ginger pieces sliced"),
        (126, 404, "2 ripe pears sliced"),
        (126, 771, "2 cinnamon sticks plus extra to serve"),
        (126, 768, "4 cardamom pods"),
        (126, 4, "3 tablespoons light brown sugar"),
        (126, 442, "4 limes juice of"),
        (126, 442, "2 limes zest of"),
        (126, 96, "500 ml Bacardi Oro")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (126, 23),
        (126, 9)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

# insert_SkillVideoInRecipe_qry = '''
#     INSERT INTO
#         SkillVideoInRecipe(recipe_id, skill_video_id)
#     VALUES
#         ()
# '''
# cursor.execute(insert_SkillVideoInRecipe_qry)
# conn.commit()

############### 127: Blood Orange Mimosa ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (127, 396, "60ml blood orange juice fresh or from a carton (cold)"),
        (127, 117, "Prosecco top up"),
        (127, 396, "1 blood orange zest of")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (127, 23),
        (127, 9)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

# insert_SkillVideoInRecipe_qry = '''
#     INSERT INTO
#         SkillVideoInRecipe(recipe_id, skill_video_id)
#     VALUES
#         ()
# '''
# cursor.execute(insert_SkillVideoInRecipe_qry)
# conn.commit()

############### 128: Sangria Latina ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (128, 877, "2 large chunks of fresh watermelon aprrox 150g, plus extra to garnish"),
        (128, 442, "1 lime"),
        (128, 774, "50 ml ginger syrup"),
        (128, 96, "300 ml Bacardi Carta Blanco"),
        (128, 117, "Martini Prosecco"),
        (128, 924, "ice cubed"),
        (128, 877, "watermelon segment")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (128, 23),
        (128, 11),
        (128, 12),
        (128, 13),
        (128, 14),
        (128, 9)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

# insert_SkillVideoInRecipe_qry = '''
#     INSERT INTO
#         SkillVideoInRecipe(recipe_id, skill_video_id)
#     VALUES
#         ()
# '''
# cursor.execute(insert_SkillVideoInRecipe_qry)
# conn.commit()

############### 129: Bloody Mary ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (129, 120, "2 parts Grey Goose vodka"),
        (129, 79, "4 parts organic tomato juice"),
        (129, 78, "\u00bd part of lemon juice (to taste)"),
        (129, 930, "4 dashes of Worcestershire sauce"),
        (129, 916, "4 dashes of Tabasco (or hot pepper sauce)"),
        (129, 3, "1 pinch of fleur de sel (or sea salt)"),
        (129, 780, "1 pinch of black pepper"),
        (129, 770, "1 stick of celery"),
        (129, 519, "1 bunch of aromatic herbs"),
        (129, 924, "ice cubed")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (129, 23),
        (129, 11),
        (129, 12),
        (129, 14),
        (129, 9)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

# insert_SkillVideoInRecipe_qry = '''
#     INSERT INTO
#         SkillVideoInRecipe(recipe_id, skill_video_id)
#     VALUES
#         ()
# '''
# cursor.execute(insert_SkillVideoInRecipe_qry)
# conn.commit()

############### 130: Chirstmas Pudding Vodka ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (130, 775, "1 piece of blade mace"),
        (130, 771, "2 sticks of cinnamon"),
        (130, 783, "2 teaspoons ground mixed spice"),
        (130, 441, "1 lemon"),
        (130, 396, "1 orange"),
        (130, 375, "300 g currants"),
        (130, 202, "200 g chopped mixed peel"),
        (130, 4, "450 g light muscovado sugar"),
        (130, 120, "1 litre quality vodka")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (130, 23),
        (130, 9)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

# insert_SkillVideoInRecipe_qry = '''
#     INSERT INTO
#         SkillVideoInRecipe(recipe_id, skill_video_id)
#     VALUES
#         ()
# '''
# cursor.execute(insert_SkillVideoInRecipe_qry)
# conn.commit()

############### 131: Elderflower lemonade with frozen berries ###############
insert_IngredientInRecipe_qry = '''
    INSERT INTO 
        IngredientInRecipe(recipe_id, ingredient_id, description)
    VALUES
        (131, 441, "2 lemons"),
        (131, 4, "caster sugar"),
        (131, 381, "35 ml elderflower cordial"),
        (131, 926, "1 handful of frozen berries"),
        (131, 8, "sparkling water to top up")
'''
cursor.execute(insert_IngredientInRecipe_qry)
conn.commit()

insert_TagInRecipe_qry = '''
    INSERT INTO
        TagInRecipe(recipe_id, tag_id)
    VALUES
        (131, 23),
        (131, 9)
'''
cursor.execute(insert_TagInRecipe_qry)
conn.commit()

# insert_SkillVideoInRecipe_qry = '''
#     INSERT INTO
#         SkillVideoInRecipe(recipe_id, skill_video_id)
#     VALUES
#         ()
# '''
# cursor.execute(insert_SkillVideoInRecipe_qry)
# conn.commit()


cursor.close()