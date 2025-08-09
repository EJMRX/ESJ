from flask import Blueprint, render_template
bp = Blueprint('comptabilite', __name__, url_prefix='/comptabilite', template_folder='templates')
@bp.route('/')
def index():
    return render_template('comptabilite/index.html')