#!venv/bin/python
from app import app

if __name__ == '__main__':

	app.run(host='0.0.0.0', threaded=True, debug=True, port=5001)