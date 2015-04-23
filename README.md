# cs373-idb  [![travis-ci-badge](https://travis-ci.org/tbarn/cs373-idb.svg?branch=master)](https://travis-ci.org/tbarn/cs373-idb)

#####For the graders:    
Our models.py is actually app.py. According to Downing, we do not need a models.py. This causes models.html to be app.html.    
We updated the largest sized images, per graders' request, to speed up page loading.
We added a models page that allows the user to sort the pillar's attributes on various criteras

##Overview
A Flask app hosted on Rackspace with Python and Bootstrap that emulates IMDB to track three pillars.

Our pillars:
* Cuisines
* Recipes
* Ingredients

For more information refer to [Introduction](https://github.com/tbarn/cs373-idb/wiki/(1)-Introduction) Wiki page

##Dependencies
Needed libraries to run app: flask (need to install), psycogp2 (need to install), unittest, getpass, io

Needed libraries to run tests: flask (need to install) and unittest

##Important Files
Refer to [Application Structure](https://github.com/tbarn/cs373-idb/wiki/(5)-Application-Structure) Wiki Page

##Quick setup (assumes you have git, python3 and pip for python3)
--Clone github project
sudo git clone https://github.com/tbarn/cs373-idb.git

--Download necessary libraries
sudo pip3 install Flask
sudo apt-get install libpq-dev python-dev
sudo pip3 install psycopg2

--Setup the Database
http://www.postgresql.org/docs/9.3/static/tutorial-createdb.html

---- download db
sudo apt-get install postgresql-9.3

---- make user and create DB 
sudo -u postgres createuser owning_user
sudo -u postgres createdb -O owning_user mydb

---- insert tables
psql mydb < tableschema.sql 

---- insert data into tables
python3 insertionDict.py 

---- insert materialized views for searching
psql mydb < search.sql


--Run the flask app
python3 app.py

Go to local server 


