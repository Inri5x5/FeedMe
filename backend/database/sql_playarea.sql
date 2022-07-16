-- Views and functions



-- /search/tag/tags
-- get tags and categories
create or replace view recipe_tags_categories as 
SELECT tc.id, tc.name, 
        FROM Tag_Categories tc
            JOIN Tags t on t.tag_category_id = tc.tag_category_id
;

-- /search/recipes
create or replace view recipe_ingredients as
SELECT r.recipe_id, GROUP_CONCAT(ir.ingredient_id)
        FROM    Recipes r
                JOIN Ingredient_in_Recipe ir on ir.recipe_id = r.recipe_id
        GROUP BY r.recipe_id
;

-- /dash/statistics
create or replace view recipe_ratings as
SELECT r.recipe_id, 
            SUM(CASE WHEN rr.rating = 1 THEN 1 ELSE 0 END) AS one_rating,
            SUM(CASE WHEN rr.rating = 2 THEN 1 ELSE 0 END) AS two_rating,
            SUM(CASE WHEN rr.rating = 3 THEN 1 ELSE 0 END) AS three_rating,
            SUM(CASE WHEN rr.rating = 4 THEN 1 ELSE 0 END) AS four_rating,
            SUM(CASE WHEN rr.rating = 5 THEN 1 ELSE 0 END) AS five_rating,
        FROM recipes r
            JOIN public_recipes pr ON pr.recipe_id = r.recipe_id
            JOIN recipe_ratings rr ON rr.recipe_id = r.recipe_id
        WHERE pr.author_id = %s
        GROUP BY r.recipe_id
;