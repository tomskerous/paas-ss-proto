
from flask import (
  render_template,
  Blueprint,
  current_app)

base = Blueprint('base', __name__)

@base.route('/')
@base.route('/index')
def index():
  return render_template('index.html')

@base.route('/product-page')
def product_page():
  return render_template('paas_product_page.html')

@base.route('/docs.html')
def proto_docs():
  return render_template('docs.html')

