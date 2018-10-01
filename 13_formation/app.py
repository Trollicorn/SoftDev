'''
Mohammed Uddin
SoftDev1 pd6
K 13 -- Echo Echo Echo
2018-09-27
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")                                
def home():
	return render_template("login.html")

@app.route("/auth")                      
def authenticate():
	print(request)
	print(request.headers)
	return render_template("authenticate.html", username = request.args['username'], method = request.method)


if __name__ == "__main__":
	app.debug = True
	app.run()