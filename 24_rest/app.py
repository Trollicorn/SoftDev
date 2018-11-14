#Mohammed Uddin
#SoftDev1 pd6
#K24 -- A RESTful Journey Skyward
#2018-11-13
from flask import Flask, render_template
from urllib import request,parse
import json

app = Flask(__name__)

@app.route("/")
def show():
    url = "https://api.nasa.gov/planetary/apod?date=2017-10-29&api_key=SbfYjFfTeIJ3yt22QfKtIwTYZNMgyofC0jfrPfZf"
    book = request.urlopen(url) #open the book
    stuff = book.read()         #read the stuff in the book
    things = json.loads(stuff)   #turn the stuff into into things you can understand
    return render_template("demo.html",title=things['title'],pic=things['url'],explanation=things['explanation'])


if __name__== "__main__":
    app.debug = True
    app.run()
