from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "StacksGoldPrint is live"

if __name__ == "__main__":
    import os
