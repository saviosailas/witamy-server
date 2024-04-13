from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///witamy.db"

db = SQLAlchemy(app)

api = Api(app=app,
          version="0.1.a",
          description="RESTFul API for witamy mobile and web app",
          title="Witamy API",
          default="Account management",
          default_label="Endpoints for managing account",
          prefix="/api/v1/",
          validate=True,
          doc="/")

from . import urls

@app.cli.command()
def create_database():
    # python -m flask --app witamy_server create-database
    db.create_all()