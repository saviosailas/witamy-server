from .. import database

class Profiles(database.Model):

    __tablename__ = "profiles"

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    full_name = database.Column(database.String(300), nullable=False)
    user_type = database.Column(database.String(10), nullable=False, default="platinum")
    profile_picture = database.Column(database.String(150))
    connection_count = database.Column(database.Integer, default=0)
    locale = database.Column(database.String(10), default="en-US")
    about_me = database.Column(database.Text)
    profile_privacy = database.Column(database.Integer, default=0)

    def __repr__(self):
        return f"<Profiles {self.full_name}, email {self.email}>"
