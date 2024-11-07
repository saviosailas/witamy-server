from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt, create_access_token
from .. import api, database
from ..models import Profiles, Users
from flask_restx.utils import HTTPStatus
from ..parser import update_profile_parser

class Profile(Resource):
    method_decorators = [jwt_required()]

    @api.doc(security='BearerAuth')
    def get(self):
        user_id = get_jwt().get("user_id")
        profile = Profiles.query.filter_by(user_id=user_id).first()
        if profile == None:
            return {
                "message": "profile is yet to be created"
            }, HTTPStatus.NOT_FOUND
        user = Users.query.filter_by(id=user_id).first()
        return {
            "name": profile.full_name,
            "email": user.email, # revoke token after email update and send new token
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
        name = json_data.get("fullname")
        user_type = json_data.get("user_type")
        profile_picture = json_data.get("profile_picture")
        locate = json_data.get("locate")
        about_me = json_data.get("about_me")
        profile_privacy = json_data.get("profile_privacy")
        # revoke token after email update and send new token
        if name is not None and name != "":
            profile.name = name
        if user_type is not None and name != "":
            profile.user_type = user_type
        if profile_picture is not None:
            profile.profile_picture = profile_picture
        if about_me is not None:
            profile.about_me = about_me
        if profile_privacy is not None and isinstance(profile_privacy, int) and profile_privacy in (0, 1):
            profile.profile_privacy = profile_privacy

        try:
            database.session.commit()
        except Exception as exp:
            return {
                "message": "something went wrong"
            }, HTTPStatus.BAD_REQUEST

        email = json_data.get("email")
        if email is None:
            return {
                "message": "updated profile"
            }, HTTPStatus.CREATED
        else:
            user = Users.query.filter_by(id=user_id).first()
            user.email = email
            try:
                database.session.commit()
            except Exception as exp:
                return {
                    "message": "something went wrong on updating email"
                }, HTTPStatus.BAD_REQUEST
            return {
                "message": "updated profile",
                "jwt_token": create_access_token(identity=json_data.get("email"), additional_claims={"user_id": user_id})
            }, HTTPStatus.CREATED