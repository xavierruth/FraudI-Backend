from flask import Flask
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, mundo Flask!"

if __name__ == "__main__":
    app.run(debug=True)
