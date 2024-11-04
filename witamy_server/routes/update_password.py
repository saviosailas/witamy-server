from flask_restx import Resource, reqparse
from flask_restx.utils import HTTPStatus
from ..parser import password_update_input_parser
from .. import api
from .. import database
from ..models import User
from flask_jwt_extended import jwt_required

class UpdatePassword(Resource):
    method_decorators = [jwt_required()]

    @api.expect("update_password_parser", password_update_input_parser)
    def put(self):
        form_data = reqparse.request.form
        username = form_data.get("username")
        password = form_data.get("password")
        new_password = form_data.get("new_password")
        if username is None or password is None or new_password is None:
            return {
                "error": "something went wrong"
            }, HTTPStatus.BAD_REQUEST
        user = User.query.filter_by(username=username).first()
        if user is None:
            return {
                "error": "Invalid username"
            }, HTTPStatus.UNAUTHORIZED
        if user.password == password:
            user.password = new_password
            try:
                database.session.commit()
            except Exception as exp:
                print(exp)
                return {
                    "error": "something went wrong"
                }, HTTPStatus.INTERNAL_SERVER_ERROR

            return {
                "message": "updated password sucessful"
            }, HTTPStatus.CREATED
        
        return {
            "error": "Invalid password"
        }, HTTPStatus.UNAUTHORIZED