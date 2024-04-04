import SocNet
import os

class MainApp:
	VERSION = 0.1
	SOCNET = SocNet.SocNet()
	USER_ID = -1
	def __init__(self):
		os.system('cls')
		while True:
			if self.USER_ID == -1:
				os.system('cls')
				print(f"SocNet v{self.VERSION} - Главное окно")
				print("Выберите команду:")
				print("1 - Авторизоваться\n2 - Зарегистрироваться")
				user_choice = input(": ")
				match int(user_choice):
					case 1:
						self.auth()
					case 2:
						self.signup()
			else:
				self.draw_list_friends()

	def auth(self):
		os.system('cls')
		print(f"SocNet v{self.VERSION} - Авторизация")
		user_login = input("Введите логин: ")
		user_pass = input("Введите пароль: ")
		auth_result = self.SOCNET.login(user_login, user_pass)
		if auth_result == -1:
			# os.system('cls')
			print("SocNet v0.1 - Ошибка авторизации")
			print("Такого пользователя не существует")
			input("Нажмите любую кнопку, чтобы продолжить...")
			return

		self.USER_ID = auth_result

	def draw_list_friends(self):
		os.system('cls')
		friend_list = []
		count = 1
		print(f"SocNet v{self.VERSION} - Список друзей")
		print("---------------------------")
		friend_list = self.SOCNET.get_list_friends(self.USER_ID)

		for friend in friend_list:
			print(f"{count}: {friend[1]}")
			print("---------------------------")
			count+=1
		print("1 - Открыть чат")
		print("2 - Добавить друга")
		print("3 - Удалить друга")
		print("4 - Выйти")
		user_choice = int(input(": "))
		match user_choice:
			case 1:
				chat_choice = int(input("Введите номер чата: "))
				self.draw_chat(friend_list[chat_choice-1])
			case 2:
				self.add_friend()
			case 3:
				chat_choice = int(input("Введите номер друга: "))
				self.delete_friend(friend_list[chat_choice-1])
			case 4:
				self.logout()

	def draw_chat(self, friend):
		while True:
			os.system('cls')
			print(f"SocNet v{self.VERSION} - Чат c {friend[1]}")
			print("---------------------------")
			for message in self.SOCNET.get_list_messages(self.USER_ID, friend[0]):
				print(message)
			print("---------------------------")
			print("1 - Написать сообщение")
			print("0 - Назад")
			user_choice = int(input(": "))
			match user_choice:
				case 1:
					self.send_message_to_friend(id_friend)
				case 0:
					break

	def send_message_to_friend(self, id_friend):
		message = input("Введите сообщение: ")
		self.SOCNET.send_message(self.USER_ID, id_friend, message)

	def add_friend(self):
		chat_choice = input("Введите имя друга: ")
		result = self.SOCNET.add_friend(self.USER_ID, chat_choice)
		input(f"{result}. Нажмите любую кнопку...")

	def delete_friend(self, friend):
		result = self.SOCNET.delete_friend(self.USER_ID, friend)
		input(f"{result}. Нажмите любую кнопку...")

	def logout(self):
		self.USER_ID = -1	

	def signup(self):
		os.system('cls')
		print("SocNet v0.1 - Регистрация")
		print("Введите логин:")
		user_login = input()
		print("Введите пароль:")
		user_pass = input()
		signup_result = self.SOCNET.create_user(user_login, user_pass)
		if signup_result == -1:
			# os.system('cls')
			print("SocNet v0.1 - Ошибка регистрации")
			print("Такой пользователь уже существует")
			input("Нажмите любую кнопку, чтобы продолжить...")
			return

		self.USER_ID = signup_result
if __name__ == '__main__':
	mainApp = MainApp()