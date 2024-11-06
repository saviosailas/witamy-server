from ..models import Profiles
from flask_restx import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt
from .. import api

class CreateProfile(Resource):
    method_decorators = [jwt_required()]

    @api.doc(security='BearerAuth')
    def post(self):
        json_data = reqparse.request.get_json()
        # try? fetch exiting data from db
        user_profile = Profiles(user_id=get_jwt().get("user_id"))
        print(json_data)
        return {}, 201