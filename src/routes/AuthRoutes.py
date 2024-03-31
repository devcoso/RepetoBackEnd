from flask import request, jsonify, Blueprint
#Models
from src.models.User import User
#Services
from src.services.AuthService import AuthService

main = Blueprint('auth_blueprint', __name__)

@main.route('/login', methods=['POST'])
def login():
    user = User(None, None, request.json['email'], request.json['password'])
    user = AuthService.login(user)
    if user != None:
        return jsonify({'user': user, 'error': False})
    else:
        return jsonify({'message': 'Crendenciales inválidas', 'error': True}), 401
        
@main.route('/signup', methods=['POST'])
def register():
    user = User(None, request.json['name'], request.json['email'], request.json['password'])
    user = AuthService.register(user)
    if user['error'] == False:
        return jsonify({'user': user['user'], 'error': False})
    else:
        return jsonify({'message': user['message'], 'error': True}), 401
    
@main.route('/forgot-password', methods=['POST'])
def forgot_password():
    user = User(None, None, request.json['email'], None)
    user = AuthService.forgot_password(user)
    if user['error'] == False:
        return jsonify({'message': user['message'], 'error': False})
    else:
        return jsonify({'message': user['message'], 'error': True}), 401
    
@main.route('/reset-password', methods=['POST'])
def reset_password():
    response = AuthService.reset_password(request.json['token'], request.json['password'])
    if response['error'] == False:
        return jsonify({'message': response['message'], 'error': False})
    else:
        return jsonify({'message': response['message'], 'error': True}), 401

@main.route('/me' , methods=['GET'])
def me(): 
    user = AuthService.me(request.headers)
    print(request.headers)
    if user['error'] == False:
        return jsonify({'user': user['user'], 'error': False})
    else:
        return jsonify({'message': user['message'], 'error': True}), 401
