


import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER PRIMARY KEY);"        #build SQL stmt, save as string
c.execute(command)

with open('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #insert into tbl values(name,age,id);
        pop = "INSERT INTO peeps VALUES('{0}',{1},{2});".format(row['name'],row['age'],row['id'])
        c.execute(pop)

command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);"        #build SQL stmt, save as string (same as for peeps)
c.execute(command)

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #insert into tbl values(courses,mark,id);
        pop = "INSERT INTO courses VALUES('{0}',{1},{2});".format(row['code'],row['mark'],row['id'])
        c.execute(pop)

#==========================================================

db.commit() #save changes
db.close()  #close database