from flask_restx import reqparse

signup_input_parser = reqparse.RequestParser()
signup_input_parser.add_argument("username", type=str, location="form", required=True, help="Account username")
signup_input_parser.add_argument("password", type=str, location="form", required=True, help="Account password")