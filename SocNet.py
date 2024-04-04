class SocNet:
	__ID_LAST_USER = 10
	__MESSAGES = [[1, 2, "Test text"],
				[2, 1, "Test text 2"]]
	__USERS = [[1, "admin", "password"],
			[2, "test", "test"],
			[3, "friend1", "friend1"]]
	__FRIENDS = [[1, [2, 3]], [2, [1]], [3,[]]]

	def __init__(self):
		pass
		
	def login(self, login, password):
		# Метод авторизации с помощью логина и пароля
		# param login - любая строка
		# param password - любая строка
		# return - id пользователя
		for user in self.__USERS:
			if user[1] == login and user[2] == password:
				return user[0]
		return -1

	def send_message(self, id_user, id_friend, text):
		# Метод, добавляющий сообщение
		# param id_user - любое число
		# param id_friend - любое число
		# param text - любая строка
		# return - результат операции 
		self.__MESSAGES.append([id_user, id_friend, text])
		return "success"

	def add_friend(self, id_user, name_friend):
		# Метод, добавляющий в друзья
		# param id_user - любое число
		# param name_friend - любая строка
		# return - статус операции 
		friend_id = self.find_user_by_name(name_friend)
		if friend_id == -1:
			return "User is not existed"
		for friend in self.__FRIENDS:
			if friend[0] == id_user:
				if friend_id in friend[1]:
					return "User already in friend list"
				else:
					friend[1].append(friend_id)
					return "success"

	def delete_friend(self, id_user, num_friend):
		# todo: finish method
		return "success"

	def find_user_by_name(self, name):
		# Метод, возвращающий id по имени
		# param name - любая строка
		# return - id пользователя
		for user in self.__USERS:
			if user[1] == name:
				return user[0]
		return -1

	def create_user(self, login, password):
		# Метод, создающий пользователя
		# param login - любая строка
		# param password - любая строка
		# return - результат операции
		for user in self.__USERS:
			if user[1] == login:
				return -1
		self.__ID_LAST_USER += 1
		self.__USERS.append([self.__ID_LAST_USER, login, password])
		self.__FRIENDS.append([self.__ID_LAST_USER, []])
		return self.__ID_LAST_USER

	def get_list_friends(self, id_user):
		# Метод, выводящий список друзей
		# param id_user - любое число
		# return - массив друзей
		list_id_friends = None
		friends_list = []
		for friends in self.__FRIENDS:
			if friends[0] == id_user:
				list_id_friends = friends[1]
				break
		for friend in list_id_friends:
			for user in self.__USERS:
				if friend == user[0]:
					friends_list.append([user[0], user[1]])
					break
		return friends_list

	def get_list_messages(self, id_user, id_friend):
		return ["Вы: Test text", "test: Test text 2"]