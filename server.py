#!/usr/bin/env python3
"""Utility script to start Gym Server."""

import os

from gym_server import app

DEBUG_FLAG = 'GYM_DEBUG'

HOST = '0.0.0.0'

if __name__ == '__main__':
    app.run(debug=os.getenv(DEBUG_FLAG, False), host=HOST)
