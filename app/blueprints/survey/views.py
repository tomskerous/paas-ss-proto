from flask import (
  render_template,
  Blueprint,
  current_app)

import json
import os

survey = Blueprint('survey', __name__, url_prefix='/survey')