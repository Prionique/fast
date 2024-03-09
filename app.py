from flask import Flask, render_template, url_for, redirect

app = Flask(__name__, template_folder='templates')
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/release/<name>")
def name(name):
    a = {"prio001": "Primon - Space Dimension", "prio002": "Ilija Frapp - Gay"}
    return render_template("index.html", name = name)
app.run()
