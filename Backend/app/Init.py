from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
from Config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    dictConfig(app.config['LOGGING'])
    
    db.init_app(app)
    
    with app.app_context():
        try:
            db.engine.connect()
            app.logger.info("Database connection successful.")
            result = db.session.execute("SELECT 1")
            app.logger.info(f"Query result: {result.scalar()}")
        except Exception as e:
            app.logger.error(f"Database connection failed: {e}")

    from Routs import UserRouts
    app.register_blueprint(UserRouts.bp)
    
    return app
