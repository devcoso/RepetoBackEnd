from flask import Blueprint, jsonify, request
main = Blueprint('index_blueprint', __name__)


@main.route('/')
def index():
    try:
        return jsonify({'status': True,'message': 'Hola Mundo'})
    except Exception as ex:
        return jsonify({'status': False,'message': str(ex)}), 500