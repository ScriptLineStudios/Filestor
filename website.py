from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import shutil

app = Flask(__name__)

@app.route("/upload", methods=['POST','PUT'])
def print_filename():
    file = request.files['file']
    with open(file.filename, "wb") as f:
        f.write(file.read())
    return "", 200

if __name__ == "__main__":
    app.run(debug=True)

    