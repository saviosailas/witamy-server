from flask_restx import reqparse

create_profile_parser = reqparse.RequestParser()
create_profile_parser.add_argument("name", type=str, required=True, help="full name cannot be blank", location="json")
create_profile_parser.add_argument("email", type=str, required=True, help="Email cannot be blank", location="json")
create_profile_parser.add_argument("user_type", type=str, required=True, help="platinum is default", location="json")
create_profile_parser.add_argument("profile_picture", type=str, required=False, help="Use meta data from file upload", location="json")
create_profile_parser.add_argument("locale", type=str, required=True, help="en-US is default", default="en_US", location="json")
create_profile_parser.add_argument("about_me", type=str, required=True, help="Info displayed on your bio.", location="json")
create_profile_parser.add_argument("profile_privacy", type=int, required=True, help="1 - public, 0 - private", default=1, location="json")
