from database import DataBase


fileName = input('Введите путь к файлу с IDs:\n')

ids = []
with open(fileName, 'r') as f:
	ids = f.read().split()
	db = DataBase()
	for i in range(len(ids)):
		print('{} / {}'.format(i, len(ids)), end='\r')
		db.add(ids[i])