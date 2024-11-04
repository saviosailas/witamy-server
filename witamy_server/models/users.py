from .. import database

class User(database.Model):

    __tablename__ = "User"
    
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(140), unique=True, nullable=False)
    password = database.Column(database.String(40), nullable=False)