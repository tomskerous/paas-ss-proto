from flask import (
  render_template,
  Blueprint,
  current_app)

import json
import os

docs = Blueprint('docs', __name__, url_prefix='/docs')