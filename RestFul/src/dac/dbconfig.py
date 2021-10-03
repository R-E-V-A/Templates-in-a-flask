from flask_mongoengine import MongoEngine
from config import Config

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)