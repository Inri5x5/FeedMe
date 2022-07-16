import sqlite3
import json

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

# add a single recipe for backend testing
insert_into_recipes_query = """
INSERT INTO 
    recipes (id,title,description,image,video,time_required,servings)
VALUES
    (0, "Superfood Salad", "Full of great veggies and high-fibre quinoa, this easy-to-make salad is nutritious, delicious and super-satisfying. Top with juicy pomegranate seeds for a great burst of flavour.", "https://img.jamieoliver.com/jamieoliver/recipe-database/oldImages/large/1460_1_1436891540.jpg", "", 40, 6);
"""

cursor = cursor.execute(insert_into_recipes_query)
conn.commit()

insert_into_steps_query = """
INSERT INTO 
    steps (recipe_id, step_number,description,image)
VALUES
    (0, 1, "Preheat the oven to 200°C/400°F/gas 6.", ""),
    (0, 2, "Scrub and chop the sweet potatoes into 2.5cm chunks. Place into a roasting tray with the chilli flakes, ground coriander and cinnamon, a drizzle of olive oil and a little sea salt and black pepper, then toss well.", ""),
    (0, 3, "Spread out into an even layer and place in the hot oven for 15 to 20 minutes, or until golden and crisp.", ""),
    (0, 4, "Meanwhile, cook the quinoa in boiling salted water according to the packet instructions.", ""),
    (0, 5, "Once cooked, drain and rinse the quinoa under cold running water, then leave to cool along with the broccoli. Remove the sweet potato from the oven and leave it to cool, too.", ""),
    (0, 6, "Slice the broccoli into small florets, then halve and finely slice the stalk. Place into a heatproof colander and rest it over the quinoa pan. Cover and steam for 3 minutes, or until just tender.", ""),
    (0, 7, "Meanwhile, toast the nuts in a dry frying pan over a medium-high heat for 2 to 3 minutes, then transfer to a pestle and mortar and crush lightly.", ""),
    (0, 8, "Halve the pomegranate and squeeze half the juice into a large bowl. Add 3 times as much extra virgin olive oil, the lime juice and balsamic vinegar. Whisk well and season to taste.", ""),
    (0, 9, "Add the cooled broccoli and sprouts to the dressing, then snip in the cress. Roughly chop the coriander (stalks and all), finely slice the chilli and add to the bowl along with the quinoa and sweet potato.", ""),
    (0, 10, "Toss well, spread out on a serving platter, then scoop out and dot over the avocado flesh.", ""),
    (0, 11, "Bash the reserved pomegranate half with a wooden spoon so the seeds come tumbling out and scatter these over the platter along with the nuts, snip the cress on top, then serve with the feta crumbled over the top.", "");
"""

cursor = cursor.execute(insert_into_steps_query)
conn.commit()

insert_into_ingredientInRecipe_query = """
INSERT INTO 
    ingredientInRecipe (recipe_id, ingredient_id, description)
VALUES
    (0, 140, "200 g quinoa"),
    (0, 442, "2 limes")
"""

cursor = cursor.execute(insert_into_ingredientInRecipe_query)
conn.commit()
