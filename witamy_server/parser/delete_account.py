from flask_restx import reqparse

delete_account_input_parser = reqparse.RequestParser()
delete_account_input_parser.add_argument("password", type=str, location="form", required=True, help="Account password")