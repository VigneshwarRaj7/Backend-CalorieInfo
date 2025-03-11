from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

   
    from app.Controllers.controller import controller_bp  
    app.register_blueprint(controller_bp)  

    return app
