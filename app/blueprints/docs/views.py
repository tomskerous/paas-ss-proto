from flask import (
  render_template,
  Blueprint,
  current_app)

import json
import os

docs = Blueprint('docs', __name__, url_prefix='/docs')

@docs.route('/publishing-on-paas')
def publishing():
  return render_template('docs/publishing-on-paas.html')