from flask import (
  render_template,
  Blueprint,
  current_app)

import json
import os

docs = Blueprint('docs', __name__, url_prefix='/docs')

@docs.route('/', defaults={'path': ''})
@docs.route('/<path:path>')
def catch_all(path):
  # need to see if it exists
  return render_template( 'docs/' + path )

@docs.route('/publishing-on-paas')
def publishing():
  return render_template('docs/publishing-on-paas.html')