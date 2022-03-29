# coding:utf-8


from flask import Blueprint
from flask_restful import Api

# 创建蓝图对象

blp_api = Blueprint("api_1_0", __name__)

from Ihone.api_10.user import uesrs

_blp_api = Api(blp_api)
_blp_api.add_resource(uesrs.UserAPi, '/userinfo', endpoint='userapi')
