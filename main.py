import SocNet
import os

class MainApp:
	SOCNET = SocNet.SocNet()
	USER_ID = -1
	def __init__(self):
		os.system('cls')
		while True:
			if self.USER_ID == -1:
				# os.system('cls')
				print("SocNet v0.1 - Главное окно")
				print("Выберите команду:")
				print("1 - Авторизоваться\n2 - Зарегистрироваться")
				user_choice = input()
				match int(user_choice):
					case 1:
						self.auth()
					case 2:
						self.signup()

	def auth(self):
		# os.system('cls')
		print("SocNet v0.1 - Авторизация")
		print("Введите логин:")
		user_login = input()
		print("Введите пароль:")
		user_pass = input()
		auth_result = self.SOCNET.login(user_login, user_pass)
		if auth_result == -1:
			# os.system('cls')
			print("SocNet v0.1 - Ошибка авторизации")
			print("Такого пользователя не существует")
			input("Нажмите любую кнопку, чтобы продолжить...")
			return

		self.USER_ID = auth_result

	def signup(self):
		# os.system('cls')
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