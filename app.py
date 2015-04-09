#!flask/bin/python

from flask import Flask, jsonify, abort, make_response, render_template, request

# For running unittests
from io import StringIO
from tests import app, TestIDB
from unittest import TextTestRunner, makeSuite

# For database
import psycopg2
import psycopg2.extras

import getpass
username = getpass.getuser()
#print username
conn = psycopg2.connect("dbname='mydb' user=" + username)

#conn = psycopg2.connect("dbname='mydb' user='zach'")


index = {
	"leaning":"/static/pisa_tower.jpeg",
	"peppers":"/static/mexican_peppers.jpeg",
	"bagel":"/static/french_bagel.jpeg"
}


# API Routes, may split these out later

def find_cuisine_relationships(cuisine_id):
    """
    Helper function to join a cuisine with its relationships with recipes and ingredients 

    input: cuisine_id

    output: returns an cuisine dict with its relationships included
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select * from cuisines where cuisine_id = " +  str(cuisine_id)  + ";")
    result = cur.fetchone()

    cur.execute("select i.ingredient_id, i.name from cuisines inner join c_and_i using (cuisine_id) inner join ingredients i using (ingredient_id) where cuisine_id = " + str(cuisine_id) + ";")
    ingredients = cur.fetchall()
    result['ingredients'] = ingredients

    cur.execute("select r.recipe_id, r.name from cuisines inner join recipes r using (cuisine_id) where cuisine_id = " + str(cuisine_id) + ";")
    recipes = cur.fetchall()
    result['recipes'] = recipes

    return result

@app.route('/api/v1.0/cuisines', methods=['GET'])
def get_cuisines():
    """
    API GET request for all cuisines

    output: returns a response formatted in JSON with all the cuisines and their attributes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select * from cuisines;")
    cuisines = cur.fetchall()
    results = []

    for r in cuisines:
        results.append(find_cuisine_relationships(r['cuisine_id']))

    return jsonify({'status': 'success', 'data': {'type': 'cuisines', 'cuisines': results}})

@app.route('/api/v1.0/cuisines/<int:cuisine_id>', methods=['GET'])
def get_cuisine(cuisine_id):
    """
    API GET request for a specific cuisine

    input: cuisine_id 
    
    output: returns a response formatted in JSON for the cuisine requested by id with its attributes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select count(*) from cuisines where cuisine_id = " + str(cuisine_id) + ";")
    isValid = cur.fetchone() 
    if isValid['count'] == 0:
        abort(404)

    result = find_cuisine_relationships(cuisine_id)

    return jsonify({'status': 'success', 'data': {'type': 'cuisine', 'cuisine': result}})

def find_recipe_relationships(recipe_id):
    """
    Helper function to join a recipe with its relationships with ingredients and cuisines 

    input: recipe_id

    output: returns an recipe dict with its relationships included
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select * from recipes where recipe_id = " +  str(recipe_id)  + ";")
    result = cur.fetchone()


    cur.execute("select i.ingredient_id, i.name, ri.quantity from r_and_i ri inner join ingredients i using(ingredient_id) where recipe_id = " + str(recipe_id) + ";")
    ingredients = cur.fetchall()
    result['ingredients'] = ingredients

    cur.execute("select c.cuisine_id, c.name from recipes r inner join cuisines c using(cuisine_id) where recipe_id = " + str(recipe_id) + ";")
    cuisine = cur.fetchall()
    result['cuisine'] = cuisine

    result['instructions'] = eval(result['instructions'])
    return result

@app.route('/api/v1.0/recipes', methods=['GET'])
def get_recipes():
    """
    API GET request for all recipes

    output: returns a response formatted in JSON with all the recipes and their attributes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select * from recipes;")
    recipes = cur.fetchall()
    results = []

    for r in recipes:
        results.append(find_recipe_relationships(r['recipe_id']))

    return jsonify({'status': 'success', 'data': {'type': 'recipes', 'recipes': results}})

@app.route('/api/v1.0/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    """
    API GET request for a specific recipe

    input: recipe_id 

    output: returns a response formatted in JSON for the recipe requested by id with its attributes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select count(*) from recipes where recipe_id = " + str(recipe_id) + ";")
    isValid = cur.fetchone() 
    if isValid['count'] == 0:
        abort(404)

    result = find_recipe_relationships(recipe_id)

    return jsonify({'status': 'success', 'data': {'type': 'recipe', 'recipe': result}})

