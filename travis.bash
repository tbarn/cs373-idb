#!/bin/bash

check_file () {
    if [ -f "$1" ]
    then
        echo "$1 found"
    else
        echo "$1 not found"
        exit -1
    fi
}

echo "Checking for all files"

check_file "IDB.log"
check_file "README.md"
check_file "Report.pdf"
check_file "UML.pdf"
check_file "apiary.apib"
check_file "app.html"
check_file "app.py"
check_file "insertionDict.py"
check_file "requirements.txt"
check_file "search.sql"
check_file "tableschema.sql"
check_file "tests.out"
check_file "tests.py"

cd static 
check_file "jquery-latest.js"
check_file "jquery.tablesorter.js"
cd ..

postgres createuser owning_user 
postgres createdb -O owning_user mydb
psql mydb < tableschema.sql
python3 insertionDict.py

python3 tests.py

echo "Done."
