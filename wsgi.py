from flask import Flask
from sys import version

app = Flask(__name__)

@app.route("/test")
def index():
    return f"Hello uWSGI from python version: {version}\n"

application = app
