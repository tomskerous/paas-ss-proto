# -*- coding: utf-8 -*-
"""
Application configuration
"""

import os

# get settings from environment, or credstash if running in AWS
env = os.environ

DEBUG = bool(env.get('DEBUG', True))

SECRET_KEY = 'zSt\x03\x82\x81\xe8\x8a\xea\xb5\x8a\xa2klF\xfa\t\xee\xe2l\x80\x9di\xe2'

# XXX Don't change the following settings unless necessary

# Skips concatenation of bundles if True, which breaks everything
ASSETS_DEBUG = False

ASSETS_LOAD_PATH = [
    'app/static',
    'app/templates']
