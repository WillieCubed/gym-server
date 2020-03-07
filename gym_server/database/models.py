"""Models for Gym Server experiments."""

from datetime import datetime

from gym_server.app import db
from gym_server.experiments.models import ExperimentStatus


class UserModel(db.Model):
    """A user object model.

    Attributes:
        id: The primary identifier for a user
        name: A name used to reference the user
        email: A email used to reset password
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.Text)
    password = db.Column(db.String(64))
    experiments = db.relationship('Experiment', back_populates='users', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.id}>'


class ExperimentModel(db.Model):
    """An experiment object model.

    TODO: Support multiple owners for an experiment (IAM).

    Attributes:
        id: The primary identifier for an experiment.
        name: A user-specified name for this experiment.
        description: Optional user-specified notes for this experiment.
        creation_date: The timestamp indicating when this experiment had its initial
            configuration created.
        config_name: The name of the experiment configuration file
        owner: The ID of the user who owns this experiment
    """

    __tablename__ = 'experiments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64))
    creation_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    last_updated = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    status = db.Column(db.Enum(ExperimentStatus), index=True)
    config_name = db.Column(db.String(64))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    owner = db.relationship('Experiment', back_populates='experiments')

    def __repr__(self):
        return f'<Experiment {self.id}>'
