from flask import flask

SHIPPING_ANNOUNCEMENT = "arriving soon"

@app.route("/")
def home():
    return "Welcome"
