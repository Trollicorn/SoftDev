from flask import Flask 
app = Flask(__name__)

@app.route("/")
def homepage():
	return """<p><a href="/one">route 1</a></p>
	          <p><a href="/two">route 2</a></p>
	          <p><a href="/three">route 3</a></p>"""

@app.route("/one")
def route1():
	return """<p>welcome to someplace</p> <a href="/"> return </a>"""

@app.route("/two")
def route2():
	return """<p>The Spanish Inquisition</p> <a href="/"> return </a>"""

@app.route("/three")
def route3():
	return """<p>look behind you</p> <a href="/"> return </a>"""

if __name__ == '__main__':
	app.debug = True;

app.run()