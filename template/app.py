from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def hello():
    return ""

@app.route("/my_foist_template")
def ree():
    return render_template( "model_tmplt.html", foo = "foooo" )

if (__name__=="__main__"):
    app.debug = True
app.run()
