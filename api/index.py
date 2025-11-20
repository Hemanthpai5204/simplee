from flask import Flask, jsonify, render_template
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response
import sys
import os

# Correct path handling for templates/static
current_dir = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(current_dir, "..", "templates")
static_path = os.path.join(current_dir, "..", "static")

app = Flask(__name__, template_folder=templates_path, static_folder=static_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/greet")
def greet():
    return jsonify({"message": "Hello, nice to meet you!"})

# Vercel expects "app" variable to be the WSGI entry point
# No handler() function required
