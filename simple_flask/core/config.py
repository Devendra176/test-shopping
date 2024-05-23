import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SCHEMA_FILE = os.path.join(os.getcwd(), 'simple_flask/schema.sql')
    DATABASE_URI = os.path.join(os.getcwd(), 'instance/shopping.db')
    USE_RAW_QUERY_DB_INIT = False
    BASE_DIR = os.getcwd()
    SWAGGER_UI = os.path.join(BASE_DIR, 'swagger-ui')
    SWAGGER_CONFIG = os.path.join(BASE_DIR, 'swagger.yaml')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    DATABASE_URI = os.path.join(os.getcwd(), 'instance/test.db')
