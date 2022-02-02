from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config["SECRET_KEY"] = "SECRET_KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "JWT_SECRET_KEY"
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

import views, models, resources

api.add_resource(resources.UserRegistration, "/registration")
api.add_resource(resources.UserLogin, "/login")
api.add_resource(resources.UserLogoutAccess, "/logout/access")
api.add_resource(resources.UserLogoutRefresh, "/logout/refresh")
api.add_resource(resources.TokenRefresh, "/token/refresh")
api.add_resource(resources.AllUsers, "/users")
api.add_resource(resources.Video, "/video/<int:video_id>")
