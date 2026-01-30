from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('website', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        # In a real app, you would check credentials here
        return redirect(url_for('catalogue.index') + '#catalogue_recherche')
    return render_template('login.html')