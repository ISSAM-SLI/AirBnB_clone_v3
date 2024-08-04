#!/usr/bin/python3
"""
Module to provide JSON responses for API endpoints
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def index():
    """Return the status of the API"""
    response = {"status": "OK"}
    return jsonify(response)
