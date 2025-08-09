from flask import Blueprint, render_template
bp = Blueprint('ventes', __name__, url_prefix='/ventes', template_folder='templates')
@bp.route('/')
def index():
    return render_template('ventes/index.html')