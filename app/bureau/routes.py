from flask import Blueprint, render_template
bp = Blueprint('bureau', __name__, url_prefix='/bureau', template_folder='templates')
@bp.route('/')
def index():
    return render_template('bureau/index.html')