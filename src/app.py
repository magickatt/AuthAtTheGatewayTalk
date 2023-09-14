import logging

from flask import Flask
from flask.logging import default_handler

from database import close_database


def create_app():
    app = Flask(__name__)

    root = logging.getLogger()
    root.addHandler(default_handler)
    root.setLevel(logging.INFO)

    app.teardown_appcontext(close_database)

    return app
