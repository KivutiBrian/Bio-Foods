import os

class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/orderManagementSystem'
    SECRET_KEY = 'some-secret-key'
    FLASK_ENV= os.environ.get("FLASK_ENV")

class ProductionConfig(Config):
    DEBUG = False