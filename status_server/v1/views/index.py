#!/usr/bin/python3
""" Index view
"""
from flask import jsonify

from api.v1.views import app_views


def index():
    """ Return a simple message """
    return jsonify({"message": "Welcome!"})
