#!/usr/bin/python3
"""
Module to handle all default RESTful API actions for User objects.
"""

from flask import jsonify, make_response, request, abort
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieve the list of all User objects"""
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieve a User object by ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete a User object by ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Create a new User"""
    body = request.get_json()
    if body is None:
        abort(400, description="Not a JSON")
    if 'email' not in body:
        abort(400, description="Missing email")
    if 'password' not in body:
        abort(400, description="Missing password")

    user = User(**body)
    user.save()
    return make_response(jsonify(user.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Update an existing User object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    body = request.get_json()
    if body is None:
        abort(400, description="Not a JSON")

    ignore_keys = {'id', 'email', 'created_at', 'updated_at'}
    for key, value in body.items():
        if key not in ignore_keys:
            setattr(user, key, value)

    user.save()
    return make_response(jsonify(user.to_dict()), 200)
