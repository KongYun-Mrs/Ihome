import redis


class Config(object):
    SECRET_KEY = "XHSOI*Y9dfs9cshd9"

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-session
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USER_SIGNER = True  # 对cookie中的session_id 隐藏
    PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期


class Development(Config):
    DEBUG = True


class Product(Config):
    DEBUG = False


config_map = {"develop": Development, "pro": Product}
