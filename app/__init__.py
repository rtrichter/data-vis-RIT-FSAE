from flask import Flask

def init_app() -> Flask:
    """Initialize the core application"""
    app = Flask(__name__)

    # register blueprints
    from app.home.blueprint import blueprint as bp1
    app.register_blueprint(bp1)
    from app.plotly_test.blueprint import blueprint as bp2
    app.register_blueprint(bp2)
    

    return app
    