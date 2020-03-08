"""Logging utilities for the server.

This deploy this on a cloud solution besides Google Cloud, this is the file to
modify.
"""
import os
import logging

from google.cloud import logging as glogging

LOG_NAME = 'GYM_SERVER'


class LoggingError(Exception):
    """An error raised when a logging error occurs"""


class GymServerLogger(logging.Logger):
    def __init__(self, use_remote: bool = False):
        super().__init__(LOG_NAME)
        if use_remote:
            self._init_remote_logger()
            return
        self._remote_log_client = None
        self._use_remote = use_remote

    def _init_remote_logger(self):
        if not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
            # TODO: Put this into separate function that takes credentials as a param
            raise LoggingError('Remote logger option enabled but GOOGLE_APPLICATION_CREDENTIALS is not set.')
        # Connects the logger to the root gym_logging handler; by default this captures
        # all logs at INFO level and higher
        self._remote_log_client = glogging.Client()
        self._remote_log_client.setup_logging()


# Instantiates a client
def init_logging():
    """Return a logger."""
    return GymServerLogger()
