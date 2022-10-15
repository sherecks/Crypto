import os
from routes import pages
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def create_app():
    app=Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    client = MongoClient("mongodb://host/Cluster0")
    app.db = client.get_default_database()

    app.register_blueprint(pages)
    return app