import sqlite3

DATABASE_FILE_NAME = 'users.db'
CREATE_TABLES_SQL = '''
	CREATE TABLE IF NOT EXISTS users (
		id integer PRIMARY KEY AUTOINCREMENT,
		user_id text NOT NULL
	);
'''

class DataBase():
	def __init__(self):
		self.conn = self.create_connection()
		try:
			self.create_tables()
		except Exception as e:
			print(e)

	def create_connection(self):
		try:
			return sqlite3.connect(DATABASE_FILE_NAME)
			return True
		except Exception as e:
			print(e)
			return None
	def create_tables(self):
		try:
			c = self.conn.cursor()
			c.execute(CREATE_TABLES_SQL)
			return True
		except Exception as e:
			return None
	def add(self, user_id):
		c = self.conn.cursor()
		c.execute("INSERT INTO users (user_id) VALUES ('{}')".format(user_id))
		self.conn.commit()
	def get(self, user_id):
		c = self.conn.cursor()
		c.execute("SELECT * FROM users WHERE user_id = '{}'".format(user_id))
		return c.fetchone()
	def get_all(self):
		c = self.conn.cursor()
		c.execute("SELECT * FROM users")
		return c.fetchall()
	def get_top(self, amount=10):
		c = self.conn.cursor()
		c.execute("SELECT * FROM users")
		return c.fetchmany(amount)
	def get_page(self, limit=10, page=0):
		users = self.get_all()
		return users[limit * page: limit * (page + 1)]
	def __del__(self):
		self.conn.close()
