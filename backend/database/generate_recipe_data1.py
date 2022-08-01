# recipe id 3-31, 90-110
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

# BEAUTIFUL COURGETTE CARBONARA ID=3
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (3, 875, "6 medium green and yellow courgettes"),
    (3, 35, "500 g penne"),
    (3, 591, "4 large free-range eggs"),
    (3, 184, "100 ml single cream"),
    (3, 165, "1 small handful of Parmesan cheese"),
    (3, 864, "olive oil"),
    (3, 874, "6 slices of higher-welfare back bacon"),
    (3, 532, "\u00bd a bunch of fresh thyme (15g)")
"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (3, 1),
    (3, 9),
    (3, 15),
    (3, 20),
    (3, 17),
    (3, 18)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (3, 0),
    (3, 115),
    (3, 116)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# ROASTED PARSNIPS ID=4
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (4, 816, "1.5 kg medium parsnips"),
    (4, 148, "50 g unsalted butter"),
    (4, 876, "4 fresh bay leaves"),
    (4, 866, "1 tablespoon white or red wine vinegar"),
    (4, 681, "2 tablespoons runny honey")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (4, 8),
    (4, 11),
    (4, 13),
    (4, 15),
    (4, 19),
    (4, 22)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (4, 236)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# BUTTERFLIED PRAWN SKEWERS ID=5
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (5, 441, "2 lemons"),
    (5, 522, "3 cloves of garlic"),
    (5, 779, "1 bunch of fresh flat-leaf parsley (30g)"),
    (5, 864, "olive oil"),
    (5, 737, "320 g large raw shell-on king prawns from sustainable sources"),
    (5, 865, "extra virgin olive oil"),
    (5, 869, "\u00bd-1 fresh red chilli"),
    (5, 525, "\u00bd a bunch of fresh mint (15g)"),
    (5, 830, "\u00bd a red onion"),
    (5, 877, "1 small watermelon"),
    (5, 813, "1 cucumber"),
    (5, 159, "100 g feta"),
    (5, 874, "8 rashers of higher-welfare smoked pancetta or streaky bacon")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (5, 8),
    (5, 11),
    (5, 13),
    (5, 15),
    (5, 19),
    (5, 22)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (5, 139),
    (5, 155),
    (5, 302),
    (5, 319)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# BUDDY'S QUICK PIZZETTAS ID=6
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (6, 146, "350 g self-raising flour, plus extra for dusting"),
    (6, 864, "olive oil"),
    (6, 180, "250 g natural yoghurt"),
    (6, 522, "2 cloves of garlic"),
    (6, 811, "1 x 400 g tin of quality plum tomatoes"),
    (6, 513, "\u00bd a bunch of fresh basil (15g)"),
    (6, 869, "1 fresh red chilli"),
    (6, 153, "50 g Cheddar cheese"),
    (6, 165, "30 g Parmesan cheese"),
    (6, 163, "150 g mozzarella cheese"),
    (6, 499, "4 chestnut mushrooms"),
    (6, 595, "2 slices of higher-welfare cooked ham")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (6, 1),
    (6, 9),
    (6, 15),
    (6, 17),
    (6, 22)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (6, 105),
    (6, 193),
    (6, 194),
    (6, 212)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# FISH FINGER TACOS ID=7
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (7, 238, "1.2 kg white fish fillets skin off, pin-boned, from sustainable sources"),
    (7, 146, "100 g plain flour"),
    (7, 591, "2 large free-range eggs"),
    (7, 33, "250 g wholemeal bread"),
    (7, 864, "olive oil"),
    (7, 800, "\u00bc of a red cabbage (150g)"),
    (7, 687, "white wine vinegar"),
    (7, 585, "2 corn on the cob"),
    (7, 442, "1 lime"),
    (7, 865, "extra virgin olive oil"),
    (7, 40, "4 wholemeal tortillas"),
    (7, 180, "natural yoghurt or soured cream to serve")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (7, 7),
    (7, 9),
    (7, 17),
    (7, 18),
    (7, 20)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (7, 16),
    (7, 43),
    (7, 121)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# STRAWBERRY AND CREAM SANDWICH SPONGE ID=8
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (8, 148, "225 g unsalted butter (at room temperature) plus extra for greasing"),
    (8, 4, "225 g white caster sugar"),
    (8, 446, "1 teaspoon vanilla extract"),
    (8, 591, "4 large free-range eggs"),
    (8, 146, "225 g self-raising flour"),
    (8, 22, "1 teaspoon baking powder"),
    (8, 174, "1 splash of milk"),
    (8, 184, "200 ml double cream"),
    (8, 878, "1\u00bd tablespoon of icing sugar plus extra for dusting"),
    (8, 435, "250 g fresh strawberries")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (8, 9),
    (8, 11),
    (8, 15),
    (8, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (8, 44),
    (8, 43),
    (8, 174),
    (8, 129),
    (8, 145)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# CHAI SPICED CARROT CAKE ID=9
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (9, 17, "250 ml vegetable oil, plus extra for greasing"),
    (9, 815, "4 large carrots"),
    (9, 441, "1 large lemon"),
    (9, 375, "100 g currants or sultanas"),
    (9, 647, "100 g pecans"),
    (9, 146, "280 g plain flour"),
    (9, 22, "2 teaspoons baking powder"),
    (9, 774, "1 tablespoon ground ginger"),
    (9, 771, "1 tablespoon ground cinnamon"),
    (9, 768, "2 teaspoons ground cardamom"),
    (9, 772, "\u00bc teaspoon ground cloves"),
    (9, 764, "\u00bc teaspoon ground anise"),
    (9, 777, "\u00bc teaspoon ground nutmeg"),
    (9, 62, "1 black tea bag"),
    (9, 591, "2 large free-range eggs"),
    (9, 4, "200 g caster sugar, 200 g light brown sugar"),
    (9, 374, "30 g flaked coconut"),
    (9, 148, "200 g unsalted butter (at room temperature)"),
    (9, 156, "200 g cream cheese"),
    (9, 878, "125 g icing sugar")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (9, 9),
    (9, 11),
    (9, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (9, 215),
    (9, 111)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# RHUBARB AND CUSTARD TART ID=10
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (10, 146, "500 g plain flour"),
    (10, 878, "100 g icing sugar plus 1 teaspoon"),
    (10, 148, "250 g unsalted butter (cold)"),
    (10, 591, "3 large free-range eggs"),
    (10, 174, "500 ml whole milk"),
    (10, 446, "1 teaspoon vanilla bean paste"),
    (10, 17, "vegetable oil for greasing"),
    (10, 640, "50 g flaked almonds"),
    (10, 526, "1 kg rhubarb"),
    (10, 364, "500 g mixed eating apples"),
    (10, 4, "160 g golden caster sugar"),
    (10, 881, "3 level tablespoons custard powder"),
    (10, 446, "2 teaspoons vanilla bean paste")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (10, 9),
    (10, 11),
    (10, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (10, 43),
    (10, 44),
    (10, 60),
    (10, 211)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# LAMINGTONS ID=11
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (11, 148, "500 g unsalted butter (at room temperature), plus extra for greasing"),
    (11, 146, "250 g self-raising flour plus extra for dusting"),
    (11, 4, "250 g golden caster sugar"),
    (11, 591, "5 large free-range eggs"),
    (11, 174, "100 ml milk"),
    (11, 446, "\u00bd teaspoon vanilla extract"),
    (11, 22, "\u00bd teaspoon baking powder"),
    (11, 894, "250 g quality dark chocolate (70%)"),
    (11, 878, "100 g icing sugar"),
    (11, 374, "300 g desiccated coconut"),
    (11, 895, "1 x 340 g jar of quality raspberry jam")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (11, 9),
    (11, 11),
    (11, 15),
    (11, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (11, 43),
    (11, 174),
    (11, 240)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# CHOCOLATE ORANGE SHORTBREAD ID=12
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (12, 148, "150 g unsalted butter at room temperature"),
    (12, 146, "200 g plain flour"),
    (12, 4, "50 g golden caster sugar plus extra to sprinkle"),
    (12, 396, "1 orange"),
    (12, 894, "50 g quality dark chocolate (70%)")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (12, 9),
    (12, 11),
    (12, 15),
    (12, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (12, 240)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# ST CLEMENT'S SHORTBREAD ID=13
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (13, 148, "200 g unsalted butter (at room temperature) plus extra for greasing"),
    (13, 396, "1 orange"),
    (13, 441, "1 lemon"),
    (13, 4, "100 g caster sugar plus extra for sprinkling"),
    (13, 146, "300 g gluten-free flour"),
    (13, 891, "50 g rice flour"),
    (13, 22, "1 teaspoon baking powder")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (13, 9),
    (13, 11),
    (13, 15),
    (13, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (13, 240)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# CHOCOLATE CHIP MUFFINS ID=14
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (14, 864, "olive or rapeseed oil"),
    (14, 146, "375 g plain flour"),
    (14, 22, "1 tablespoon baking powder"),
    (14, 896, "\u00bd teaspoon baking soda"),
    (14, 148, "10 tablespoons unsalted butter"),
    (14, 4, "200 g sugar"),
    (14, 591, "2 large free-range eggs"),
    (14, 180, "360 ml natural yoghurt"),
    (14, 720, "2 generous handfuls of chocolate chips"),
    (14, 447, "1 splash of pomegranate juice"),
    (14, 878, "2 tablespoons icing sugar")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (14, 9),
    (14, 11),
    (14, 15),
    (14, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (14, 43),
    (14, 174),
    (14, 240)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# CRUSTADE (APPLE TART) ID=15
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (15, 364, "1 kg apples such as Golden Delicious or Chantecler"),
    (15, 86, "100 ml armagnac"),
    (15, 148, "55 g unsalted butter"),
    (15, 902, "12 sheets of filo pastry (270g)"),
    (15, 4, "115 g caster sugar plus extra for sprinkling"),
    (15, 446, "1 teaspoon vanilla sugar or a few drops of vanilla extract"),
    (15, 441, "1 lemon"),
    (15, 527, "1 small sprig of fresh rosemary")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (15, 9),
    (15, 11),
    (15, 15),
    (15, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (15, 60),
    (15, 211),
    (15, 223)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# ENGLISH MUFFINS ID=16
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (16, 174, "300 ml milk plus extra"),
    (16, 510, "1 x 7 g sachet of dried yeast"),
    (16, 4, "25 g white caster sugar"),
    (16, 638, "50 g shortening or lard"),
    (16, 146, "425 g plain flour plus extra"),
    (16, 148, "unsalted butter")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (16, 9),
    (16, 15),
    (16, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (16, 240)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# THE BEST COFFEE AND WALNUT CAKE ID=17
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (17, 148, "140 g butter (at room temperature) plus extra for greasing"),
    (17, 648, "75 g walnuts plus extra to garnish"),
    (17, 4, "175 g sugar"),
    (17, 591, "3 large free-range eggs"),
    (17, 146, "150 g self-raising flour"),
    (17, 896, "\u00bd teaspoon baking powder"),
    (17, 60, "170 ml espresso"),
    (17, 878, "225 g icing sugar")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (17, 9),
    (17, 11),
    (17, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (17, 133),
    (17, 98),
    (17, 43),
    (17, 174)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# SALTED CARAMEL BROWNIES ID=18
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (18, 148, "225 g butter plus extra for greasing, and 15 g salted butter"),
    (18, 894, "250 g dark chocolate (70% cocoa solids)"),
    (18, 4, "285 g caster sugar"),
    (18, 591, "4 large free-range eggs"),
    (18, 146, "150 g plain flour"),
    (18, 446, "\u00bc of a vanilla pod"),
    (18, 184, "40 ml double cream"),
    (18, 9, "40 g golden syrup")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (18, 9),
    (18, 11),
    (18, 15),
    (18, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (18, 174),
    (18, 43)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# PEAR AND GINGER PUDDING ID=19
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (19, 148, "55 g unsalted butter softened, plus extra for greasing"),
    (19, 146, "55 g self-raising flour"),
    (19, 4, "55 g caster sugar"),
    (19, 591, "1 large free-range egg"),
    (19, 774, "1 piece of stem ginger in syrup"),
    (19, 396, "1 orange"),
    (19, 404, "1 ripe pear"),
    (19, 9, "golden syrup or reserved ginger syrup")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (19, 9),
    (19, 11),
    (19, 15),
    (19, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (19, 251),
    (19, 266)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# PASSIO-BERRY CHOUX BUNS ID=20
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (20, 184, "125 ml double cream"),
    (20, 180, "125 ml Greek yoghurt"),
    (20, 400, "4 large passion fruit"),
    (20, 878, "250 g fondant icing sugar"),
    (20, 434, "300 g raspberries plus extra to serve"),
    (20, 4, "3 tablespoons and 1 teaspoon caster sugar"),
    (20, 441, "1 lemon"),
    (20, 148, "75 g butter"),
    (20, 591, "4 large free-range eggs and 3-4 medium free-range eggs"),
    (20, 446, "\u00bd teaspoon vanilla bean paste"),
    (20, 174, "75 ml whole milk"),
    (20, 146, "100 g plain flour")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (20, 9),
    (20, 11),
    (20, 15),
    (20, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (20, 174),
    (20, 43),
    (20, 15),
    (20, 148)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# VEGAN TOFFEE APPLE UPSIDE-DOWN CAKE ID=21
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (21, 21, "25 g vegan margarine plus extra for greasing"),
    (21, 364, "3 dessert apples"),
    (21, 4, "195 g muscovado sugar"),
    (21, 146, "180 g plain flour"),
    (21, 896, "1 teaspoon bicarbonate of soda"),
    (21, 783, "1\u00bd teaspoons mixed spice"),
    (21, 899, "80 ml sunflower oil"),
    (21, 687, "1 tesapoon vinegar"),
    (21, 441, "1 lemon"),
    (21, 648, "85 g shelled walnuts")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (21, 9),
    (21, 11),
    (21, 12),
    (21, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (21, 133),
    (21, 98),
    (21, 176)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# PINEAPPLE AND COCONUT CAKE ID=22
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (22, 408, "200 g fresh pineapple"),
    (22, 148, "110 g unsalted butter (at room temperature) plus extra for greasing"),
    (22, 4, "110 g caster sugar"),
    (22, 591, "2 large free-range eggs"),
    (22, 184, "250 ml sour cream"),
    (22, 146, "200 g self-raising flour plus extra for dusting"),
    (22, 896, "\u00bc tesapoon bicarbonate of soda"),
    (22, 374, "150 g desiccated coconut"),
    (22, 878, "1-2 tablespoons icing sugar")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (22, 8),
    (22, 11),
    (22, 15),
    (22, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (22, 43),
    (22, 174),
    (22, 55),
    (22, 57),
    (22, 65)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# LEMON AND PISTACHIO CANNOLI ID=23
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (23, 146, "300 g plain flour plus extra for dusting"),
    (23, 4, "50 g caster sugar"),
    (23, 896, "\u00bc teaspoon bicarbonate of soda"),
    (23, 771, "1 pinch of ground cinnamon"),
    (23, 441, "3 lemons and 1\u00bd tablespoons candied lemon peel"),
    (23, 111, "4 tablespoons marsala wine"),
    (23, 591, "1 large free-range egg"),
    (23, 148, "4 tablespoons butter"),
    (23, 899, "2 litres sunflower oil for frying"),
    (23, 878, "150 g icing sugar plus extra to serve"),
    (23, 182, "400 g ricotta cheese"),
    (23, 910, "150 g mascarpone cheese"),
    (23, 180, "150 g Greek-style yoghurt"),
    (23, 655, "75 g pistachios")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (23, 10),
    (23, 11),
    (23, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (23, 43),
    (23, 174),
    (23, 114)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# VANILLA YOGHURT PANNA COTTA ID=24
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (24, 7, "1 leaf of gelatine"),
    (24, 179, "200 ml semi-skimmed milk"),
    (24, 446, "\u00bd teaspoon vanilla bean paste"),
    (24, 180, "200 g natural yoghurt"),
    (24, 526, "200 g rhubarb"),
    (24, 681, "2 tablespoons runny honey plus extra to serve"),
    (24, 435, "300 g strawberries")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (24, 9),
    (24, 13),
    (24, 15),
    (24, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (24, 232),
    (24, 145),
    (24, 129)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# BANANA PANTTONE PUDDING ID=25
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (25, 148, "65 g soft unsalted butter plus extra for greasing"),
    (25, 771, "ground cinnamon"),
    (25, 4, "200 g golden caster sugar plus extra for sprinkling"),
    (25, 446, "3 teaspoons vanilla bean paste"),
    (25, 591, "3 large free-range eggs"),
    (25, 443, "3 clementines"),
    (25, 179, "600 ml semi-skimmed milk"),
    (25, 97, "optional: smooth whisky, brandy, golden rum"),
    (25, 369, "4 bananas"),
    (25, 379, "150 g Medjool dates"),
    (25, 909, "500 g panettone"),
    (25, 640, "15 g flaked almonds"),
    (25, 184, "150 ml single cream"),
    (25, 907, "vanilla ice cream to serve")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (25, 9),
    (25, 11),
    (25, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (25, 43),
    (25, 174),
    (25, 50)

"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# MANGO AND YOGHURT LAYER POTS ID=26
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (26, 392, "1 ripe mango"),
    (26, 446, "1 teaspoon vanilla extract"),
    (26, 180, "180 g natural yoghurt"),
    (26, 911, "100 g Granola Dust")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (26, 9),
    (26, 11),
    (26, 13),
    (26, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()


# Chocolate & avocado mousse ID=27
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (27, 894, "300 g quality dark chocolate (70%)"),
    (27, 367, "2 large ripe avocados"),
    (27, 719, "2 heaped teaspoons cocoa powder"),
    (27, 446, "2 teaspoons vanilla bean paste"),
    (27, 9, "3 tablespoons maple syrup"),
    (27, 928, "1 x 160 g tin of coconut cream"),
    (27, 396, "fresh fruit such as oranges, strawberries, blueberries, raspberries to serve"),
    (27, 425, "amarena cherries in syrup to serve, optional"),
    (27, 929, "white chocolate to serve, optional")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (27, 9),
    (27, 11),
    (27, 13),
    (27, 15),
    (27, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (27, 213),
    (27, 221),
    (27, 34)

"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# Vanilla custard ID=28
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (28, 446, "1 vanilla pod"),
    (28, 174, "600 ml whole milk"),
    (28, 591, "4 large free-range egg yolks"),
    (28, 4, "2 tablespoons caster sugar"),
    (28, 931, "1 tablespoon cornflour")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (28, 9),
    (28, 11),
    (28, 15),
    (28, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (28, 15),
    (28, 43),
    (28, 174)

"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# Classic apple crumble ID=29
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (29, 364, "1.5 kg mixed apples (I like to use half Bramley)"),
    (29, 4, "150 g golden caster sugar"),
    (29, 441, "1 lemon"),
    (29, 148, "50 g unsalted butter (cold)"),
    (29, 146, "100 g plain flour")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (29, 9),
    (29, 11),
    (29, 15),
    (29, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (29, 176),
    (29, 60),
    (29, 51),
    (29, 211),
    (29, 223)

"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# Simple chocolate tart ID=30
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (30, 184, "300 ml double cream"),
    (30, 4, "2 level tablespoons caster sugar"),
    (30, 894, "400 g quality dark chocolate (70%)"),
    (30, 148, "90 g unsalted butter at room temperature"),
    (30, 174, "100 ml milk"),
    (30, 932, "1 tart shell baked blind"),
    (30, 719, "quality cocoa powder for dusting")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (30, 9),
    (30, 11),
    (30, 15),
    (30, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()


# Ice-cream sandwiches ID=31
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (31, 174, "150 ml whole milk"),
    (31, 510, "\u00bd x 7 g sachet of dried yeast"),
    (31, 146, "300 g strong bread flour plus extra for dusting"),
    (31, 933, "200 g Tipo 00 flour"),
    (31, 4, "60 g golden caster sugar"),
    (31, 148, "60 g unsalted butter (cold) plus extra for brushing"),
    (31, 591, "2 large free-range eggs"),
    (31, 864, "olive oil"),
    (31, 878, "icing sugar for dusting"),
    (31, 907, "ice cream, chocolate, cream, seasonal berries, your favourite nuts \u2013 get creative!")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (31, 9),
    (31, 11),
    (31, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (31, 43),
    (31, 174)

"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()









##########################################################################################################











# Beef tacos ID=90
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (90, 796, "1 onion"),
    (90, 809, "1 red pepper and 1 green pepper"),
    (90, 864, "olive oil"),
    (90, 522, "2 cloves of garlic"),
    (90, 890, "1 pinch of paprika"),
    (90, 773, "1\u00bd teaspoons cumin"),
    (90, 880, "500 g quality minced beef"),
    (90, 898, "250 ml organic beef stock"),
    (90, 934, "12 corn taco shells"),
    (90, 811, "2 ripe tomatoes"),
    (90, 870, "1 spring onion"),
    (90, 517, "3 sprigs of fresh coriander"),
    (90, 442, "1 lime"),
    (90, 367, "2 ripe avocados"),
    (90, 885, "2 tablespoons cr\u00e8me fra\u00eeche")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (90, 9),
    (90, 7),
    (90, 13),
    (90, 15),
    (90, 17),
    (90, 20)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (90, 91),
    (90, 300),
    (90, 336),
    (90, 339)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# Light & fluffy rice ID=91
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (91, 131, "350 g basmati rice")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (91, 8),
    (91, 11),
    (91, 12),
    (91, 13),
    (91, 14),
    (91, 15),
    (91, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (91, 126)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()



# Lemon rice ID=92
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (92, 131, "455 g basmati rice"),
    (92, 17, "5 tablespoons vegetable oil"),
    (92, 903, "2 tablespoons mustard seeds"),
    (92, 565, "2 teaspoons urad dhal (small dried split peas)"),
    (92, 534, "1 handful curry leaves"),
    (92, 441, "2 lemons rind and juice of"),
    (92, 517, "1 bunch fresh coriander chopped"),
    (92, 3, "sea salt"),
    (92, 780, "freshly ground black pepper")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (92, 2),
    (92, 8),
    (91, 11),
    (91, 12),
    (91, 13),
    (91, 14),
    (92, 24)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (92, 192)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# My Singapore-style fried rice ID=93
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (93, 131, "150 g brown or basmati rice"),
    (93, 818, "320 g crunchy veg such as asparagus, baby corn, broccoli, leek, Chinese, red or white cabbage, pak choi, carrot"),
    (93, 522, "1 clove of garlic"),
    (93, 774, "2 cm piece of ginger"),
    (93, 591, "1 large free-range egg"),
    (93, 864, "olive oil"),
    (93, 874, "1 rasher of smoked streaky bacon"),
    (93, 737, "4 fresh or frozen raw peeled prawns"),
    (93, 665, "1 tablespoon low-salt soy sauce"),
    (93, 936, "1 teaspoon mixed seeds"),
    (93, 937, "1 teaspoon chilli jam")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (93, 9),
    (93, 14),
    (93, 17),
    (93, 18),
    (93, 20)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (93, 43),
    (93, 44),
    (93, 174),
    (93, 116),
    (93, 222)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# Singapore-Style Chilli Tofu ID=94
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (94, 653, "40 g cashew nuts"),
    (94, 17, "neutral oil for frying"),
    (94, 721, "200 g firm tofu dried with kitchen paper and cut into bite-sized cubes"),
    (94, 796, "1 onion finely chopped"),
    (94, 774, "1 tablespoon grated ginger (approx. 3cm)"),
    (94, 522, "3 cloves of garlic crushed"),
    (94, 869, "2 red chillies finely chopped (use fewer chillies or deseed if you prefer a milder heat)"),
    (94, 811, "1 medium tomato diced"),
    (94, 887, "200 ml hot veg or chicken stock, or boiling water"),
    (94, 798, "\u00bd a medium head of broccoli or 150g tenderstem broccoli, cut into small florets"),
    (94, 591, "1 small egg lightly beaten"),
    (94, 16, "4 tablespoons tomato ketchup"),
    (94, 938, "2 tablespoons sweet chilli sauce"),
    (94, 665, "1 tablespoon light soy sauce"),
    (94, 129, "rice")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (94, 9),
    (94, 17),
    (94, 18),
    (94, 21)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (94, 180),
    (94, 130)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# Katsu-style tofu rice bowls ID=95
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (95, 721, "450 g firm tofu"),
    (95, 782, "\u00bd teaspoon ground turmeric"),
    (95, 10, "2 tablespoons white miso"),
    (95, 939, "rice vinegar"),
    (95, 940, "mirin"),
    (95, 147, "300 g short grain brown rice"),
    (95, 29, "60 g breadcrumbs"),
    (95, 650, "40 g sesame seeds"),
    (95, 864, "olive oil"),
    (95, 941, "\u00bd teaspoon curry powder"),
    (95, 392, "2 tablespoons mango chutney"),
    (95, 408, "\u00bd a pineapple"),
    (95, 869, "2 fresh red chillies"),
    (95, 870, "4 spring onions"),
    (95, 815, "400 g mixed crunchy veg such as carrots, sugar snaps, cucumber, cabbage"),
    (95, 517, "\u00bd a bunch of fresh coriander (15g)"),
    (95, 916, "hot chilli sauce to serve")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (95, 3),
    (95, 9),
    (95, 11),
    (95, 12),
    (95, 14),
    (95, 17),
    (95, 18),
    (95, 20)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (95, 77),
    (95, 79),
    (95, 86)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# Stephen Mangan's Sri Lankan fish curry ID=96
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (96, 420, "35 g goraka or 2 tablespoons tamarind paste"),
    (96, 522, "2 cloves of garlic"),
    (96, 774, "2 cm piece of ginger"),
    (96, 942, "3 pandan leaves"),
    (96, 771, "1 large pinch of ground cinnamon"),
    (96, 780, "\u00bd a teaspoon ground black pepper"),
    (96, 534, "30 fresh curry leaves"),
    (96, 316, "300 g yellowfin tuna from sustainable sources"),
    (96, 943, "2 banana leaves"),
    (96, 863, "dried red chilli flakes optional"),
    (96, 811, "2 ripe tomatoes"),
    (96, 786, "1 fresh green chilli"),
    (96, 374, "\u00bd a fresh coconut"),
    (96, 442, "2 limes"),
    (96, 796, "\u00bd an onion"),
    (96, 148, "1 small knob of unsalted butter"),
    (96, 782, "1 small pinch of ground turmeric"),
    (96, 131, "1 builder\u2019s mug basmati rice (150g)")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (96, 9),
    (96, 13),
    (96, 17),
    (96, 20)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (96, 292),
    (96, 71),
    (96, 84),
    (96, 300),
    (96, 339)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# Jodie Whittaker's massaman curry ID=97
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (97, 643, "1 handful of unsalted peanuts (30g)"),
    (97, 592, "500 g beef chuck"),
    (97, 77, "1 x 400 ml tin of reduced-fat coconut milk"),
    (97, 796, "1 white onion"),
    (97, 820, "1 white potato (250g)"),
    (97, 817, "1 sweet potato (250g)"),
    (97, 944, "3 tablespoon fish sauce plus extra to serve"),
    (97, 4, "3 teaspoons palm sugar"),
    (97, 935, "450 g jasmine rice"),
    (97, 17, "vegetable oil"),
    (97, 869, "6 sun-dried chillies and 1 fresh bird's-eye chilli"),
    (97, 861, "1 tablespoon coriander seeds"),
    (97, 772, "5 cloves"),
    (97, 882, "1 tablespoon fennel seeds"),
    (97, 788, "1 tablespoon white peppercorns"),
    (97, 928, "100 ml coconut cream"),
    (97, 442, "3 limes"),
    (97, 211, "4 sticks of lemongrass"),
    (97, 522, "21 cloves of garlic"),
    (97, 517, "5 pieces of coriander root or \u00bd a bunch of fresh coriander stalks (15g)"),
    (97, 797, "10 small shallots"),
    (97, 912, "\u00bd tablespoon shrimp paste"),
    (97, 945, "200 g Thai string beans (yard-long beans)"),
    (97, 946, "300 g bok choi"),
    (97, 815, "2 carrots"),
    (97, 813, "1 cucumber"),
    (97, 947, "200 g beansprouts"),
    (97, 513, "\u00bd a bunch of fresh Thai basil (15g)"),
    (97, 525, "\u00bd a bunch of fresh mint (15g)"),
    (97, 939, "2 tablespoons rice wine vinegar")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (97, 9),
    (97, 14),
    (97, 17),
    (97, 18),
    (97, 20)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (97, 74),
    (97, 339),
    (97, 10),
    (97, 128),
    (97, 260),
    (97, 272)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# Tofu fried rice ID=98
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (98, 870, "6 spring onions"),
    (98, 131, "1 x 250 g sachet of cooked brown basmati rice"),
    (98, 937, "2 heaped teaspoons chilli jam"),
    (98, 591, "2 large free-range eggs"),
    (98, 721, "150 g firm silken tofu")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (98, 0),
    (98, 9),
    (98, 11),
    (98, 13),
    (98, 14),
    (98, 15),
    (98, 17),
    (98, 18),
    (98, 20)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (98, 43),
    (98, 174)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()


# Mexican-inspired bowl ID=99
insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (99, 147, "320 g brown rice"),
    (99, 585, "1 corn on the cob"),
    (99, 830, "1 red onion"),
    (99, 522, "2 cloves of garlic"),
    (99, 786, "1 fresh jalape\u00f1o or green chilli"),
    (99, 809, "1 small red pepper and 1 small yellow pepper"),
    (99, 517, "1 bunch of fresh coriander (30g)"),
    (99, 864, "olive oil"),
    (99, 773, "1 teaspoon ground cumin"),
    (99, 868, "1 teaspoon ground coriander"),
    (99, 771, "1 stick of cinnamon"),
    (99, 811, "1 x 400 g tin of quality plum tomatoes"),
    (99, 367, "1 ripe avocado"),
    (99, 442, "2 limes"),
    (99, 865, "extra virgin olive oil"),
    (99, 948, "1 x 400 g tin of black beans"),
    (99, 890, "\u00bd teaspoon smoked paprika"),
    (99, 180, "natural yoghurt"),
    (99, 916, "hot chilli sauce"),
    (99, 40, "6 wholemeal tortillas")

"""
cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()

insert_into_tagInRecipe_query = """
INSERT INTO 
    tagInRecipe (recipe_id, tag_id)
VALUES
    (99, 7),
    (99, 9),
    (99, 11),
    (99, 15),
    (99, 17),
    (99, 20)
"""
cursor = cursor.execute(insert_into_tagInRecipe_query)
conn.commit()

insert_skillVideoInRecipe_query = """
INSERT INTO 
    skillVideoInRecipe (recipe_id, skill_video_id)
VALUES
    (99, 332),
    (99, 11),
    (99, 300),
    (99, 336),
    (99, 221)
"""
cursor.execute(insert_skillVideoInRecipe_query)
conn.commit()



cursor.close()