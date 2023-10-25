from app import init_app, shutdown
from os import system

if __name__ == "__main__":
    app = init_app()
    try: 
        app.run()
    finally:
        shutdown(app)