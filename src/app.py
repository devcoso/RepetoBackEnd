from flask import Flask

from config import config

#Router
from routers import AuthRoutes

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Página no encontrada</h1>",404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(AuthRoutes.main,url_prefix='/api/auth')

    # Error handlers
    app.register_error_handler(404,page_not_found)

    app.run(debug=True,port=5000)
