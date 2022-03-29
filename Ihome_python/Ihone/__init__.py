import redis

from flask import Flask
from settings import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from Ihone.util.app_logger import init_log

# 数据库实例
db = SQLAlchemy()

#  redis对象
redis_store = None


def create_app(config_name):
    app = Flask(__name__)

    config_class = config_map.get(config_name)

    # 加载配置类
    app.config.from_object(config_class)

    # 初始化db
    db.init_app(app)

    # 初始化redis工具
    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # 利用flask-session 将session数据保存到redis中
    Session(app)

    # 为应用开启csrf跨域baohu
    CSRFProtect(app)

    # 注册蓝图
    from Ihone.api_10.user import blp_api
    app.register_blueprint(blp_api, url_prefix='/api/v1.0')

    # 初始化日志
    init_log(app)
    return app
