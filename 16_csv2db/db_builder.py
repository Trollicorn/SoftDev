#Team Orange --Kaitlin Wan and Mohammed Uddin
#SoftDev1 pd6
#K16 -- No Trouble 
#2018-10-04

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
        pop = ("insert into peeps values(" + "'" + row['name'] + "'" + ',' + row['age'] + ',' + row['id'] + ');')
        c.execute(pop)

command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);"        #build SQL stmt, save as string (same as for peeps)
c.execute(command)

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #insert into tbl values(courses,mark,id);
        pop = ("insert into courses values(" + "'" + row['code'] + "'" + ',' + row['mark'] + ',' + row['id'] + ');')
        c.execute(pop)

command = ('select * from peeps;')
c.execute(command) #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database