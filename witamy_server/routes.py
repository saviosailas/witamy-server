from flask_restx import Resource

class SignUp(Resource):
    method_decorators = []

    def post(self):
        return {}
    
class Login(Resource):
    method_decorators = []

    def post(self):
        return {}
    
class UpdatePassword(Resource):
    method_decorators = []

    def put(self):
        return {}
    
class DeleteAccount(Resource):
    method_decorators = []

    def delete(self):
        return {}

class DebugPipeline(Resource):
    method_decorators = []

    def get(self):
        return {}