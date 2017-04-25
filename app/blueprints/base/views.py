
from flask import (
  render_template,
  Blueprint,
  request,
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

@base.route('/create-account-submitted', methods=['GET', "POST"])
def create_account_submitted():
  if request.method == 'POST':
    email = request.form['email-addr']
    return render_template('create-account-submitted.html', user_email=email)
  else:
    return render_template('create-account-submitted.html')

@base.route('/create-account-completed', methods=['GET', "POST"])
def create_account_completed():
  if request.method == 'POST':
    email = request.form['email-addr']
    return render_template('create-account-completed.html', user_email=email)
  else:
    return render_template('create-account-completed.html')