from .routes import SignUp, Login, UpdatePassword, DeleteAccount
from .routes import DebugPipeline
from . import api

api.add_resource(SignUp, "/signup", strict_slashes=False)
api.add_resource(Login, "/login", strict_slashes=False)
api.add_resource(UpdatePassword, "/update_password", strict_slashes=False)
api.add_resource(DeleteAccount, "/delete", strict_slashes=False)
api.add_resource(DebugPipeline, "/debug-pipeline", strict_slashes=False)