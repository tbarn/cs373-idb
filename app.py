#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, render_template

app = Flask(__name__)

index = {
	"leaning":"/static/pisa_tower.jpeg",
	"peppers":"/static/mexican_peppers.jpeg",
	"bagel":"/static/french_bagel.jpeg"
}

cuisines = [
    {
        "id": 1, 
        "name": "Japanese", 
        "description": "The Japanese diet consists principally of rice; fresh, lean seafood; and pickled or boiled vegetables.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/a/a5/Tempura%2C_sashimi%2C_pickles%2C_ris_og_misosuppe_%286289116752%29.jpg", 
        "youtube_URL": "https://www.youtube.com/watch?v=nxxx0-CgQ0o", 
        "map": "https://www.google.com/maps/place/Japan/@37.4900318,136.4664008,6z/data=!3m1!4b1!4m2!3m1!1s0x34674e0fd77f192f:0xf54275d47c665244", 
        "ingredients": [
        {"id": 1, "name": "sushi rice"}, 
        {"id": 2, "name": "avocado"}, 
        {"id": 3, "name": "crab meat"}, 
        {"id": 4, "name": "cucumber"}, 
        {"id": 5, "name": "nori"}, 
        {"id": 6, "name": "sesame seeds"}], 
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "facebook_page": "https://www.facebook.com/pages/Japanese-food/111895362163042?ref=br_rs"
    },
    {
        "id": 2, 
        "name": "French", 
        "description": "Meals range from the very basic, such as the traditional baguette plus cheese plus inexpensive wine, to very elaborate affairs than can involve a dozen courses and different wines consumed over several hours.", 
        "image_URL": "http://www.henit.ie/wp-content/uploads/2013/12/french_cuisine.jpeg", 
        "youtube_URL": "https://www.youtube.com/watch?v=B7EgCPAca_0", 
        "map": "https://www.google.com/maps/place/France/@46.71109,1.7191036,5z/data=!3m1!4b1!4m2!3m1!1s0xd54a02933785731:0x6bfd3f96c747d9f7", 
        "ingredients": [
        {"id": 7, "name": "thinly sliced onions"}, 
        {"id": 8, "name": "sugar"}, 
        {"id": 9, "name": "pepper"}, 
        {"id": 10, "name": "vegetable oil"}, 
        {"id": 11, "name": "beef broth"}, 
        {"id": 12, "name": "sliced French bread"}, 
        {"id": 13, "name": "shredded swiss cheese"}, ], 
        "recipes": [{"id": 2, "name": "French Onion Soup"}], 
        "facebook_page": ""
    }
]

recipes = [
    {
        "id": 1, 
        "name": "California Roll", 
        "description": "Originally from California, one of the most popular styles of sushi in the US.", 
        "image_URL": "http://japanfoodchannel.com/wp-content/uploads/2012/05/California_Rolls_Cropped.jpg", 
        "youtube_URL": "https://www.youtube.com/watch?v=nxX3XKE94W8", 
        "ingredients": [
        {"id": 1, "name": "sushi rice", "quantity": "1 batch"}, 
        {"id": 2, "name": "avocado", "quantity": "1"}, 
        {"id": 3, "name": "crab meat", "quantity": "1/4 kg"}, 
        {"id": 4, "name": "cucumber", "quantity": "1"}, 
        {"id": 5, "name": "nori", "quantity": "1 pack"}, 
        {"id": 6, "name": "sesame seeds", "quantity": ""}], 
        "instructions": [
        "Cook the batch of sushi rice", 
        "Place nori on bamboo mat", 
        "Split nori in half", 
        "On one sheet layer with small amount of rice", 
        "Layer rice with sesame seeds", 
        "Flip nori and rice over", 
        "Cut cucumber and avocado into strips", 
        "Then along bottom edge of nori, put few strips of cucumber down", 
        "Follow with a few strips of avocado", 
        "Finally add some crabmeat", 
        "Be sure to not add too much filling or roll won't seal",
        "Then roll, hold filling in place and use mat to lift rice over the filling", 
        "Once rice hits the filling, peel back and finish rolling the rice into a cylinder", 
        "Then slice rolls to be ready to serve", 
        "Serve with soy sauce and wasabi"], 
        "cuisine": {"id": 1, "name": "Japanese"}
    },
    {
        "id": 2, 
        "name": "French Onion Soup", 
        "description": "Type of soup usually based on meat stock and onions, served with bread and cheese", 
        "image_URL": "http://jewishinstlouis.org/wp-content/uploads/2013/08/French-Onion-Soup.jpg", 
        "youtube_URL": "https://www.youtube.com/watch?v=-DLDMQucqDI", 
        "ingredients": [
        {"id": 7, "name": "thinly sliced onions", "quantity": "4 cups"}, 
        {"id": 8, "name": "sugar", "quantity": "1/2 tablespoon"}, 
        {"id": 9, "name": "pepper", "quantity": "1/4 teaspoon"}, 
        {"id": 10, "name": "vegetable oil", "quantity": "1/4 cup"}, 
        {"id": 11, "name": "beef broth", "quantity": "4 cups"}, 
        {"id": 12, "name": "sliced French bread", "quantity": "4 slices"}, 
        {"id": 13, "name": "shredded swiss cheese", "quantity": "1/2 cup"}], 
        "instructions": [
        "In soup pot, cook onions, sugar, and pepper in oil until caramelized (~ 15-20 mins)", 
        "Stir often", 
        "Add broth, bring to boil", 
        "Reduce heat, cover and simmer for 20 mins", 
        "Ladle into oven-proof bowls", 
        "Top each with bread and cheese", 
        "Broil until cheese is bubbly"], 
        "cuisine": {"id": 2, "name": "French"}
    }

]

