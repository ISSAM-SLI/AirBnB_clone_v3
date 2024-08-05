#!/usr/bin/python3
"""
Module that sets up the blueprint for API views
"""

from api.v1.views.states import *
from api.v1.views.index import *
from api.v1.views.cities import *
from flask import Blueprint

app_views = Blueprint('app_view', __name__, url_prefix='/api/v1/')
