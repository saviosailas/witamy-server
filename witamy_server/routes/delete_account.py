from flask_restx import Resource, reqparse
from flask_restx.utils import HTTPStatus
from ..parser import delete_account_input_parser
from .. import api
from .. import database
from ..models import Users, Profiles
from flask_jwt_extended import jwt_required, get_jwt_identity

class DeleteAccount(Resource):
    method_decorators = [jwt_required()]

    @api.doc(security='BearerAuth')
    @api.expect("delete_account_parser", delete_account_input_parser)
    def delete(self):
        form_data = reqparse.request.form
        username = get_jwt_identity()
        print(username)
        password = form_data.get("password")
        if username is None or password is None:
            return {
                "error": "something went wrong"
            }, HTTPStatus.BAD_REQUEST
        user = Users.query.filter_by(email=username).first()
        if user is None:
            return {
                "error": "Invalid username"
            }, HTTPStatus.UNAUTHORIZED
        if user.password == password:
            try:
                profile = Profiles.query.filter_by(user_id=user.id).first()
                if profile != None:
                    database.session.delete(profile)
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