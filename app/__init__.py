# coding: utf-8
from flask import Flask

#I've defined the next three lines to avoid encoding conflicts
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
app.config.from_pyfile('../config.py')

appname = 'Appname';


from app import views