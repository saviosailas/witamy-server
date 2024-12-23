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
        email = form_data.get("email")
        password = form_data.get("password")
        if email is None or password is None:
            return {
                "error": "something went wrong"
            }, HTTPStatus.BAD_REQUEST
        user = Users.query.filter_by(email=email).first()
        if user is None:
            return {
                "error": "Invalid email"
            }, HTTPStatus.UNAUTHORIZED
        if user.password == password:
            return {
                "message": "login successful",
                "jwt_token": create_access_token(identity=email, additional_claims={"user_id" : user.id})
            }
        return {
            "error": "Invalid password"
        }, HTTPStatus.UNAUTHORIZED
