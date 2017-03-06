
from flask import (
  render_template,
  Blueprint,
  current_app)

ss = Blueprint('ss', __name__, url_prefix='/ss')

@ss.route('/')
@ss.route('/sign-in')
def sign_in():
  return render_template('sign_in.html')



