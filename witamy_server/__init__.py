from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from os import environ
from datetime import timedelta

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///witamy.db"
if environ.get("jwt_secret") is not None:
    app.config["JWT_SECRET_KEY"] = environ.get("jwt_secret")
else:
    app.config["JWT_SECRET_KEY"] = "donot-use-this-key-on-production"

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=10)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=360)

jwt_authorizations = {
    'BearerAuth': {
        'type': 'apiKey',
        'scheme': 'bearer',
        'name': 'Authorization',
        'in': 'header'
    },
    'AdminBearerAuth': {
        'type': 'apiKey',
        'scheme': 'bearer',
        'name': 'X-Authorization',
        'in': 'header'
    }
}

api = Api(app=app,
          version="0.1.a",
          description="RESTFul API for witamy mobile and web app",
          title="Witamy API",
          default="Account management",
          default_label="Endpoints for managing account",
          prefix="/api/v1/",
          validate=True,
          doc="/",
          authorizations=jwt_authorizations)

database = SQLAlchemy(app)

jwt = JWTManager(app)

from . import urls

@app.cli.command()
def create_database():
    # python -m flask --app witamy_server create-database
    # or use flask shell:
    #   set FLASK_APP=witamy_server
    #   python -m flask shell
    #   >>> from witamy_server import database
    #   >>> database.create_all()
    #   >>> exit()
    database.create_all()