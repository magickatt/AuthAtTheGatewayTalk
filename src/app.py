from flask import Flask
from database import close_database

def create_app():
    app = Flask(__name__)
    app.teardown_appcontext(close_database)
    return app
