from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from gym_server.database.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    """Create a new Flask app instance.

    Args:
        config_class: An object containing default application configuration
    """
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_class)

    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    # Register blueprints
    flask_app.register_blueprint(experiments_bp)
    flask_app.register_blueprint(auth_bp, url_prefix='/auth')

    return flask_app


DATABASE_PATH = Path().absolute() / 'gym_server.db'

from .experiments import bp as experiments_bp
from .auth import bp as auth_bp

app = create_app()

__all__ = ['app', 'db']

# This has to follow app = Flask(__name__) otherwise there will be ImportError.
from .routes import index
