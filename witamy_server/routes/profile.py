from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from .. import api
from ..models import Profiles

class Profile(Resource):
    method_decorators = [jwt_required()]

    @api.doc(security='BearerAuth')
    def get(self):
        profile = Profiles(user_id=get_jwt().get("user_id"))
        profile.full_name = "test"
        profile.email = "test"
        profile.user_type = "test"
        profile.profile_picture = "test"
        profile.connection_count = "test"
        profile.locale = "test"
        profile.about_me = "test"
        profile.profile_privacy = 0

        print(profile.user_id)
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