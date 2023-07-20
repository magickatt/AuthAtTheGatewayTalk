from flask import Flask, Response
from decorators import key_required

app = Flask(__name__)

@app.route("/")
@key_required
def hello_world():
    return Response({
        "greeting": ["hello", "world"]
    })
