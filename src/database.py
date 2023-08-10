import sqlite3

from flask import current_app, g

# Not ideal but a simple quick way to handle the database connections
# https://flask.palletsprojects.com/en/2.3.x/tutorial/database/
def get_database_connection() -> sqlite3.Connection:
    if 'database' not in g:
        g.database = create_database_connection()
    return g.database

def create_database_connection() -> sqlite3.Connection:
    database = sqlite3.connect(
        "database.sqlite",
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    database.row_factory = sqlite3.Row
    return database

# Close the database connection on application shutdown (teardown)
def close_database(_=None):
    # if database := g.pop('database', None) is not None:
    #     database.close()
    pass
