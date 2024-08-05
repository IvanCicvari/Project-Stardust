from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
from Config import Config
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    dictConfig(app.config['LOGGING'])
    
    db.init_app(app)
    with app.app_context():
        try:
            # Test database connection
            db.engine.connect()
            app.logger.info("Database connection successful.")
            # Ensure all tables are created (only for development)
            db.create_all()

        except Exception as e:
            app.logger.error(f"Database connection failed: {e}")

    # Import and register blueprints
    from Routs.UserRouts import bp as user_bp
    app.register_blueprint(user_bp)

    # Swagger UI setup
    SWAGGER_URL = "/swagger"
    API_URL = "/static/swagger.json"
    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': 'Access API'
        }
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
    
    return app
