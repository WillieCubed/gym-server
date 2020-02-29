from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from ..database.config import Config


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

DATABASE_PATH = Path().absolute() / 'gym_server.db'

# This has to follow app = Flask(__name__) otherwise there will be ImportError.
from .routes import index

__all__ = ['app', 'db']
