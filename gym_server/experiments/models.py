from enum import Enum


class ExperimentStatus(Enum):
    """The current state of an experiment."""
    not_started = 0
    starting = 1
    running = 2
    finished = 3
    error = 10
