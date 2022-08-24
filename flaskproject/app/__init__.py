from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import bus_page
    app.register_blueprint(bus_page.bp)
    return app