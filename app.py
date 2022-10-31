from routes import pages
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app=Flask(__name__)
    app.register_blueprint(pages)
    return app