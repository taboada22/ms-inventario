from app.config import config
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_caching import Cache
from app.config.config_cache import cache_config




db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cache = Cache()

def create_app() -> None:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cache.init_app(app, config=cache_config)
    
    from app.resources import stock
    app.register_blueprint(stock)

    
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
