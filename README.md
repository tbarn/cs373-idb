# cs373-idb

For the graders: 
Our models.py is actually app.py. According to Downing, we do not need a models.py. This causes models.html to be app.html. 

Needed libraries to run app: flask

Needed libraries to run tests: requests and unittest

To run unit tests locally on the UTCS machines, run: python3 tests.py


Quick setup (WIP)
sudo pip3 install Flask

--setup
sudo apt-get install postgresql-9.3
http://www.postgresql.org/docs/9.3/static/tutorial-createdb.html

--Make user and create DB 
sudo -u postgres createuser owning_user
sudo -u postgres createdb -O owning_user dbname

--Insert table
psql mydb < tableschema.sql 

sudo apt-get install libpq-dev python-dev
sudo pip3 install psycopg2

--Insert info
python3 insertionDict.py 

python3 app.py

Go to local server 

