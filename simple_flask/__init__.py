import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from simple_flask.core.response import CustomResponse


static = os.path.join(os.getcwd(), 'static')


def load_env_variables(env_path):
    load_dotenv()


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=None):
    # Create the app
    app = Flask(__name__, static_folder=static)
    # TODO: Configure flask app

    env_path = os.path.join(os.getcwd(), '.env')
    load_env_variables(env_path)

    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_object('simple_flask.core.config.Config')

    app.json.sort_keys = False
    app.response_class = CustomResponse

    db.init_app(app)
    migrate.init_app(app, db)

    from simple_flask.commands.scripts import admin_command_bp
    app.register_blueprint(admin_command_bp)

    from simple_flask.core.swagger import swagger_bp
    app.register_blueprint(swagger_bp)

    from simple_flask.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
