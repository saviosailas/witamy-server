from flask_restx import reqparse

login_input_parser = reqparse.RequestParser()
login_input_parser.add_argument("username", type=str, location="form", required=True, help="Account username", default="guest")
login_input_parser.add_argument("password", type=str, location="form", required=True, help="Account password", default="Password12")


signup_input_parser = reqparse.RequestParser()
signup_input_parser.add_argument("username", type=str, location="form", required=True, help="Account username")
signup_input_parser.add_argument("password", type=str, location="form", required=True, help="Account password")

password_update_input_parser = reqparse.RequestParser()
password_update_input_parser.add_argument("username", type=str, location="form", required=True, help="Account username")
password_update_input_parser.add_argument("password", type=str, location="form", required=True, help="Account password")
password_update_input_parser.add_argument("new_password", type=str, location="form", required=True, help="New password")


delete_account_input_parser = reqparse.RequestParser()
delete_account_input_parser.add_argument("username", type=str, location="form", required=True, help="Account username")
delete_account_input_parser.add_argument("password", type=str, location="form", required=True, help="Account password")

debug_input_parser = reqparse.RequestParser()
debug_input_parser.add_argument("key", type=str, location="headers", required=True, help="secret + pubic key")
