class SocNet:
	ID_LAST_USER = 1
	MESSAGES = []
	USERS = [[1, "admin", "password"]]
	FRIENDS = [[1, []]]

	def __init__(self):
		pass
		
	def login(self, login, password):
		# Метод авторизации с помощью логина и пароля
		# param login - любая строка
		# param password - любая строка
		# return - id пользателя
		for user in self.USERS:
			if user[1] == login and user[2] == password:
				return user[0]
		return -1

	def send_message(self, text, id_friend):
		# todo: finish method
		return "success"

	def add_friend(self, name_friend):
		# todo: finish method
		return "success"

	def delete_friend(self, num_friend):
		# todo: finish method
		return "success"

	def find_user_by_name(self, name):
		# todo: finish method
		return 1

	def create_user(self, login, password):
		# Метод, создающий пользователя
		# param login - любая строка
		# param password - любая строка
		# return - результат операции
		for user in self.USERS:
			if user[1] == login:
				return "failed"
		self.ID_LAST_USER += 1
		self.USERS.append([self.ID_LAST_USER, login, password])
		self.FRIENDS.append([self.ID_LAST_USER, []])
		return "success"