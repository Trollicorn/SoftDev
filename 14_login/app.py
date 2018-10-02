#Mohammed A Lee - Mohammed Uddin and Thomas Lee
#SoftDev1 pd6
#K14 -- Do I Know You?
#2018-10-01
from flask import Flask, render_template, request, session, url_for, redirect
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

user = 'abc'
pw = '123'

@app.route("/")
def login():
    if "username" in session:
        return render_template('welcome.html', username= session['username'])
    return render_template('login.html')

@app.route("/auth")
def logged():
    if request.args['username'] == user and request.args['password'] == pw:
        session['username'] = request.args['username']
        return render_template('welcome.html', username= request.args['username'])
    else:
        return render_template('error.html')

@app.route("/exit")
def leave():
    session.pop('username')
    return redirect(url_for("login"))


if __name__== "__main__":
    app.debug = True
    app.run()