import time
import os

account = {"MuffinHavlop" : "Minhhieu1", "HoangMinhHieu" : "260707"}

while True:
	pick = input("Welcome to Doors11, please log in or sign up(log, sign): ")
	pick = pick.lower()
	if pick == "log":
		def login():
			global account
			os.system('cls')
			print("LOG-IN OPTION")
			print("*********************")
			user_name = input("Enter your username: ")
			if account.get(user_name) is not None:
				pass_word = input("Enter your password: ")
				if pass_word in account.values():
					for i in range(0, 4):
						loading_screen = "processing" + "."*i					
						os.system('cls')
						print(loading_screen, end="\r")
						time.sleep(1)
					print("Access granted!, enjoy hell!!!")
					exit()
				else:
					print("wrong password, try again")
			else:
				print("Username is not in the system")
		login()
	else:
		def sign_up():
			global account
			os.system('cls')
			print("SIGN-UP OPTION")
			print("*********************")
			user_name = input("Please Enter your username: ")
			password = input("please enter your password: ")
			re_enter_password = input("please re-enter your password: ")
			while password != re_enter_password:
				re_enter_password = input(("re-enter password is not sync with password, try again: "))
			else:
				for i in range(4):
					loading_screen = "processing" + "."*i				
					os.system('cls')
					print(loading_screen, end="\r")
					time.sleep(1)
				print(f"Account {user_name} has been successfully registered!!!")
				account.update({user_name : password})
		sign_up()
			
		