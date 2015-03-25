#!/usr/bin/python3

# -------------------------------
# TestIDB.py
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase
import requests
from lxml import html

from app import *

# -----------
# TestIDB
# -----------

class TestIDB (TestCase) :

    # ----------
    # API Routes
    # ----------


    # -- API Cuisines --

    def test_api_cuisines_1 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines')
        #r = get_cuisines()
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        # Test Content
        self.assertEqual(j['data']['cuisines'][0]['name'], 'Japanese')
        self.assertEqual(j['data']['cuisines'][9]['name'], 'Persian')

    def test_api_cuisines_2 (self) :
# Should this really be an error?
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines/')
        #r = get_cuisines()
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # -- API Cuisine --

    def test_api_cuisine_1 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines/1')
        #r = get_cuisine(1)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['cuisine']['name'], 'Japanese')

    def test_api_cuisine_2 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines/10')
        #r = get_cuisine(10)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['cuisine']['name'], 'Persian')

    # Error case
    def test_api_cuisine_3 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines/400')
        #r = get_cuisine(400)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # Error case
    def test_api_cuisine_4 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines/0')
        #r = get_cuisine(0)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # Error case
    def test_api_cuisine_5 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines/11')
        #r = get_cuisine(11)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # -- API Recipes --

    def test_api_recipes_1 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/recipes')
        #r = get_recipes()
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['recipes'][0]['name'], 'California Roll')
        self.assertEqual(j['data']['recipes'][9]['name'], 'Persian Rice')

    def test_api_recipes_2 (self) :
# Should this really be an error?
        r = requests.get('http://104.239.168.220/api/v1.0/recipes/')
        #r = get_recipes()
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

# -- API Recipe --

    def test_api_recipe_1 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/recipes/1')
        #r = get_recipe(1)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['recipe']['name'], 'California Roll')

    def test_api_recipe_2 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/recipes/10')
        #r = get_recipe(10)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['recipe']['name'], 'Persian Rice')

    # Error case
    def test_api_recipe_3 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/recipes/400')
        #r = get_recipe(400)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # Error case
    def test_api_recipe_4 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/recipes/0')
        #r = get_recipe(0)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # Error case
    def test_api_recipe_5 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/recipes/11')
        #r = get_recipe(11)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # -- API Ingredients --

    def test_api_ingredients_1 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients')
        #r = get_ingredients()
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['ingredients'][0]['name'], 'sushi rice')
        self.assertEqual(j['data']['ingredients'][52]['name'], 'saffron threads')

    def test_api_ingredients_2 (self) :
# Should this really be an error?
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients/')
        #r = get_ingredients()
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # -- API Ingredient --

    def test_api_ingredient_1 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients/1')
        #r = get_ingredient(1)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['ingredient']['name'], 'sushi rice')

    def test_api_ingredient_2 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients/53')
        #r = get_ingredient(10)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['ingredient']['name'], 'saffron threads')

    # Error case
    def test_api_ingredient_3 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients/400')
        #r = get_ingredient(400)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # Error case
    def test_api_ingredient_4 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients/0')
        #r = get_ingredient(0)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # Error case
    def test_api_ingredient_5 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients/54')
        #r = get_ingredient(11)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # --------------
    # Website Routes
    # --------------

    # -- HTML Index --

    def test_html_index_1 (self) :
        r = requests.get('http://104.239.168.220')
        #r = get_index_template()
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    def test_html_index_2 (self) :
        r = requests.get('http://104.239.168.220/')
        #r = get_index_template()
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # -- HTML Team --

    def test_html_team_1 (self) :
        r = requests.get('http://104.239.168.220/team.html')
        #r = get_team_template()
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # -- HTML Ingredients --

    def test_html_ingredients_1 (self) :
        r = requests.get('http://104.239.168.220/ingredients.html')
        #r = get_ingredients_template()
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # -- HTML Recipes --

    def test_html_recipes_1 (self) :
        r = requests.get('http://104.239.168.220/recipes.html')
        #r = get_recipes_template()
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # -- HTML Cuisines --

    def test_html_cuisines_1 (self) :
        r = requests.get('http://104.239.168.220/cuisines.html')
        #r = get_cuisines_template()
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # -- HTML Ingredient --

    def test_html_ingredient_1 (self) :
        r = requests.get('http://104.239.168.220/ingredient/1')
        #r = get_ingredient_template(1)
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    def test_html_ingredient_2 (self) :
        r = requests.get('http://104.239.168.220/ingredient/53')
        #r = get_ingredient_template(53)
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

#NEED TO FIX
    # Error case
    def test_html_ingredient_3 (self) :
        r = requests.get('http://104.239.168.220/ingredient/0')
        #r = get_ingredient_template(0)
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

#NEED TO FIX
    # Error case
    def test_html_ingredient_4 (self) :
        r = requests.get('http://104.239.168.220/ingredient/54')
        #r = get_ingredient_template(54)
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # Error case
    def test_html_ingredient_5 (self) :
        r = requests.get('http://104.239.168.220/ingredient/')
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # Error case
    def test_html_ingredient_6 (self) :
        r = requests.get('http://104.239.168.220/ingredient/a')
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # -- HTML Recipe --

    def test_html_recipe_1 (self) :
        r = requests.get('http://104.239.168.220/recipe/1')
        #r = get_recipe_template(1)
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    def test_html_recipe_2 (self) :
        r = requests.get('http://104.239.168.220/recipe/10')
        #r = get_recipe_template(10)
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

#NEED TO FIX
    # Error case
    def test_html_recipe_3 (self) :
        r = requests.get('http://104.239.168.220/recipe/0')
        #r = get_recipe_template(0)
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

#NEED TO FIX
    # Error case
    def test_html_recipe_4 (self) :
        r = requests.get('http://104.239.168.220/recipe/11')
        #r = get_recipe_template(11)
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # Error case
    def test_html_recipe_5 (self) :
        r = requests.get('http://104.239.168.220/recipe/')
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # Error case
    def test_html_recipe_6 (self) :
        r = requests.get('http://104.239.168.220/recipe/a')
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # -- HTML Cuisine --

    def test_html_cuisine_1 (self) :
        r = requests.get('http://104.239.168.220/cuisine/1')
        #r = get_cuisine_template(1)
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    def test_html_cuisine_2 (self) :
        r = requests.get('http://104.239.168.220/cuisine/10')
        #r = get_cuisine_template(10)
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

#NEED TO FIX
    # Error case
    def test_html_cuisine_3 (self) :
        r = requests.get('http://104.239.168.220/cuisine/0')
        #r = get_cuisine_template(0)
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

#NEED TO FIX
    # Error case
    def test_html_cuisine_4 (self) :
        r = requests.get('http://104.239.168.220/cuisine/11')
        #r = get_cuisine_template(11)
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # Error case
    def test_html_cuisine_5 (self) :
        r = requests.get('http://104.239.168.220/cuisine/')
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # Error case
    def test_html_cuisine_6 (self) :
        r = requests.get('http://104.239.168.220/cuisine/a')
        c = r.headers['content-type']
        self.assertEqual(c, 'text/html; charset=utf-8')

    # -------------
    # Error Handler
    # -------------

# ----
# main
# ----

if __name__ == "__main__" :
    main(warnings='ignore')


