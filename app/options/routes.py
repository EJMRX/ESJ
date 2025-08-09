from flask import Blueprint, render_template
bp = Blueprint('options', __name__, url_prefix='/options', template_folder='templates')
@bp.route('/')
def index():
    return render_template('options/index.html')