ingredients = [
    {
        "id": 1, 
        "name": "sushi rice", 
        "description": "Sushi-meshi is a preparation of white, short-grained, Japanese rice mixed with a dressing consisting of rice vinegar, sugar, salt, and occasionally kombu and sake.", 
        "image_URL": "http://cdn2.norecipes.com/wp-content/uploads/2012/06/sushi-rice-8.jpg?e77857", 
        "youtube_URL": "http://www.youtube.com/embed/tNcs3mf1uTU", 
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "cuisines": [{"id": 1, "name": "Japanese"}]
    },
    {
        "id": 2, 
        "name": "avocado", 
        "description": "like a herd of crawfish tickling your ears with their mandibles", 
        "image_URL": "http://www.shooter-szene.de/content/wp-content/uploads/2014/04/gabe-newell-steam-valve.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/tNcs3mf1uTU", 
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "cuisines": [{"id": 1, "name": "Japanese"}]
    },
    {
		"id": 3, 
		"name": "imitation crab meat", 
        "description": "Imitation crab meat is processed seafood made of finely pulverized white fish flesh (surimi), shaped and cured to resemble leg meat of snow crab or Japanese spider crab, widely used in America as a replacement for 100% crab meat in many dishes - popularly used in American sushi.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/c/c7/Kanikama.jpg", 
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "cuisines": [{"id": 1, "name": "Japanese"}]
	},
    {
		"id": 4, 
        "name": "cucumber", 
        "description": "Long cylindrical green-skinned fruit with edible seeds and soft white flesh. Smaller cucumbers (kirbys) are used for pickling.", 
          "image_URL": "http://upload.wikimedia.org/wikipedia/commons/e/ed/Cucumber_and_cross_section.jpg", 
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "cuisines": [{"id": 1, "name": "Japanese"}]
	}
]

# API Routes, may split these out later

@app.route('/api/v1.0/cuisines', methods=['GET'])
def get_cuisines():
    return jsonify({'status': 'success', 'data': {'cuisines': cuisines}})

@app.route('/api/v1.0/cuisines/<int:cuisine_id>', methods=['GET'])
def get_cuisine(cuisine_id):
    cuisine = [cuisine for cuisine in cuisines if cuisine['id'] == cuisine_id]
    if len(cuisine) == 0:
        abort(404)
    return jsonify({'status': 'success', 'data': {'cuisine': cuisine[0]}})

@app.route('/api/v1.0/recipes', methods=['GET'])
def get_recipes():
    return jsonify({'status': 'success', 'data': {'recipes': recipes}})

@app.route('/api/v1.0/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = [recipe for recipe in recipes if recipe['id'] == recipe_id]
    if len(recipe) == 0:
        abort(404)
    return jsonify({'status': 'success', 'data': {'recipe': recipe[0]}})

@app.route('/api/v1.0/ingredients', methods=['GET'])
def get_ingredients():
    return jsonify({'status': 'success', 'data': {'ingredients': ingredients}})

@app.route('/api/v1.0/ingredients/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    ingredient = [ingredient for ingredient in ingredients if ingredient['id'] == ingredient_id]
    if len(ingredient) == 0:
        abort(404)
    return jsonify({'status': 'success', 'data': {'ingredient': ingredient[0]}})

# Website routes

@app.route('/', methods=['GET'])
def get_index_template():
    return render_template("index.html",index=index)

@app.route('/team.html', methods=['GET'])
def get_team_template():
    return render_template("team.html")

@app.route('/ingredients.html', methods=['GET'])
def get_ingredients_template():
    return render_template("ingredients.html", ingredients=ingredients)

@app.route('/recipes.html', methods=['GET'])
def get_recipes_template():
    return render_template("recipes.html", recipes=recipes)

@app.route('/cuisines.html', methods=['GET'])
def get_cuisines_template():
    return render_template("cuisines.html", cuisines=cuisines)

@app.route('/ingredient/<int:ingredient_id>', methods=['GET'])
def get_ingredient_template(ingredient_id):
    # TODO: Out of index errors
    ingredient1 = ingredients[ingredient_id - 1]
    return render_template("ingredient.html",
       ingredient=ingredient1)

@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe_template(recipe_id):
    # TODO: Out of index errors
    recipe1 = recipes[recipe_id - 1]
    return render_template("recipe.html",
       recipe=recipe1)

@app.route('/cuisine/<int:cuisine_id>', methods=['GET'])
def get_cuisine_template(cuisine_id):
    # TODO: Out of index errors
    cuisine1 = cuisines[cuisine_id - 1]
    return render_template("cuisine.html",
       cuisine=cuisine1)

# Error responses

@app.errorhandler(404)
def error_404(error):
    return make_response(jsonify({'status': 'error', 'error_message': 'Not found', 'error_code': 404}), 404)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host = '0.0.0.0')
