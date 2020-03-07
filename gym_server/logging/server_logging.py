"""Logging utilities for the server.

This deploy this on a cloud solution besides Google Cloud, this is the file to
modify.
"""
import os
import logging

from google.cloud import logging as glogging

LOG_NAME = 'GYM_SERVER'


# Instantiates a client
def init_logging():
    """Return a logger."""
    if not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
        return logging.getLogger('gym_server')
    client = glogging.Client()

    # Connects the logger to the root logging handler; by default this captures
    # all logs at INFO level and higher
    client.setup_logging()

    return client.logger(LOG_NAME)
