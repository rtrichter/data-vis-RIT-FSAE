from flask import Flask

def init_app() -> Flask:
    """Initialize the core application"""
    app = Flask(__name__)

    # register blueprints
    from app.home.blueprint import blueprint
    app.register_blueprint(blueprint)
    

    return app
    