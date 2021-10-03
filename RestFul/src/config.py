import os

class Config:
    DB = os.environ.get('DB')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
