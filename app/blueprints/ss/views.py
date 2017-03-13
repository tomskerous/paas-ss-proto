
from flask import (
  render_template,
  Blueprint,
  current_app)

import json
import os

ss = Blueprint('ss', __name__, url_prefix='/ss')

@ss.route('/')
@ss.route('/sign-in')
def sign_in():
  return render_template('sign_in.html')

@ss.route('/2fa')
def two_fa():
  return render_template('2fa.html')

@ss.route('/account')
def account():
  with open('app/data/org.json') as data_file:
      org = json.load( data_file )
  return render_template('account-page.html', org=org)

@ss.route('/request-account')
def request_account():
  return render_template('request_account.html')

@ss.route('/request-submitted')
def request_submitted():
  return render_template('request_submitted.html')

@ss.route('/spaces/create')
def create_space():
  return render_template('create_space.html')

@ss.route('/spaces/add-user')
def space_add_user():
  return render_template('space_add_user.html')

@ss.route('/services')
def services():
  return render_template('services.html')

@ss.route('/services/create')
def create_service():
  return render_template('create_service.html')

# eventually make this accept name of a <service>
# and get service data from json file
@ss.route('/spaces/')
@ss.route('/spaces/<space>')
def space(space=""):
  pathtodata = 'app/data/' + space + '/.json'
  space = {}
  if os.path.isfile( pathtodata ):
    with open('app/data/org.json') as data_file:
      space = json.load( data_file )

  return render_template('space.html', space=space)

@ss.route('/apps/')
@ss.route('/apps/<appname>')
def app_details(appname=""):
  pathtodata = 'app/data/' + appname + '/.json'
  paas_app = {'name': appname}
  if os.path.isfile( pathtodata ):
    with open('app/data/org.json') as data_file:
      paas_app = json.load( data_file )

  return render_template('app_details_page.html', paas_app=paas_app)
