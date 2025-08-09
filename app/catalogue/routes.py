from flask import Blueprint, render_template
bp = Blueprint('catalogue', __name__, url_prefix='/catalogue', template_folder='templates')
@bp.route('/')
def index():
    return render_template('catalogue/index.html')