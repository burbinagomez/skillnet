import os
from dotenv import load_dotenv
from db import db

load_dotenv()


class Config:

    @staticmethod
    def init_app(app):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
        db.init_app(app)
        with app.app_context():
            db.create_all()

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}