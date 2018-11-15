#Mohammed Uddin
#SoftDev1 pd6
#K25 -- Getting More REST
#2018-11-14

import json
from urllib import request,parse

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def show():
    url = "http://universities.hipolabs.com/search?name=harvard"
    book = request.urlopen(url)
    stuff = book.read()
    things = json.loads(stuff)
    thing = things[0]
    return render_template("demo.html",name=thing['name'],site=thing['web_pages'],country=thing['country'])


if __name__== "__main__":
    app.debug = True
    app.run()
