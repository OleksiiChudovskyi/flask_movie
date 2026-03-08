import pathlib

BASE_DIR = pathlib.Path(__file__).parent


class Config:
    SECRET_KEY = 'you-will-never-know'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(BASE_DIR / 'data' / 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
