"""Configuration variables for the database."""

import os
import platform
from pathlib import Path

# TODO: Fix this hack and make

DB_NAME = 'gym-server.sqlite'
ENV_DB_URL = 'DATABASE_URL'

if platform.system() == 'Windows':
    db_path = str(Path(__file__).parent.parent / DB_NAME).replace('\\', '\\\\')
else:
    db_path = str(Path(__file__).parent.parent / DB_NAME)


class Config:
    """Gym Server environment variable configuration."""
    SQLALCHEMY_DATABASE_URI = os.environ.get(ENV_DB_URL) or \
                              f'sqlite:////{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
