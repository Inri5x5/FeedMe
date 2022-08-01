import requests
import json

fp = open('./source_data/recipes.json', 'r')
recipe_data = json.load(fp)
fp.close()

recipe_list = [
	#generate_recipe_data0 (3)
	#"https://www.jamieoliver.com/recipes/vegetables-recipes/superfood-salad/",
	#"https://www.jamieoliver.com/recipes/soup-recipes/cheats-pea-soup/",
	#"https://www.jamieoliver.com/recipes/pasta-recipes/one-pan-veggie-lasagne/",
	
	# generate_recipe_data1 (29)
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

	# generate_recipe_data2 (29)
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

	# generate_recipe_data3 (29)
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
	
	# generate_recipe_data1 (21)
	# "https://www.jamieoliver.com/recipes/beef-recipes/beef-tacos/"
	# "https://www.jamieoliver.com/recipes/rice-recipes/light-and-fluffy-rice/",
	# "https://www.jamieoliver.com/recipes/rice-recipes/lemon-rice/",
	# "https://www.jamieoliver.com/recipes/rice-recipes/my-singapore-style-fried-rice/",
	# "https://www.jamieoliver.com/recipes/rice-recipes/singapore-style-chilli-tofu/",
	# "https://www.jamieoliver.com/recipes/rice-recipes/katsu-style-tofu-rice-bowl/",
	# "https://www.jamieoliver.com/recipes/fish-recipes/stephen-mangan-s-fish-curry/",
	# "https://www.jamieoliver.com/recipes/beef-recipes/jodie-whittaker-s-massaman-curry/",
	# "https://www.jamieoliver.com/recipes/rice-recipes/tofu-fried-rice/",
	# "https://www.jamieoliver.com/recipes/rice-recipes/mexican-inspired-bowl/",
	# "https://www.jamieoliver.com/recipes/rice-recipes/sushi-rolls/",
	# "https://www.jamieoliver.com/recipes/vegetable-recipes/veggie-pad-thai/",
	# "https://www.jamieoliver.com/recipes/chicken-recipes/chicken-tofu-noodle-soup/",
	# "https://www.jamieoliver.com/recipes/stew-recipes/chinese-steak-tofu-stew/",
	# "https://www.jamieoliver.com/recipes/soup-recipes/korean-chicken-hotpot/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/simple-veggie-tofu-stir-fry/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/rojak/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/tofu-chickpea-curry-with-spring-greens/",
	# "https://www.jamieoliver.com/recipes/seafood-recipes/prawn-tofu-pad-thai/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/hot-sour-soup/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/miso-soup-with-tofu-cabbage/",

	# generate_recipe_data2 (21)
	# "https://www.jamieoliver.com/recipes/fruit-recipes/super-green-smoothie/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/almond-banana-passion-fruit-smoothie/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/grapefruit-carrot-apple-juice/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/strawberry-slushie/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/mango-lassi/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/oat-pear-cardamom-smoothie/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/super-smoothie-ice-lollies/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/kiwi-fruit-ginger-and-banana-smoothie/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/pomegranate-ginger-lime-flavoured-water/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/frozen-fruit-smoothies/",
	# "https://www.jamieoliver.com/recipes/drink-recipes/pink-pepper-negroni/",
	# "https://www.jamieoliver.com/recipes/drink-recipes/limoncello/",
	# "https://www.jamieoliver.com/recipes/rum-recipes/hot-rummy-lemonade/",
	# "https://www.jamieoliver.com/recipes/rum-recipes/dry-passion-fruit-daiquiri/",
	# "https://www.jamieoliver.com/recipes/drink-recipes/spiced-chai/",
	# "https://www.jamieoliver.com/recipes/rum-recipes/mulled-pear-ginger/",
	# "https://www.jamieoliver.com/recipes/rum-recipes/blood-orange-mimosa/",
	# "https://www.jamieoliver.com/recipes/rum-recipes/sangria-latina/",
	# "https://www.jamieoliver.com/recipes/vodka-recipes/bloody-mary/",
	# "https://www.jamieoliver.com/recipes/vodka-recipes/christmas-pudding-vodka/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/elderflower-lemonade-with-frozen-berries/",
	
	# generate_recipe_data3 (21)
	# "https://www.jamieoliver.com/recipes/pancake-recipes/gluten-free-one-cup-pancakes/",
	# "https://www.jamieoliver.com/recipes/oat-recipes/apple-pear-overnight-oats/",
	# "https://www.jamieoliver.com/recipes/breakfast-recipes/one-pan-breakfast/",
	# "https://www.jamieoliver.com/recipes/breakfast-recipes/eggy-bread-muffins/",
	# "https://www.jamieoliver.com/recipes/egg-recipes/roll-and-go-omelette-wrap/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/sticky-cinnamon-fig-yoghurt-breakfast-bowls/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/one-cup-blueberry-pancakes/",
	# "https://www.jamieoliver.com/recipes/bread-recipes/cardamom-clementine-morning-buns/",
	# "https://www.jamieoliver.com/recipes/fruit-recipes/roasted-stone-fruit/",
	# "https://www.jamieoliver.com/recipes/bread-recipes/classic-crumpets/",
	# "https://www.jamieoliver.com/recipes/eggs-recipes/hollandaise-sauce/",
	# "https://www.jamieoliver.com/recipes/eggs-recipes/simple-cheese-omelette/",
	# "https://www.jamieoliver.com/recipes/eggs-recipes/quick-mexican-breakfast/",
	# "https://www.jamieoliver.com/recipes/eggs-recipes/charred-avo-eggs/",
	# "https://www.jamieoliver.com/recipes/bread-recipes/mushroom-sourdough-bruschettas/",
	# "https://www.jamieoliver.com/recipes/eggs-recipes/omelette-aux-fines-herbes/",
	# "https://www.jamieoliver.com/recipes/fish-recipes/irish-potato-cakes-with-smoked-salmon/",
	# "https://www.jamieoliver.com/recipes/eggs-recipes/brilliant-breakfast-waffles/",
	# "https://www.jamieoliver.com/recipes/eggs-recipes/green-eggs-ham/",
	# "https://www.jamieoliver.com/recipes/eggs-recipes/kerryann-s-dippy-eggs-asparagus-soldiers/",
	# "https://www.jamieoliver.com/recipes/vegetables-recipes/giant-veg-r-sti/"
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