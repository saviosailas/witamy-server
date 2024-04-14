from flask_restx import Resource
from .parser import login_input_parser, signup_input_parser, password_update_input_parser, delete_account_input_parser
from .parser import debug_input_parser
from . import api

class SignUp(Resource):
    method_decorators = []

    @api.expect("signup_parser", signup_input_parser)
    def post(self):
        return {}
    
class Login(Resource):
    method_decorators = []

    @api.expect("login_parser", login_input_parser)
    def post(self):
        return {}
    
class UpdatePassword(Resource):
    method_decorators = []

    @api.expect("update_password_parser", password_update_input_parser)
    def put(self):
        return {}
    
class DeleteAccount(Resource):
    method_decorators = []

    @api.expect("delete_account_parser", delete_account_input_parser)
    def delete(self):
        return {}

class DebugPipeline(Resource):
    method_decorators = []

    @api.expect(debug_input_parser)
    def get(self):
        return {}