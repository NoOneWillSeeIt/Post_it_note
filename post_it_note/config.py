import os

class Config:
    SECRET_KEY = 'totally secret string' or os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def init_app(app):
        pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///static/site.db'
    DEBUG = True