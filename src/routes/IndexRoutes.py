from flask import request, jsonify, Blueprint

main = Blueprint('index_blueprint', __name__)

@main.route('/')
def index():
    return jsonify({'message': 'API Repeto'})