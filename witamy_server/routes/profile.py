from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt, create_access_token
from .. import api
from ..models import Profiles
from flask_restx.utils import HTTPStatus
from ..parser import update_profile_parser

class Profile(Resource):
    method_decorators = [jwt_required()]

    @api.doc(security='BearerAuth')
    def get(self):
        profile = Profiles.query.filter_by(user_id=get_jwt().get("user_id")).first()
        if profile == None:
            return {
                "message": "profile is yet to be created"
            }, HTTPStatus.NOT_FOUND
        return {
            "name": profile.full_name,
            "email": get_jwt_identity(), # revoke token after email update and send new token
            "user_type": profile.user_type,
            "profile_picture": profile.profile_picture,
            "connection_count": profile.connection_count,
            "locale": profile.locale,
            "about_me": profile.about_me,
            "profile_privacy": profile.profile_privacy
        }
    
    @api.doc(security='BearerAuth')
    @api.expect("update_profile_parser", update_profile_parser)
    def put(self):
        json_data = update_profile_parser.parse_args() 
        user_id = get_jwt().get("user_id")
        profile = Profiles.query.filter_by(user_id=user_id).first()
        if profile is None:
            return {
                "message": "profile is yet to be created"
            }, HTTPStatus.NOT_FOUND
        
        # revoke token after email update and send new token
        return {
            "message": "updated profile",
            "jwt_token": create_access_token(identity=json_data.get("email"), additional_claims={"user_id": user_id})
        }, HTTPStatus.CREATED