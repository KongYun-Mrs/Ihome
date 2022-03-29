# coding:utf-8

from flask_restful import Resource, reqparse
from flask_restful import marshal
from flask import current_app
from Ihone.api_10.user import model

Response = {"username": ""}


class UserAPi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("username", nullable=False, type=str, help='请输入正确的用户名', location=["json", "value"],
                                 reuired=True)

        def get(self):
            request_json = self.parser.parse_args()
            current_app.logger.info(request_json.get("username"))
            print(request_json.get("username"))
            user_info = {"username": request_json.get("username")}
            return marshal(Response, user_info)
