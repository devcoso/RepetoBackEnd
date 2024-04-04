from flask import Flask

from config import config
from flask_cors import CORS


#Router
from routers import IndexRoutes
from routers import AuthRoutes
from routers import PersonaRoutes
from routers import RecicladoRoutes
from routers import RecicladoMaquinaRoutes

app = Flask(__name__)
CORS(app)

def page_not_found(error):
    return "<h1>Página no encontrada</h1>",404

if __name__ == '__main__':

    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(IndexRoutes.main,url_prefix='/')
    app.register_blueprint(AuthRoutes.main,url_prefix='/api/auth')
    app.register_blueprint(PersonaRoutes.main,url_prefix='/api/persona')
    app.register_blueprint(RecicladoMaquinaRoutes.main,url_prefix='/api/recic_maquina')
    app.register_blueprint(RecicladoRoutes.main,url_prefix='/api/reciclado')

    # Error handlers
    app.register_error_handler(404,page_not_found)
    app.run(debug=True,host='192.168.190.68',port=3000)
    # app.run(debug=True,host='172.20.12.204',port=3000)
    # app.run(debug=True)
