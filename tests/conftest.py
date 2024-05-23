import pytest
from flask_migrate import upgrade, downgrade
from sqlalchemy.exc import LegacyAPIWarning, SADeprecationWarning

from simple_flask import create_app, db
from simple_flask.core.config import TestConfig
from simple_flask.core.db_conf import parse_sql_script
from simple_flask.core.utils import drop_all_tables_sqlite

import warnings


@pytest.fixture(autouse=True)
def ignore_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="flask_sqlalchemy.engine")
    warnings.filterwarnings("ignore", category=UserWarning)
    warnings.filterwarnings("ignore", category=LegacyAPIWarning)
    warnings.filterwarnings("ignore", category=SADeprecationWarning)


@pytest.fixture(scope='package')
def client():
    app = create_app(TestConfig)
    with app.test_client() as testing_client:
        with app.app_context():
            import os
            if os.path.exists(app.config['DATABASE_URI']):
                os.remove(app.config['DATABASE_URI'])

            if app.config['USE_RAW_QUERY_DB_INIT']:
                parse_sql_script()
            else:
                upgrade()
            yield testing_client

            if app.config['USE_RAW_QUERY_DB_INIT']:
                with db.engine.connect() as connection:
                    drop_all_tables_sqlite(connection)
            else:
                downgrade(revision='base')
