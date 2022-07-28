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
	# "https://www.jamieoliver.com/recipes/pasta-recipes/beautiful-courgette-penne-carbonara/",
	# "https://www.jamieoliver.com/recipes/parsnip-recipes/roasted-parsnips/",
	# "https://www.jamieoliver.com/recipes/prawn-recipes/butterflied-prawn-skewers/",
	# "https://www.jamieoliver.com/recipes/pizza-recipes/buddys-quick-pizzettas/",
	# "https://www.jamieoliver.com/recipes/fish-recipes/fish-finger-tacos/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/strawberry-cream-sandwich-sponge/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/chai-spiced-carrot-cake/"
	# "https://www.jamieoliver.com/recipes/fruit-recipes/rhubarb-and-custard-tart/"
	# "https://www.jamieoliver.com/recipes/chocolate-recipes/lamingtons/",
	# "https://www.jamieoliver.com/recipes/chocolate-recipes/chocolate-orange-shortbread/",
	# "https://www.jamieoliver.com/recipes/dessert-recipes/st-clement-s-shortbread/",
	# "https://www.jamieoliver.com/recipes/chocolate-recipes/chocolate-chip-muffins/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/croustade-apple-tart/",
	# "https://www.jamieoliver.com/recipes/bread-recipes/english-muffins/",
	# "https://www.jamieoliver.com/recipes/uncategorised-recipes/the-best-coffee-walnut-cake/",
	# "https://www.jamieoliver.com/recipes/chocolate-recipes/salted-caramel-brownies/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/pear-ginger-pudding/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/passion-berry-choux-buns/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/vegan-toffee-apple-upside-down-cake/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/pineapple-coconut-cake/",
	# "https://www.jamieoliver.com/recipes/uncategorised-recipes/lemon-amp-pistachio-cannoli/",
	# "https://www.jamieoliver.com/recipes/yoghurt-recipes/vanilla-yoghurt-panna-cotta/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/banana-panettone-pudding/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/mango-yoghurt-layer-pots/",
	# "https://www.jamieoliver.com/recipes/easter-recipes/chocolate-avocado-mousse/",
	# "https://www.jamieoliver.com/recipes/egg-recipes/vanilla-custard/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/classic-apple-crumble/",
	# "https://www.jamieoliver.com/recipes/chocolate-recipes/simple-chocolate-tart/",
	# "https://www.jamieoliver.com/recipes/ice-cream-recipes/ice-cream-sandwiches/"

	# generate_recipe_data_2 (29)
	# "https://www.jamieoliver.com/recipes/pasta-recipes/buddys-bolognese/",
	# "https://www.jamieoliver.com/recipes/pasta-recipes/rotolo-of-spinach-squash-ricotta/",
	# "https://www.jamieoliver.com/recipes/pasta-recipes/quick-seafood-pasta/",
	# "https://www.jamieoliver.com/recipes/pasta-recipes/epic-veg-lasagne/",
	# "https://www.jamieoliver.com/recipes/potato-recipes/potato-gnocchi/",
	# "https://www.jamieoliver.com/recipes/rice-recipes/ultimate-mushroom-risotto/",
	# "https://www.jamieoliver.com/recipes/pasta-recipes/sausage-pasta-bake/",
	# "https://www.jamieoliver.com/recipes/chicken-recipes/chicken-paella/",
	# "https://www.jamieoliver.com/recipes/pasta-recipes/spaghetti-aglio-olio-spring-greens/",
	# "https://www.jamieoliver.com/recipes/pasta-recipes/gennaro-s-classic-spaghetti-carbonara/", 
	# "https://www.jamieoliver.com/recipes/pasta-recipes/vegan-mac-n-cheese/",
	# "https://www.jamieoliver.com/recipes/pasta-recipes/meatballs-and-pasta/",
	# "https://www.jamieoliver.com/recipes/pasta-recipes/pasta-with-aubergine-tomato-sauce/",
	# "https://www.jamieoliver.com/recipes/chicken-recipes/chicken-sausage-prawn-jambalaya/",
	# Stew
	# "https://www.jamieoliver.com/recipes/chicken-recipes/spring-chicken-stew/",
	# "https://www.jamieoliver.com/recipes/beef-recipes/beef-brisket-with-red-wine-shallots/",
	# "https://www.jamieoliver.com/recipes/fish-recipes/easy-curried-fish-stew/",
	# "https://www.jamieoliver.com/recipes/game-recipes/sweet-sour-rabbit/",
	# "https://www.jamieoliver.com/recipes/mushroom-recipes/mushroom-bourguignon/",
	# "https://www.jamieoliver.com/recipes/pork-recipes/anna-friel-s-balinese-pork-stew/",
	# "https://www.jamieoliver.com/recipes/lamb-recipes/moroccan-lamb-stew/",
	# "https://www.jamieoliver.com/recipes/beef-recipes/beef-stroganoff/",
	# "https://www.jamieoliver.com/recipes/beef-recipes/oxtail-stew/",
	# "https://www.jamieoliver.com/recipes/vegetable-recipes/mexican-style-roasted-veg-ragu/",
	# "https://www.jamieoliver.com/recipes/seafood-recipes/sweetcorn-and-mussel-chowder/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/incredible-sicilian-aubergine-stew-caponata/",
	# "https://www.jamieoliver.com/recipes/chicken-recipes/jools-simple-chicken-and-veg-stew/",
	# "https://www.jamieoliver.com/recipes/lamb-recipes/lamb-tagine/",
	# "https://www.jamieoliver.com/recipes/pork-recipes/jools-sausage-smoky-bean-casserole/",

	# generate_recipe_data_3 (29)
	# "https://www.jamieoliver.com/recipes/lamb-recipes/slow-roasted-lamb/",
	# "https://www.jamieoliver.com/recipes/roast-chicken-recipes/farmhouse-roast-chicken/",
	# "https://www.jamieoliver.com/recipes/pork-recipes/perfect-pork-belly/",
	# "https://www.jamieoliver.com/recipes/beef-recipes/roast-topside-of-beef/",
	# "https://www.jamieoliver.com/recipes/salmon-recipes/roasted-salmon-artichokes/",
	# "https://www.jamieoliver.com/recipes/chicken-recipes/sweet-chicken-surprise/",
	# "https://www.jamieoliver.com/recipes/lamb-recipes/balsamic-lamb-shoulder/",
	# "https://www.jamieoliver.com/recipes/fish-recipes/roasted-salmon-summer-veg-traybake/",
	# "https://www.jamieoliver.com/recipes/fish-recipes/spiced-sea-bass-with-caramelised-fennel/",
	# "https://www.jamieoliver.com/recipes/game-recipes/sweet-amp-sticky-roast-quail/",
	# "https://www.jamieoliver.com/recipes/lamb-recipes/leg-of-lamb-with-amazing-gravy/",
	# "https://www.jamieoliver.com/recipes/pork-recipes/porchetta-di-davida/",
	# "https://www.jamieoliver.com/recipes/fish-recipes/green-tea-roasted-salmon/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/roast-mejadra-onions/",
	# "https://www.jamieoliver.com/recipes/goose-recipes/spiced-roast-goose/",

	# "https://www.jamieoliver.com/recipes/carrot-recipes/clementine-roasted-carrots/",
	# "https://www.jamieoliver.com/recipes/pickle-recipes/easy-homemade-pickle/",
	# "https://www.jamieoliver.com/recipes/vegetable-recipes/chorizo-pear-red-cabbage/",
	# "https://www.jamieoliver.com/recipes/vegetable-recipes/beautiful-courgettes/",
	# "https://www.jamieoliver.com/recipes/vegetable-recipes/roasted-root-veg/",
	# "https://www.jamieoliver.com/recipes/spinach-recipes/creamed-spinach/",
	# "https://www.jamieoliver.com/recipes/cauliflower-recipes/pot-roast-cauliflower/",
	# "https://www.jamieoliver.com/recipes/potato-recipes/balsamic-potatoes/",
	# "https://www.jamieoliver.com/recipes/vegetable-recipes/peas-beans-chilli-mint/",
	# "https://www.jamieoliver.com/recipes/spinach-recipes/wilted-spinach-with-yoghurt-raisins/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/asparagus-with-mushroom-mayonnaise/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/jersey-royals-wild-garlic/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/delicious-winter-salad/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/raw-spring-salad/"
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
			'video': None,
			'ingredients': ingredients,
			'steps': steps,
			'servings': servings,
			'time': time
		}
	)

fp = open('./source_data/recipes.json', 'w')
json.dump(recipe_data, fp, indent=2)
fp.close()

#print(response.text)