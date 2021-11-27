from flask import Flask, request
from . import youtube
import json

def create_app():
    app = Flask(__name__)
    @app.route("/")
    def index():
        return "Hello COSC381!"

    @app.route("/youtube")
    def handle_youtube():
        query_term = "flask"

        if "q" in request.args:
            query_term = request.args["q"]
        results = youtube.youtube_search(query_term, 3)
        return json.dumps(results)


    return app