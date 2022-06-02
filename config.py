class Config(object):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_PATH= None
    ENV="production"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    ENV="development"
    # SESSION_COOKIE_PATH= "/var/www/flaga/dane"
    SESSION_COOKIE_PATH= None

class TestingConfig(Config):
    TESTING = True