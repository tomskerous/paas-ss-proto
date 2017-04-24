
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

@base.route('/support')
def support():
  return render_template('support.html')

@base.route('/paas-for-designers')
def paas_for_designers():
  return render_template('paas-for-designers.html')
