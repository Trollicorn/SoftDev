from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hello():
	return ""

@app.route("/occupations")
def ree():
	with open("data/occupations.csv") as csv_file:
		import csv
		reader = csv.DictReader(csv_file, delimiter=',') 
		return render_template("model_tmplt.html", occupations=reader)

if __name__ == '__main__':
	app.debug = True
app.run()
