from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config.config import config
#from app.config.cache_config import cache_config
#from app.resources.routes import RouteApp
#from flask_caching import Cache
import os
from app.extensions import db

from app.resource.usuario_resource import user_bp  # Importar tu blueprint TEMPORAL

# # Instancias globales de extensiones
migrate = Migrate()
# cache = Cache()

def create_app():
    app_context = os.getenv("FLASK_CONTEXT")
    print(f"app_context: {app_context}")

    app = Flask(__name__)

    configuration = config[app_context if app_context else 'development']
    app.config.from_object(configuration)
    app.secret_key = os.getenv('SECRET_KEY')
    
    db.init_app(app)
    migrate.init_app(app, db)

    # cache.init_app(app, config=cache_config)

    # route = RouteApp()
    # route.init_app(app)
    app.register_blueprint(user_bp) # TEMPORAL


    return app