def find_ingredients_relationships(ingredient_id):
    """
    Helper function to join an ingredient with its relationships with recipes and cuisines 

    input: ingredient_id

    output: returns an ingredient dict with its relationships included
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select * from ingredients where ingredient_id = " +  str(ingredient_id)  + ";")
    result = cur.fetchone()

    cur.execute("select r.recipe_id, r.name from ingredients inner join r_and_i using (ingredient_id) inner join recipes r using (recipe_id) where ingredient_id = " + str(ingredient_id) + ";")
    recipes = cur.fetchall()
    result['recipes'] = recipes

    cur.execute("select c.cuisine_id, c.name from ingredients inner join c_and_i using (ingredient_id) inner join cuisines c using (cuisine_id) where ingredient_id = " + str(ingredient_id) + ";")
    cuisine = cur.fetchall()
    result['cuisines'] = cuisine

    return result    

@app.route('/api/v1.0/ingredients', methods=['GET'])
def get_ingredients():
    """
    API GET request for all ingredients

    output: returns a response formatted in JSON with all the ingredients and their attributes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select * from ingredients;")
    ingredients = cur.fetchall()
    results = []

    for r in ingredients:
        results.append(find_ingredients_relationships(r['ingredient_id']))
        
    return jsonify({'status': 'success', 'data': {'type': 'ingredients', 'ingredients': results}})

@app.route('/api/v1.0/ingredients/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    """
    API GET request for a specific ingredient

    input: ingredient_id
    
    output: returns a response formatted in JSON for the ingredient requested by id with its attributes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select count(*) from ingredients where ingredient_id = " + str(ingredient_id) + ";")
    isValid = cur.fetchone() 
    if isValid['count'] == 0:
        abort(404)

    result = find_ingredients_relationships(ingredient_id)

    return jsonify({'status': 'success', 'data': {'ingredient': result}})

# Website routes

@app.route('/', methods=['GET'])
def get_index_template():
    """
    output: returns index page
    """
    return render_template("index.html",index=index)

@app.route('/team.html', methods=['GET'])
def get_team_template():
    """
    output: renders team page
    """
    return render_template("team.html")

@app.route('/ingredients.html', methods=['GET'])
def get_ingredients_template():
    """
    output: returns a flask template filled in with the ingredients
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select * from ingredients;")
    results = cur.fetchall()
    ingredients = []

    for r in results:
        ingredients.append(find_ingredients_relationships(r['ingredient_id']))
        
    return render_template("ingredients.html", ingredients=ingredients)

@app.route('/recipes.html', methods=['GET'])
def get_recipes_template():
    """
    output: returns a flask template filled in with the recipes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select * from recipes;")
    results = cur.fetchall()
    recipes = []

    for r in results:
        recipes.append(find_recipe_relationships(r['recipe_id']))

    return render_template("recipes.html", recipes=recipes)

@app.route('/cuisines.html', methods=['GET'])
def get_cuisines_template():
    """
    output: returns a flask template filled in with the cuisines
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select * from cuisines;")
    results = cur.fetchall()
    cuisines = []

    for r in results:
        cuisines.append(find_cuisine_relationships(r['cuisine_id']))

    return render_template("cuisines.html", cuisines=cuisines)

@app.route('/ingredient/<int:ingredient_id>', methods=['GET'])
def get_ingredient_template(ingredient_id):
    """
    input: ingredient id number
    
    output: returns a flask template with the data from the ingredient that
     corresponds to the ingredient id
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select count(*) from ingredients where ingredient_id = " + str(ingredient_id) + ";")
    isValid = cur.fetchone() 
    if isValid['count'] == 0:
        abort(404)

    ingredient1 = find_ingredients_relationships(ingredient_id)

    return render_template("ingredient.html",
       ingredient=ingredient1)

@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe_template(recipe_id):
    """
    input: recipe id number
    
    output: returns a flask template filled in with the data from the recipe that
     corresponds to the recipe id
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select count(*) from recipes where recipe_id = " + str(recipe_id) + ";")
    isValid = cur.fetchone() 
    if isValid['count'] == 0:
        abort(404)

    recipe1 = find_recipe_relationships(recipe_id)

    return render_template("recipe.html",
       recipe=recipe1)

@app.route('/cuisine/<int:cuisine_id>', methods=['GET'])
def get_cuisine_template(cuisine_id):
    """
    input: cuisine id number
    
    output: returns a flask template filled in with the data from the cuisine that
     corresponds to the cuisine id
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select count(*) from cuisines where cuisine_id = " + str(cuisine_id) + ";")
    isValid = cur.fetchone() 
    if isValid['count'] == 0:
        abort(404)

    cuisine1 = find_cuisine_relationships(cuisine_id)

    return render_template("cuisine.html",cuisine=cuisine1)

@app.route('/unittests', methods=['GET'])
def run_unittests():
    """
    output: returns the output of unittests
    """
    stream = StringIO()
    runner = TextTestRunner(stream=stream, verbosity=2)
    suite = makeSuite(TestIDB)
    result = runner.run(suite)
    output = stream.getvalue()
    split_output = output.split('\n')
    return render_template("unittest.html", text=split_output)
    #return stream.getvalue()


# Error responses

@app.errorhandler(404)
def error_404(error):
    """
    output: returns a JSON formatted response for 404 errors from an API route
     and a HTML 404 page when it the request is from a path not starting with '/api'
    """
    if request.path.startswith('/api'):
        return make_response(jsonify({'status': 'error', 'error_message': 'Not found', 'error_code': 404}), 404)
    return render_template("404.html",err=request.path)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host = '0.0.0.0')
