from flask import Flask
from flask import request
from flask import jsonify

from database import DataBase

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/add', methods=['POST'])
def add():
	data = request.get_json()
	db = DataBase()
	user_name = data['link'].split('/')[-1]
	db.add(user_name)
	return jsonify({'success': True})

@app.route('/get', methods=['GET'])
def get():
	try:
		limit = int(request.args.get('limit'))
		page = int(request.args.get('page'))
	except:
		page = None
		limit = None
	if page is None:
		page = 0
	if limit is None:
		limit = 10
	db = DataBase()
	users = db.get_page(limit, page)
	return jsonify(users)

app.run(host='0.0.0.0', port=80)