from flask import Flask
from decorators import key_required

app = Flask(__name__)

@app.route("/")
@key_required
def hello_world():
    return "<p>Hello, World!</p>"

