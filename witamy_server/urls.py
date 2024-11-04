from . import routes
from . import api

api.add_resource(routes.SignUp, "/signup", strict_slashes=False)
api.add_resource(routes.Login, "/login", strict_slashes=False)
api.add_resource(routes.UpdatePassword, "/update_password", strict_slashes=False)
api.add_resource(routes.DeleteAccount, "/delete", strict_slashes=False)


api.add_resource(routes.DebugPipeline, "/debug-pipeline", strict_slashes=False)