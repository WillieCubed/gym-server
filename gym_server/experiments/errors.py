"""Exceptions raised when accessing experiment resources"""


class UnknownExperimentError(Exception):
    """Raised when the requested experiment data cannot be found on the server."""
    status_code = 400
    error_code = 10
    name = ''
    message = ''


class DatabaseError(Exception):
    """Raised when a database error occurs"""
    status_code = 500
