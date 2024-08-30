import os


basedir = os.path.abspath(os.path.dirname(__file__))

class dingtalkConfig:
    URL = 'https://oapi.dingtalk.com/robot/send?access_token=0df528cc3a00b7cc6526c52e43ce170f69400b46e52734e5b0e8fa129edc3004'
    SECRET = "SECdffa9f94197c374133c138fe28abd86b2a3fb937d1d3750c0e4fd69ab718a0dd"  # SEC开头的

class dingtalkConfig_test:
    test_URL = 'https://oapi.dingtalk.com/robot/send?access_token=f83292eac2deeb253ad352c1b742eee27555830e2c7e7d59b8ae611e26e4efc8'
    test_SECRET = "SECe126a396317ee666eb82df81fef96a685dc69c860e3b9b36b6c1c981e94a4e0a"  # SEC开头的


class Config(dingtalkConfig):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'xxxx@qq.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DefaultConfig(Config):
    DEBUG = True




class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'mysql+mysqlconnector://root:123456@127.0.0.1/authbase?charset=utf8&auth_plugin=mysql_native_password'


class TestingConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DefaultConfig
}
