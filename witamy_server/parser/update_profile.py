from flask_restx import reqparse

update_profile_parser = reqparse.RequestParser()
update_profile_parser.add_argument("email", type=str, location="json", help="new token will be generated for email update")
update_profile_parser.add_argument("full_name", location="json")
update_profile_parser.add_argument("user_type", location="json")
update_profile_parser.add_argument("profile_picture", location="json")
update_profile_parser.add_argument("locale", location="json")
update_profile_parser.add_argument("about_me", location="json")
update_profile_parser.add_argument("profile_privacy", type=int, location="json")