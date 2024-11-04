from flask_restx import reqparse

debug_input_parser = reqparse.RequestParser()
debug_input_parser.add_argument("key", type=str, location="headers", required=True, help="secret + pubic key")
