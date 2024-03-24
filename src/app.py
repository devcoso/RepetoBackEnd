from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from config import config

#Services
from services.AuthService import AuthService
#Models
from models.User import User

app = Flask(__name__)
db = MySQL(app)

#Routes
@app.route('/')
def index():
    return jsonify({'message': 'API Repeto'})

@app.route('/login', methods=['POST'])
def login():
    user = User(None, None, request.form['email'], request.form['password'])
    user = AuthService.login(db, user)
    if user != None:
        return jsonify(user)
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
        
@app.route('/register', methods=['POST'])
def register():
    user = User(None, request.form['name'], request.form['email'], request.form['password'])
    user = AuthService.register(db, user)
    if user != None:
        return jsonify(user)
    else:
        return jsonify({'message': 'User already exists'}), 401

#Error 404
def status_404(error):
    return jsonify({'message': 'Not found'}), 404

#Run
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, status_404)
    app.run()