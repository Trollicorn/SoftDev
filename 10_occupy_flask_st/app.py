#Undecided -- Mohammed Uddin and Britni Canale
#SoftDev1 pd6
#K 06 Jinja Tuning
#2018-9-21

from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hello():
	return """<a href="/occupations"> occupations </a>"""

@app.route("/occupations")
def ree():
	with open("data/occupations.csv") as csv_file:
		import csv
		reader = csv.DictReader(csv_file, delimiter=',')  #creates list of ordered dictionaries
		jobList = list(reader)                            #turn reader into a list
		rList = jobList.copy();                           #copy of job list to select random job
		rList.pop()                                       #remove last element (total) from possible choices in random
		import random 
		randJob=random.choice(rList)                      #random job unweighted
		return render_template("model_tmplt.html", occupations=jobList, randJob = randJob)

if __name__ == '__main__':
	app.debug = True
app.run()
