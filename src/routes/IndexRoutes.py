from flask import request, jsonify, Blueprint
from src.utils.Security import Security
from src.utils.EmailSender import EmailSender

main = Blueprint('index_blueprint', __name__)

@main.route('/')
def index():
    return jsonify({'message': 'API Repeto'})

@main.route('/private')
def private():
    has_access = Security.verify_token(request.headers)
    if has_access == None:
        return jsonify({'message': 'Unauthorized'}), 401
    return jsonify({'message': 'Access granted', 'user': has_access})
    