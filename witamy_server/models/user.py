from .. import database

class Users(database.Model):

    __tablename__ = "users"
    
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(140), unique=True, nullable=False)
    password = database.Column(database.String(40), nullable=False)