from flask import Blueprint

program_bp = Blueprint('program', __name__, template_folder='templates')

from app.program import routes