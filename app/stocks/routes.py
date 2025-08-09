from flask import Blueprint, render_template
bp = Blueprint('stocks', __name__, url_prefix='/stocks', template_folder='templates')
@bp.route('/')
def index():
    return render_template('stocks/index.html')