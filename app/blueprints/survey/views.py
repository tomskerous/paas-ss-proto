from flask import (
  render_template,
  Blueprint,
  current_app)

import json
import os

survey = Blueprint('survey', __name__, url_prefix='/survey')

@survey.route('/', defaults={'path': ''})
@survey.route('/<path:path>')
def catch_all(path):
  # need to see if it exists
  return render_template( 'survey/' + path + '.html')

@survey.route('/using-paas-for')
def q1():
  # need to see if it exists
  return render_template( 'survey/using-paas-for.html')