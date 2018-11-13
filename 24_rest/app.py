#Mohammed Uddin
#SoftDev1 pd6
#K24 -- A RESTful Journey Skyward
#2018-11-13
from flask import Flask, render_template
import urllib3
import json

app = Flask(__name__)

api_key = "SbfYjFfTeIJ3yt22QfKtIwTYZNMgyofC0jfrPfZf"
url = "https://api.nasa.gov/planetary/apod?api_key=SbfYjFfTeIJ3yt22QfKtIwTYZNMgyofC0jfrPfZf"

http = urllib3.PoolManager()
r = http.request('GET',url)


@app.route("/")
def show():
    return render_template("templates/demo.html")


if __name__== "__main__":
    app.debug = True
    app.run()
