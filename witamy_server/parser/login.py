from flask_restx import reqparse

login_input_parser = reqparse.RequestParser()
login_input_parser.add_argument("username", type=str, location="form", required=True, help="Account username", default="guest")
login_input_parser.add_argument("password", type=str, location="form", required=True, help="Account password", default="Password12")