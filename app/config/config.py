from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2]) #este archivo config lo sube 2 NIVELES DE CARPETA(a la raiz)
load_dotenv(os.path.join(basedir, '.env')) #busca al .env del proyecto

class Config:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DB_URI')

# class TestingConfig(Config):
#     SQLALCHEMY_TRACK_MODIFICATIONS = True
#     TESTING= True
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DB_URI')

# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DB_URI')

config = {
    'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    # 'production': ProductionConfig,
    'default': DevelopmentConfig
}