from flask import Blueprint, jsonify, request

# Entities
from models.entities.Reciclado import Reciclado
# Models
from models.RecicladoModel import RecicladoModel

main = Blueprint('reciclado_blueprint', __name__)


@main.route('/')
def index():
    try:
        return jsonify({'status': True,'message': 'Reciclado'})
    except Exception as ex:
        return jsonify({'status': False,'message': str(ex)}), 500
    
@main.route('/mis_datos')
def reciclado_por_persona():
    try:
        datos = RecicladoModel.get_Reciclados_Persona(request.headers)
        return jsonify(datos)
    except Exception as ex:
        return jsonify({'status': False,'mensaje': str(ex)}), 500
    
@main.route('/registro_sinP', methods=['POST'])
def add_reciclado_sinP():
    try:
        reciclado = Reciclado(None,None,request.json['Maquina'],None,None,None)
        datos = RecicladoModel.add_Reciclado_SinP(reciclado)
        return jsonify(datos)
    except Exception as ex:
        return jsonify({'status': False,'mensaje': str(ex)}), 500
    
@main.route('/asignarPersona', methods=['POST'])
def update_reciclado_asigPersona():
    try:
        datos = RecicladoModel.update_Reciclado_AsigP(request.headers,request.json['Reciclado'])
        return jsonify(datos)
    except Exception as ex:
        return jsonify({'status': False,'mensaje': str(ex)}), 500