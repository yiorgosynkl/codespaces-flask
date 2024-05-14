from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/gnkl")
def gnkl_ui():
    return render_template("gnkl.html")