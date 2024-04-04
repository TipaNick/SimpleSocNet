class SocNet:
	__ID_LAST_USER = 10

	__MESSAGES = [[1, 2, "Test text"],
				[2, 1, "Test text 2"]]

	__USERS = [[1, "admin", "password"],
			[2, "test", "test"],
			[3, "friend1", "friend1"],
			[4, "friend_to_del", "pass"]]

	__FRIENDS = [[1, [2, 3]], [2, [1]], [3,[1]], [4,[]]]

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

	def add_friend(self, id_user, friend_name):
		# Метод, добавляющий в друзья
		# param id_user - любое число
		# param friend_name - любая строка
		# return - статус операции 
		user_friends_list = None
		friend_friends_list = None

		friend_id = self.find_user_by_name(friend_name)
		if friend_id == -1:
			return "User is not existed"

		for friend in self.__FRIENDS:
			if friend[0] == id_user:
				user_friends_list = friend[1]
			if friend[0] == friend_id:
				friend_friends_list = friend[1]

		if friend_id in user_friends_list:
			return "User already in friend list"

		user_friends_list.append(friend_id)
		friend_friends_list.append(id_user)

		return "Success"

	def delete_friend(self, id_user, friend_to_delete):
		# Метод, удаляющий из друзей
		# param id_user - любое число
		# param friend_to_delete - любой пользователь(массив [id, "name"])
		# return - статус операции 
		user_friends_list = None
		friend_friends_list = None
		for friend in self.__FRIENDS:
			if friend[0] == id_user:
				user_friends_list = friend[1]
			if friend[0] == friend_to_delete[0]:
				friend_friends_list = friend[1]

		if friend_to_delete[0] not in user_friends_list:
			return "User is not in friend list"

		user_friends_list.remove(friend_to_delete[0])
		friend_friends_list.remove(id_user)

		return "Success"

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

	def get_list_messages(self, id_user, friend):
		# Метод, собирающий сообщения
		# param id_user - любое число
		# param friend - любой пользователь(массив [id, "name"])
		# return - массив строк
		list_messages = []
		for message in self.__MESSAGES:
			if message[0] == id_user and message[1] == friend[0]:
				list_messages.append(f"Вы: {message[2]}")
			if message[1] == id_user and message[0] == friend[0]:
				list_messages.append(f"{friend[1]}: {message[2]}")

		return list_messages