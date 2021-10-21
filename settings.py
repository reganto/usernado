import os

root = os.path.dirname(os.path.abspath(__file__))
add_path = lambda *args: os.path.join(root, *args)

class BaseSettings:
    pass


class DevelopmentSettings(BaseSettings):
    development = True
    debug = True
    template_path = add_path('templates')
    cookie_secret = os.urandom(16)


class TestingSettings(BaseSettings):
    testing = True


class ProductionSettings(BaseSettings):
    production = True


settings = {
    'development': DevelopmentSettings,
    'testing': TestingSettings,
    'production': ProductionSettings,
}
