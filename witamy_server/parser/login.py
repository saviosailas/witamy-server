from flask_restx import reqparse

login_input_parser = reqparse.RequestParser()
login_input_parser.add_argument("email", type=str, location="form", required=True, help="email is the username", default="guest")
login_input_parser.add_argument("password", type=str, location="form", required=True, help="Account password", default="Password12")