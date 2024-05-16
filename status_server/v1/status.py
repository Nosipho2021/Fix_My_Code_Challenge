# File: api/v1/views/status.py

from flask import Blueprint, jsonify

# Create a blueprint for the status endpoints
status_bp = Blueprint('status', __name__)


# Define a route for the status endpoint
@status_bp.route('/api/v1/status', methods=['GET'])
def get_status():
    """ Return the status of the API """
    return jsonify({"status": "OK"})

