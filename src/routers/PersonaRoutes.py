from flask import Blueprint, jsonify, request

main = Blueprint('persona_blueprint', __name__)
# Models
from models.PersonaModel import PersonaModel

@main.route('/datos')
def datos_general():
    try:
        datos = PersonaModel.datos_generales(request.headers)
        return jsonify(datos)
    except Exception as ex:
        return jsonify({'status': False,'mensaje': str(ex)}), 500