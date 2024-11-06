from ..models import Profiles
from flask_restx import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt
from .. import api
from flask_restx.utils import HTTPStatus
from ..parser import create_profile_parser
from .. import database

class CreateProfile(Resource):
    method_decorators = [jwt_required()]

    @api.doc(security='BearerAuth')
    @api.expect("create_profile", create_profile_parser)
    def post(self):
        json_data = create_profile_parser.parse_args() 
        user_id = user_id=get_jwt().get("user_id")
        user_profile = Profiles.query.filter_by(user_id=user_id).first()
        if user_profile != None:
            return {
                "message": "Your profile already exist"
            }, HTTPStatus.FORBIDDEN
        profile = Profiles(user_id=user_id)
        profile.about_me = json_data.get("about_me")
        profile.email = json_data.get("email")
        profile.full_name = json_data.get("name")
        profile.locale = json_data.get("locale")
        profile.profile_picture = json_data.get("profile_picture")
        profile.user_type = json_data.get("user_type")
        try:
            database.session.add(profile)
            database.session.commit()
        except:
            return {
                "message": "something went wrong"
            }, HTTPStatus.BAD_REQUEST
        return {
            "message": "Created user profile"
        }, 201