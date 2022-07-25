import requests
import json

fp = open('./source_data/recipes.json', 'r')
recipe_data = json.load(fp)
fp.close()

recipe_list = [
	#generate_recipe_data_0
	#"https://www.jamieoliver.com/recipes/vegetables-recipes/superfood-salad/",
	#"https://www.jamieoliver.com/recipes/soup-recipes/cheats-pea-soup/",
	#"https://www.jamieoliver.com/recipes/pasta-recipes/one-pan-veggie-lasagne/",
	
	#generate_recipe_data_1 (29)
	#"https://www.jamieoliver.com/recipes/pasta-recipes/beautiful-courgette-penne-carbonara/"
	#"https://www.jamieoliver.com/recipes/parsnip-recipes/roasted-parsnips/",
	#"https://www.jamieoliver.com/recipes/prawn-recipes/butterflied-prawn-skewers/",
	#"https://www.jamieoliver.com/recipes/pizza-recipes/buddys-quick-pizzettas/",
	#"https://www.jamieoliver.com/recipes/fish-recipes/fish-finger-tacos/",
	#"https://www.jamieoliver.com/recipes/fruit-recipes/strawberry-cream-sandwich-sponge/",
	#"https://www.jamieoliver.com/recipes/vegetables-recipes/chai-spiced-carrot-cake/"
	#"https://www.jamieoliver.com/recipes/fruit-recipes/rhubarb-and-custard-tart/"
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#

	# generate_recipe_data_2 (29)

	# generate_recipe_data_3 (29)
]

headers = {
	"content-type": "text/plain",
	"X-RapidAPI-Key": "", # put your key here
	"X-RapidAPI-Host": "mycookbook-io1.p.rapidapi.com"
}

url = "https://mycookbook-io1.p.rapidapi.com/recipes/rapidapi"

for recipe in recipe_list:
	payload = recipe
	response = requests.request("POST", url, data=payload, headers=headers)
	full = response.json()
	name = full[0]['name']
	description = full[0]['description']
	image = full[0]['images'][0]
	ingredients = full[0]['ingredients']
	steps = full[0]['instructions'][0]['steps']
	servings = full[0]['yield']
	time = full[0]['total-time']
	recipe_data.append(
		{
			'name': name,
			'description': description,
			'image': image,
			'video': "",
			'ingredients': ingredients,
			'steps': steps,
			'servings': servings,
			'time': time
		}
	)

fp = open('./source_data/recipes.json', 'w')
json.dump(recipe_data, fp)
fp.close()

#print(response.text)