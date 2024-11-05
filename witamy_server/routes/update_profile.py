from ..models import Profiles
from flask_restx import Resource, reqparse
from flask_jwt_extended import jwt_required

class UpdateProfile(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        json_data = reqparse.request.get_json()
        print(json_data)
        return {}, 201