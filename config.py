# coding: utf-8
import os
from datetime import timedelta

#basedir = os.path.abspath(os.path.dirname(__file__))

SESSION_COOKIE_NAME = 'session'
CSRF_ENABLED = True
SECRET_KEY = 'secret_string'
TEMPLATES_AUTO_RELOAD = True

#Babel configuration
BABEL_DEFAULT_LOCALE = 'es'
BABEL_DEFAULT_TIMEZONE = 'GMT/UTC - 05:00'