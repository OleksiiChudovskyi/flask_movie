import pathlib


class Config:
    DEBUG = False
    TESTING = False

    BASE_DIR = pathlib.Path(__file__).parent

    SECRET_KEY = 'you-will-never-know'

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(BASE_DIR / 'data' / 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    API_VERSION = "/api/v1"

    SWAGGER_BASE_URL = str(API_VERSION + "/swagger")
    SWAGGER_API_URL = "/static/actorfilmswagger.json"
    SWAGGER_APP_NAME = "Flask Movie"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
