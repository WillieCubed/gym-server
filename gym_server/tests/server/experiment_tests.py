import unittest
from pathlib import Path

import requests


class ExperimentNetworkingTestCase(unittest.TestCase):
    TEST_BASE = 'localhost:5000'
    EXPERIMENTS_ENDPOINT = f'{TEST_BASE}/experiments'
    TEST_EXPERIMENT_LOCATION = f'{EXPERIMENTS_ENDPOINT}/test'
    EXPERIMENT_CONFIG_LOCATION = Path() / 'experiment_config_test.json'
    TEST_AUTH_TOKEN = 'test_token'

    def setUp(self) -> None:
        super().setUp()

    def test_create(self):
        """Test creation of an experiment."""
        config = open(self.EXPERIMENT_CONFIG_LOCATION, 'rb')
        response = requests.post(
            self.EXPERIMENTS_ENDPOINT,
            files={
                'document': config
            },
            data={

            },
            headers={
                'Content-Type': 'multipart/form-data'
            },
        )
        self.assertTrue(response.ok)
        # TODO: Check response

    def test_fetch(self):
        response = requests.get(self.TEST_EXPERIMENT_LOCATION)
        self.assertTrue(response.ok)

    def test_delete(self):
        """Test deletion of experiment data."""
        response = requests.delete(
            # TODO: Write endpoint to always regenerate deleted
            self.TEST_EXPERIMENT_LOCATION,
        )
        self.assertTrue(response.ok)


if __name__ == '__main__':
    unittest.main()
