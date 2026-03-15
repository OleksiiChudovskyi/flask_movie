import pathlib


class Config:
    DEBUG = False
    TESTING = False
    HOST = "127.0.0.1"
    PORT = 5000
    EXTERNAL_PORT = 5005

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
    HOST = "0.0.0.0"
    PORT = 5000


class ProductionConfig(Config):
    POSTGRES_DB = "fm"
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "qwerty"
    POSTGRES_HOST = "127.0.0.1"
    POSTGRES_PORT = 5432

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{POSTGRES_DB}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
