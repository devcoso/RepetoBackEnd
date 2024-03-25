from flask import Flask

# Routes
from .routes import AuthRoutes, IndexRoutes, LanguageRoutes

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(AuthRoutes.main, url_prefix='/auth')

    return app