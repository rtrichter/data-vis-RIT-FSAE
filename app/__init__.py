from flask import Flask
import os
from dotenv import dotenv_values

config = dotenv_values(".env")

# helper functions -----------------------------------------------------------
def purge_directory(path: str):
    files = os.listdir(path)
    for file in files:
        file = os.path.join(path, file)
        if os.path.isfile(file):
            os.remove(file)
        elif os.path.isdir(file):
            purge_directory(file)
            os.removedirs(file)
        else:
            raise RuntimeError(f"{file} is neither a directory nor a file")
    

# app start/stop -------------------------------------------------------------
def shutdown(app: Flask) -> None:
    # make sure there are no temporary files
    purge_directory(config["TMP"])


def init_app() -> Flask:
    """Initialize the core application"""
    app = Flask(__name__)

    # register blueprints
    from app.home.blueprint import blueprint as bp1
    app.register_blueprint(bp1)
    from app.plotly_test.blueprint import blueprint as bp2
    app.register_blueprint(bp2)
    

    return app
    