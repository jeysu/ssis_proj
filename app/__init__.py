from flask import Flask, render_template
from flaskext.mysql import MySQL
import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    mysql.init_app(app)
    
    cloudinary.config(
        cloud_name=app.config['CLOUDINARY_CLOUD_NAME'],
        api_key=app.config['CLOUDINARY_API_KEY'],
        api_secret=app.config['CLOUDINARY_API_SECRET']
    )
    
    from app.student import student_bp
    from app.program import program_bp
    from app.college import college_bp
    
    app.register_blueprint(student_bp, url_prefix='/student')
    app.register_blueprint(program_bp, url_prefix='/program')
    app.register_blueprint(college_bp, url_prefix='/college')
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app