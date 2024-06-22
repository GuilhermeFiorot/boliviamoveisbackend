import os
from dotenv import load_dotenv

#load_dotenv()

class Config:
    #BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite://app.db" #os.getenv('DATABASE_URL', f'sqlite:///{os.path.join(BASE_DIR, "app.db")}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "JwtSecretKey" #os.getenv('JWT_SECRET_KEY', 'your_secret_key')