from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import api

class Profile(Resource):
    method_decorators = [jwt_required()]

    @api.doc(security='BearerAuth')
    def get(self):
        return {
            "name": "test user",
            "username": get_jwt_identity(),
            "email": "example@gmail.com",
            "user_type": "golden",
            "profile_picture": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
            "connection_count": 13,
            "locale": "en-US",
            "about_me": "Hi! I joined Witamy on 1975!. see you soon.",
            "profile_privacy": "public"

        }