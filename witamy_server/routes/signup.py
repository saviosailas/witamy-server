from flask_restx import Resource, reqparse
from flask_restx.utils import HTTPStatus
from ..parser import signup_input_parser
from .. import api
from .. import database
from ..models import User

class SignUp(Resource):
    method_decorators = []

    @api.expect("signup_parser", signup_input_parser)
    def post(self):
        form_data = reqparse.request.form
        username = form_data.get("username")
        password = form_data.get("password")
        if username is None or password is None:
            return {
                "error": "something went wrong"
            }, HTTPStatus.BAD_REQUEST
        if User.query.filter_by(username=username).first() is not None:
            return {
                "error": "username is not available"
            }, HTTPStatus.CONFLICT
        user = User()
        user.username = username
        user.password = password
        try:
            database.session.add(user)
            database.session.commit()
        except Exception as exp:
            print(exp)
            return {
                "error": "something went wrong"
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        return {
            "message": "account created"
        }, HTTPStatus.CREATED