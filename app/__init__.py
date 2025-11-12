from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

# create app
app = Flask(__name__)
app.config.from_object(Config)

# initialise db and api
db = SQLAlchemy(app)
api = Api(app)

# import routes AFTER initializing db/api to avoid circular imports
from app import models  # noqa: F401, E402
from app.models import BookModel  # noqa: F401, E402
from app.routes import *  # noqa: F401, F403, E402


# health check route
@app.route("/")
def homepage():
    return "<h1>Health check</h1>"
