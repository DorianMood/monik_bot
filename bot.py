import requests
import json
from database import DataBase
import time

ERRORS = {
	'CAPTCHA': 14,
	'INVALID_USER': 113
}
MINUTE = 60

class Bot:
	def __init__(self):
		with open('config.json') as f:
			data = json.load(f)
			self.ACCESS_TOKEN = data['vk']['ACCESS_TOKEN']
			self.USERS_LIST_SIZE = int(data['vk']['USERS_LIST_SIZE'])
		print('token: {}'.format(self.ACCESS_TOKEN))
		print('size: {}'.format(self.USERS_LIST_SIZE))
		self.init_DB()
	def init_DB(self):
		self.db = DataBase()
	def get_all_users(self):
		return self.db.get_all()
	def add_all_with_timer(self, timer):
		users = self.get_all_users()
		for user in users:
			user_id = user[0]
			if '/' in user_id:
				user_id = user_id.split('/')[-1]
				print(user_id)
			self.add(user_id)
			time.sleep(timer)
		return True
	def next_user(self):
		top_users = self.db.get_top()
		return top_users[0]
	def add_next(self):
		user = self.next_user()
		return self.add(user)
	def add(self, user):
		# Здесь мы формируем текст запроса
		address_dude = 'https://api.vk.com/method/users.get?user_ids=' + user + \
			'&access_token=' + self.ACCESS_TOKEN + '&v=5.92'

		# Здесь мы получаем айдишник пользователя
		r = requests.get(address_dude)
		if 'response' in r.json():
			user_id = r.json()['response'][0]['id']
		else:
			print('Ошибка получения id')
			error_code = r.json()['error']['error_code']
			if error_code == ERRORS['INVALID_USER']:
				print('User not exists')
			return False

		add_dude = 'https://api.vk.com/method/friends.add?user_id=' + str(user_id) + \
		'&access_token=' + self.ACCESS_TOKEN + '&v=5.92'

		r = requests.get(add_dude)
		if 'response' in r.json():
			status = r.json()['response']
		else:
			status = 0
			print('Ошибка добавления в друзья')
			error_code = r.json()['error']['error_code']
		if status == 1 or status == 2 or status == 4:
			print('~~~~~~ ОГОНЬ ~~~~~~')
		else:
			if error_code == 14:
				print('Captcha')
			print('((( БРАТ НУ ТАК НЕ ПОЙДЕТ (((')
			return False
		return True


bot = Bot()
#bot.add(user=input('Input user: '))
bot.add_all_with_timer(30 * MINUTE)
