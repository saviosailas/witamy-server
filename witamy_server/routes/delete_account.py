from flask_restx import Resource, reqparse
from flask_restx.utils import HTTPStatus
from ..parser import delete_account_input_parser
from .. import api
from .. import database
from ..models import Users
from flask_jwt_extended import jwt_required

class DeleteAccount(Resource):
    method_decorators = [jwt_required()]

    @api.expect("delete_account_parser", delete_account_input_parser)
    def delete(self):
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
            try:
                database.session.delete(user)
                database.session.commit()
            except Exception as exp:
                print(exp)
                return {
                    "error": "something went wrong"
                }, HTTPStatus.INTERNAL_SERVER_ERROR
            return {
                "message": "account deleted"
            }, HTTPStatus.CREATED
        return {
            "error": "Invalid password"
        }, HTTPStatus.UNAUTHORIZED