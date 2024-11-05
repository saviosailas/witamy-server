from flask_restx import Resource, reqparse
from flask_restx.utils import HTTPStatus
from ..parser import login_input_parser
from .. import api
from ..models import Users
from flask_jwt_extended import create_access_token

class Login(Resource):
    method_decorators = []

    @api.expect("login_parser", login_input_parser)
    def post(self):
        form_data = reqparse.request.form
        username = form_data.get("username")
        password = form_data.get("password")
        if username is None or password is None:
            return {
                "error": "something went wrong"
            }, HTTPStatus.BAD_REQUEST
        user = Users.query.filter_by(username=username).first()
        if user is None:
            return {
                "error": "Invalid username"
            }, HTTPStatus.UNAUTHORIZED
        if user.password == password:
            return {
                "message": "login sucessful",
                "jwt_token": create_access_token(identity=username, additional_claims={"user_id" : user.id})
            }
        return {
            "error": "Invalid password"
        }, HTTPStatus.UNAUTHORIZED