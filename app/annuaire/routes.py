from flask import Blueprint, render_template
bp = Blueprint('annuaire', __name__, url_prefix='/annuaire', template_folder='templates')
@bp.route('/')
def index():
    return render_template('annuaire/index.html')