from flask import Flask, request

from youtube import youtube_search
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello COSC381!"

@app.route("/youtube")
def handle_youtube():
    query_term = "flask"

    if "q" in request.args:
        query_term = request.args["q"]
    results = youtube_search(query_term, 1)
    return json.dumps(results)