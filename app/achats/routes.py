from flask import Blueprint, render_template
bp = Blueprint('achats', __name__, url_prefix='/achats', template_folder='templates')
@bp.route('/')
def index():
    return render_template('achats/index.html')