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
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # -- API Cuisine --

    def test_api_cuisine_1 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines/1')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['cuisine']['name'], 'Japanese')

    def test_api_cuisine_2 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines/10')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['cuisine']['name'], 'Persian')

    # Error case
    def test_api_cuisine_3 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines/400')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # Error case
    def test_api_cuisine_4 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines/0')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # Error case
    def test_api_cuisine_5 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines/11')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # -- API Recipes --

    def test_api_recipes_1 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/recipes')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['recipes'][0]['name'], 'California Roll')
        self.assertEqual(j['data']['recipes'][9]['name'], 'Persian Rice')

    def test_api_recipes_2 (self) :
# Should this really be an error?
        r = requests.get('http://104.239.168.220/api/v1.0/recipes/')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

# -- API Recipe --

    def test_api_recipe_1 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/recipes/1')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['recipe']['name'], 'California Roll')

    def test_api_recipe_2 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/recipes/10')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['recipe']['name'], 'Persian Rice')

    # Error case
    def test_api_recipe_3 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/recipes/400')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # Error case
    def test_api_recipe_4 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/recipes/0')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # Error case
    def test_api_recipe_5 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/recipes/11')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # -- API Ingredients --

    def test_api_ingredients_1 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['ingredients'][0]['name'], 'sushi rice')
        self.assertEqual(j['data']['ingredients'][52]['name'], 'saffron threads')

    def test_api_ingredients_2 (self) :
# Should this really be an error?
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients/')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # -- API Ingredient --

    def test_api_ingredient_1 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients/1')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['ingredient']['name'], 'sushi rice')

    def test_api_ingredient_2 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients/53')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')
        self.assertEqual(j['data']['ingredient']['name'], 'saffron threads')

    # Error case
    def test_api_ingredient_3 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients/400')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # Error case
    def test_api_ingredient_4 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients/0')
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'error')

    # Error case
    def test_api_ingredient_5 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/ingredients/54')
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
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Ingredients' in t)
        self.assertTrue('Recipes' in t)
        self.assertTrue('Cuisines' in t)

    def test_html_index_2 (self) :
        r = requests.get('http://104.239.168.220/')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Ingredients' in t)
        self.assertTrue('Recipes' in t)
        self.assertTrue('Cuisines' in t)

    # -- HTML Team --

    def test_html_team_1 (self) :
        r = requests.get('http://104.239.168.220/team.html')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Zach Abel' in t)
        self.assertTrue('Andy Chow' in t)

    # -- HTML Ingredients --

    def test_html_ingredients_1 (self) :
        r = requests.get('http://104.239.168.220/ingredients.html')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('sushi rice' in t)
        self.assertTrue('saffron threads' in t)

    # -- HTML Recipes --

    def test_html_recipes_1 (self) :
        r = requests.get('http://104.239.168.220/recipes.html')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('California Roll' in t)
        self.assertTrue('Persian Rice' in t)

    # -- HTML Cuisines --

    def test_html_cuisines_1 (self) :
        r = requests.get('http://104.239.168.220/cuisines.html')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Japanese' in t)
        self.assertTrue('Persian' in t)

    # -- HTML Ingredient --

    def test_html_ingredient_1 (self) :
        r = requests.get('http://104.239.168.220/ingredient/1')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Ingredient: sushi rice' in t)

    def test_html_ingredient_2 (self) :
        r = requests.get('http://104.239.168.220/ingredient/53')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Ingredient: saffron threads' in t)

    # Error case
    def test_html_ingredient_3 (self) :
        r = requests.get('http://104.239.168.220/ingredient/0')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Are you sure you typed that right' in t)

    # Error case
    def test_html_ingredient_4 (self) :
        r = requests.get('http://104.239.168.220/ingredient/54')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Are you sure you typed that right' in t)

    # Error case
    def test_html_ingredient_5 (self) :
        r = requests.get('http://104.239.168.220/ingredient/')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Are you sure you typed that right' in t)

    # Error case
    def test_html_ingredient_6 (self) :
        r = requests.get('http://104.239.168.220/ingredient/a')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Are you sure you typed that right' in t)

    # -- HTML Recipe --

    def test_html_recipe_1 (self) :
        r = requests.get('http://104.239.168.220/recipe/1')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Recipe: California Roll' in t)

    def test_html_recipe_2 (self) :
        r = requests.get('http://104.239.168.220/recipe/10')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Recipe: Persian Rice' in t)

    # Error case
    def test_html_recipe_3 (self) :
        r = requests.get('http://104.239.168.220/recipe/0')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Are you sure you typed that right' in t)

    # Error case
    def test_html_recipe_4 (self) :
        r = requests.get('http://104.239.168.220/recipe/11')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Are you sure you typed that right' in t)

    # Error case
    def test_html_recipe_5 (self) :
        r = requests.get('http://104.239.168.220/recipe/')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Are you sure you typed that right' in t)

    # Error case
    def test_html_recipe_6 (self) :
        r = requests.get('http://104.239.168.220/recipe/a')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Are you sure you typed that right' in t)

    # -- HTML Cuisine --

    def test_html_cuisine_1 (self) :
        r = requests.get('http://104.239.168.220/cuisine/1')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Cuisine Type: Japanese' in t)

    def test_html_cuisine_2 (self) :
        r = requests.get('http://104.239.168.220/cuisine/10')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Cuisine Type: Persian' in t)

    # Error case
    def test_html_cuisine_3 (self) :
        r = requests.get('http://104.239.168.220/cuisine/0')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Are you sure you typed that right' in t)

    # Error case
    def test_html_cuisine_4 (self) :
        r = requests.get('http://104.239.168.220/cuisine/11')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Are you sure you typed that right' in t)

    # Error case
    def test_html_cuisine_5 (self) :
        r = requests.get('http://104.239.168.220/cuisine/')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Are you sure you typed that right' in t)

    # Error case
    def test_html_cuisine_6 (self) :
        r = requests.get('http://104.239.168.220/cuisine/a')
        c = r.headers['content-type']
        t = r.text
        self.assertEqual(c, 'text/html; charset=utf-8')
        self.assertTrue('Are you sure you typed that right' in t)

    # -------------
    # Error Handler
    # -------------

# ----
# main
# ----

if __name__ == "__main__" :
    main(warnings='ignore')


