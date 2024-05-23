from sqlalchemy import text

from simple_flask import db
from simple_flask.managers import ProductManager


def drop_all_tables_sqlite(connection):
    try:
        result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))
        tables = result.fetchall()
        for table_name, in tables:
            connection.execute(text(f"DROP TABLE IF EXISTS {table_name}"))
    except Exception as e:
        print(e)


def init_products():
    manager = ProductManager(db.session)
    dummy_data = manager.create_dummy_data()
    manager.save_all(dummy_data)
