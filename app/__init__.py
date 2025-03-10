from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Import controller and register it with the app
    from app.Controllers.controller import controller_bp  # Import your controller Blueprint
    app.register_blueprint(controller_bp)  # Register the blueprint

    return app
