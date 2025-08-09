from flask import Blueprint, render_template

bp = Blueprint('commande', __name__, url_prefix='/commande', template_folder='templates')

@bp.route('/')
def index():

    return render_template('commande/index.html')