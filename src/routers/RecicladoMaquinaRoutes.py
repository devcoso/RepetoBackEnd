from flask import Blueprint, jsonify, request

from models.RecicladoMaquinaModel import RecicladoMaquinaModel

from models.entities.RecicladoMaquina import RecicladoMaquina

main = Blueprint('recicladoMaquina_blueprint', __name__)


@main.route('/')
def api():
    try:
        return jsonify({'status': True,'mensaje': 'Api Maquina'})
    except Exception as ex:
        return jsonify({'status': False,'mensaje': str(ex)}), 500
    
@main.route('/consultar', methods=['POST'])
def consultar_reciclado_maquina():
    try:
        datos = RecicladoMaquinaModel.get_RecicladoMaquina(request.json['Maquina'])
        return jsonify(datos)
    except Exception as ex:
        return jsonify({'status': False,'mensaje': str(ex)}), 500
    
@main.route('/agregar', methods=['POST'])
def agregar_reciclado_maquina():
    try:
        recicladoMaquina = RecicladoMaquina(None,request.json['Maquina'],None,None,None)
        datos = RecicladoMaquinaModel.add_RecicladoMaquina(recicladoMaquina)
        return jsonify(datos)
    except Exception as ex:
        return jsonify({'status': False,'mensaje': str(ex)}), 500
    
@main.route('/eliminar_registros', methods=['POST'])
def eliminar_reciclado_maquina():
    try:
        recicladoMaquina = RecicladoMaquina(None,request.json['Maquina'],None,None,None)
        datos = RecicladoMaquinaModel.delete_RecicladoMaquina(recicladoMaquina)
        return jsonify(datos)
    except Exception as ex:
        return jsonify({'status': False,'mensaje': str(ex)}), 500