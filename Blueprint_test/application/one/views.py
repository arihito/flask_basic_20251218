from flask import Blueprint, render_template

one_bp = Blueprint('one_app', __name__, url_prefix='/one')

@one_bp.route('/')
def show_template():
  return render_template('one/index.j2')
