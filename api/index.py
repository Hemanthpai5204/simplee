from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder="../templates", static_folder="../static")
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/greet")
def greet():
    return jsonify({"message": "Hello, nice to meet you!"})

# For Vercel handler
def handler(event, context):
    return app(event, context)
