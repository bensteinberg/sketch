from flask import Flask, render_template
from random import randrange


app = Flask(__name__)


@app.route("/")
def sketch_index():
    """ Index route for demo sketch """
    num = randrange(0, 10)
    return render_template("index.html", num=num)
