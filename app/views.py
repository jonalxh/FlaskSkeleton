# coding: utf-8
from app import app

import os
#flask related imports
from flask import render_template, request, jsonify, send_from_directory, send_file, session, redirect, g
import flask

@app.route('/index')
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/info', methods= ['POST','GET'])
def info():
	return jsonify({"status":"ok", "data":{"name":"app", "version": "0.0.1"}})

