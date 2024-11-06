from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from .. import api
from ..models import Profiles
from flask_restx.utils import HTTPStatus

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
            "username": get_jwt_identity(),
            "email": profile.email,
            "user_type": profile.user_type,
            "profile_picture": profile.profile_picture,
            "connection_count": profile.connection_count,
            "locale": profile.locale,
            "about_me": profile.about_me,
            "profile_privacy": profile.profile_privacy
        }
    
    @api.doc(security='BearerAuth')
    def put(self):
        return {
            "message": "updated profile"
        }, HTTPStatus.CREATED