from flask import Blueprint, jsonify

app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})

