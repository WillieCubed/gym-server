"""A test runner for all Gym Server tests."""

import unittest

from gym_server.tests.server.experiment_tests import ExperimentNetworkingTestCase


def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(ExperimentNetworkingTestCase)
    return test_suite


if __name__ == '__main__':
    suite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
