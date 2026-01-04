import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    MYSQL_DATABASE_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_DATABASE_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_DATABASE_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DATABASE_DB = os.getenv('MYSQL_DB', 'ssis_db')
    MYSQL_DATABASE_PORT = int(os.getenv('MYSQL_PORT', 3306))
    
    # Cloudinary settings
    CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME')
    CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY')
    CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET')