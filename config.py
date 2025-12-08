import os

class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "troque-essa-chave")

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
