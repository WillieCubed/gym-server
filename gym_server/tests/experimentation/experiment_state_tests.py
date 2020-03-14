"""Unit tests for experimentation."""

import unittest

from gym_server.experiments.orchestrator import ExperimentOrchestrator, Experiment

BASE_URL = 'localhost:5000'

EXPERIMENTS_ENDPOINT = f'{BASE_URL}/experiments'


class ExperimentStateTestSuite(unittest.TestCase):
    """ExperimentOrchestrator tests."""

    def test_orchestrator(self):
        db = ...  # TODO: Create mock db
        orchestrator = ExperimentOrchestrator(db)


class RealtimeExperimentTestCase(unittest.TestCase):

    def test_start(self):
        pass


class AsynchronousTestCase(unittest.TestCase):

    def test_commands(self):
        experiment = Experiment() # TODO: Don't fetch experiment out of thin air.

        """Send a series of commands directly to an asynchronous Experiment."""


if __name__ == '__main__':
    unittest.main()
