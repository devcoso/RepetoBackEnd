from flask import Flask

from config import config

#Router
from routers import IndexRoutes
from routers import AuthRoutes

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Página no encontrada</h1>",404

if __name__ == '__main__':

    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(IndexRoutes.main,url_prefix='/')
    app.register_blueprint(AuthRoutes.main,url_prefix='/api/auth')

    # Error handlers
    app.register_error_handler(404,page_not_found)

    # app.run(debug=True,host='192.168.100.30',port=3000)
    app.run(debug=True)
