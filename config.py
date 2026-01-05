import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    MYSQL_DATABASE_HOST = os.getenv('MYSQL_HOST')
    MYSQL_DATABASE_USER = os.getenv('MYSQL_USER')
    MYSQL_DATABASE_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DATABASE_DB = os.getenv('MYSQL_DB')
    MYSQL_DATABASE_PORT = int(os.getenv('MYSQL_PORT'))
    
    CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME')
    CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY')
    CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET')