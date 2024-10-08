from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
from .config import Config
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})  # Allow all origins for API routes

    app.config.from_object(Config)
    
    dictConfig(app.config['LOGGING'])
    
    db.init_app(app)
    with app.app_context():
        try:
            db.engine.connect()
            app.logger.info("Database connection successful.")
            db.create_all()
        except Exception as e:
            app.logger.error(f"Database connection failed: {e}")
    jwt = JWTManager(app)

    from .api.Routs.UserRouts import bp as user_bp
    app.register_blueprint(user_bp)
    
    return app
