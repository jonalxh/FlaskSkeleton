# coding: utf-8
from flask import Flask

#Uncomment the next three lines to avoid encoding conflicts
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

app = Flask(__name__)
app.config.from_pyfile('../config.py')

appname = 'My app name'

from app import views