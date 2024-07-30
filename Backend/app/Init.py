import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
from Config import Config  # Import the Config class

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Use the Config class

    # Initialize logging
    dictConfig(app.config['LOGGING'])

    db.init_app(app)

    with app.app_context():
        try:
            # Test database connection
            db.engine.connect()
            logging.info("Database connection successful.")
            
            # Test a simple query
            result = db.session.execute("SELECT 1")
            logging.info(f"Query result: {result.scalar()}")
        except Exception as e:
            logging.error(f"Database connection failed: {e}")

    return app
