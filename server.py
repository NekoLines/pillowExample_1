from typing import Type
from flask.helpers import send_file
from flask.json import jsonify
from makeText import make_text
from flask import Flask
from flask.globals import request
import os

app = Flask(__name__)

@app.route("/api/v1/make", methods=["POST"])
def make():
    if request.method == "POST":
        if os.path.exists("meme.png"):
            os.remove("meme.png")
        args = []
        args.append(request.form.get('first'))
        args.append(request.form.get('second'))
        try:
            make_text(args, "meme.png")
        except TypeError:
            return jsonify(error="null value can't be used as parameters")
        return send_file("meme.png", mimetype="image/jpeg")

    return jsonify(error="invalid http method")

if __name__ == '__main__':
    app.run("127.0.0.1", 11451, threaded=True, debug=True)
