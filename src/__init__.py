from flask import Flask, jsonify
from flask_cors import CORS

from .routes import AuthRoutes, IndexRoutes

app = Flask(__name__)
CORS(app)

def init_app(config):
    app.config.from_object(config)

    #Blueprints 
    app.register_blueprint(AuthRoutes.main, url_prefix='/auth')
    app.register_blueprint(IndexRoutes.main, url_prefix='/')

    return app