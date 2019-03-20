import requests
import json
from database import DataBase

ACCESS_TOKEN = ''
USERS_LIST_SIZE = 100

with open('config.json') as f:
	data = json.load(f)
	ACCESS_TOKEN = data['vk']['ACCESS_TOKEN']
	USERS_LIST_SIZE = int(data['vk']['USERS_LIST_SIZE'])

print(ACCESS_TOKEN, USERS_LIST_SIZE)

db = DataBase()
users = db.get_top(USERS_LIST_SIZE)

# print('Бот стартовал.')
user = input('Введите пользователя.\n')
# print('Пользователь ' + user)


# Здесь мы формируем текст запроса
address_dude = 'https://api.vk.com/method/users.get?user_ids=' + user + \
	'&access_token=' + ACCESS_TOKEN + '&v=5.92'

# Здесь мы получаем айдишник пользователя
r = requests.get(address_dude)
if 'response' in r.json():
	user_id = r.json()['response'][0]['id']
else:
	print('Ошибка получения id')

# print( 'Получен id пользователя : ' + str(user_id) )


add_dude = 'https://api.vk.com/method/friends.add?user_id=' + str(user_id) + \
'&access_token=' + ACCESS_TOKEN + '&v=5.92'

r = requests.get(add_dude)
if 'response' in r.json():
	status = r.json()['response']
else:
	status = 0
	print('Ошибка добавления в друзья')
# print('Статус заявки : ' + str(status))

if status == 1 or status == 2 or status == 4:
	print('~~~~~~ ОГОНЬ ~~~~~~')
else:
	print('((( БРАТ НУ ТАК НЕ ПОЙДЕТ (((')
