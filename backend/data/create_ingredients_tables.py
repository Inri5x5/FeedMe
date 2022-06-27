import json

def main():
    #ingredients schema: ingredient_id (int), ingredient_category_id (int), name (string)
    ingredients_table = []

    #ingredient categories schema: ingredient_category_id (int), name (string)
    ingredient_categories_table = []

    with open("Ingredient-Category.csv", "r") as source_file:
        for line in source_file:
            split_line = line.strip().split(",")
            new_ingredients_row = {"ingredient_id": int(split_line[0]), "ingredient_category_id": int(split_line[3]), "name": split_line[1]}

            new_categories_row = {"category_id": int(split_line[3]), "name": split_line[2]}

            ingredients_table.append(new_ingredients_row)

            if new_categories_row not in ingredient_categories_table:
                ingredient_categories_table.append(new_categories_row)


    source_file.close()

    fp1 = open("ingredients_table.json", "w")
    json.dump(ingredients_table, fp1)
    fp1.close()

    fp2 = open("ingredient_categories_table.json", "w")
    json.dump(ingredient_categories_table, fp2)
    fp2.close()

    return


if __name__ == "__main__":
    main()