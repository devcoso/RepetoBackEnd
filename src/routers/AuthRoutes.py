from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Usuario import Usuario
# Models
from models.UsuarioModel import UsuarioModel

main = Blueprint('auth_blueprint', __name__)


@main.route('/login', methods=['POST'])
def login():
    try:
        inicioSesion = UsuarioModel.login(request.json['NombreUsuario'],request.json['Contrasenia'])
        return jsonify(inicioSesion)
    except Exception as ex:
        return jsonify({'status': False,'message': str(ex)}), 500

@main.route('/me')
def me():
    try:
        me = UsuarioModel.mis_datos(request.headers)
        return jsonify(me)
    except Exception as ex:
        return jsonify({'status': False,'message': str(ex)}), 500

@main.route('/restablecer', methods=['POST'])
def restablecer_contrasenia():
    try:
        restablecer = UsuarioModel.get_usuario_restablecer(request.json['Correo'])
        return jsonify(restablecer)
    except Exception as ex:
        return jsonify({'status': False,'message': str(ex)}), 500
    
@main.route('/cambiarContra', methods=['POST'])
def update_contrasenia():
    try:
        nueva_contrasenia = UsuarioModel.update_usuario_contrasenia(request.headers,request.json['Contrasenia'])
        return jsonify(nueva_contrasenia)
    except Exception as ex:
        return jsonify({'status': False,'message': str(ex)}), 500
    
@main.route('/registro', methods=['POST'])
def add_usuario():
    try:
        usuario = Usuario(None,request.json['NombreUsuario'],request.json['Contrasenia'],None,None,None,
                      request.json['Nombre'],request.json['PrimerApellido'],request.json['SegundoApellido'],request.json['Correo'],None,None,None,None)
        nuevo_usuario = UsuarioModel.add_usuario(usuario)
        return jsonify(nuevo_usuario)
    except Exception as ex:
        return jsonify({'status': False,'message': str(ex)}), 500
    
