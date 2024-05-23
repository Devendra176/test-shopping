import sqlite3

from flask import g, current_app


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE_URI'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def parse_sql_script():
    sql_schema = current_app.config['SCHEMA_FILE']
    db = get_db()
    with current_app.open_resource(sql_schema, mode='r') as f:
        db.executescript(f.read())
    db.commit()
    print(f"DB Created")
