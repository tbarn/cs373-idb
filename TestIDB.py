#!/usr/bin/python2.7

# -------------------------------
# TestIDB.py
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase
import re
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
        #r = get_cuisines()
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')

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

    def test_api_cuisine_2 (self) :
        r = requests.get('http://104.239.168.220/api/v1.0/cuisines/10')
        #r = get_cuisine(10)
        c = r.headers['content-type']
        self.assertEqual(c, 'application/json')
        j = r.json()
        self.assertEqual(j['status'], 'success')

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

    # -- API Recipes --

    # -- API Recipe --

    # -- API Ingredients --

    # -- API Ingredient --

    # --------------
    # Website Routes
    # --------------

    # -- Web Index --

    # -- Web Team --

    # -- Web Ingredients --

    # -- Web Recipes --

    # -- Web Cuisines --

    # -- Web Ingredient --

    # -- Web Recipe --

    # -- Web Cuisine --

    # -------------
    # Error Handler
    # -------------

# ----
# main
# ----

if __name__ == "__main__" :
    main()

