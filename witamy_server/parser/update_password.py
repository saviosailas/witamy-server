from flask_restx import reqparse

password_update_input_parser = reqparse.RequestParser()
password_update_input_parser.add_argument("password", type=str, location="form", required=True, help="Account password")
password_update_input_parser.add_argument("new_password", type=str, location="form", required=True, help="New password")