from flask import Flask
from app.config import load_configurations, configure_logging
from .views import webhook_blueprint
import os



def create_app():
    app = Flask(__name__)

    # Load configurations and logging settings
    load_configurations(app)
    configure_logging()
    app.config["VERIFY_TOKEN"] = os.getenv("VERIFY_TOKEN")


    # Import and register blueprints, if any
    app.register_blueprint(webhook_blueprint)


    return app
