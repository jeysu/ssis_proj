from flask import Blueprint

college_bp = Blueprint('college', __name__, template_folder='templates')

from app.college import routes