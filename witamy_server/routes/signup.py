from flask_restx import Resource, reqparse
from flask_restx.utils import HTTPStatus
from ..parser import signup_input_parser
from .. import api
from .. import database
from ..models import Users

class SignUp(Resource):
    method_decorators = []

    @api.expect("signup_parser", signup_input_parser)
    def post(self):
        form_data = reqparse.request.form
        email = form_data.get("email")
        password = form_data.get("password")
        if email is None or password is None:
            return {
                "error": "something went wrong"
            }, HTTPStatus.BAD_REQUEST
        if Users.query.filter_by(email=email).first() is not None:
            return {
                "error": "email is not available"
            }, HTTPStatus.CONFLICT
        user = Users()
        user.email = email
        user.password = password
        try:
            database.session.add(user)
            database.session.commit()
        except Exception as exp:
            print(exp)
            return {
                "error": f"something went wrong | {exp}"
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        return {
            "message": "account created"
        }, HTTPStatus.CREATED