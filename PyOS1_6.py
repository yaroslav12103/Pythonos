from progress.bar import ChargingBar as Bar
from time import sleep
import getpass
from UIKit import UIDevice

#import requests
#from bs4 import BeautifulSoup
data_path = 'data/main_data.txt'
DEVICE_NAME = str(UIDevice.currentDevice.name)
activeapp = 'Home'
system = False
active = True

def appstore():
	global activeapp, RAM
	while activeapp == 'appstore':
		print('----------')
		print('App Store')
		print('----------')
		print(f'google {appsi[0]}')
		appstorecommand = input('@')
		if appstorecommand == 'google' and appsi[0] == 'False':
			appsi[0] = 'True'
			fl = Bar("Installing google...", max=10)
			RAM -= 32
			for i in range(20):
			    sleep(0.1)
			    fl.next()
			fl.finish()
			sleep(1)
			clear()
			print('Sucsses!')
		elif appstorecommand == 'google' and appsi[0] == 'True':
			answer = input('Do you want to delete "google"?(Y/n)')
			if answer == 'Y':
				RAM += 32
				appsi[0] = 'False'
				fl = Bar("Uninstalling google...", max=15)
				for i in range(5):
					sleep(0.1)
					fl.next()
					sleep(0.6)
					fl.next()
					sleep(1)
					fl.next
				fl.finish()
				sleep(1)
				clear()
				print('Sucsses!')
		elif appstorecommand == 'home':
			clear()
			activeapp = 'Home'
		else:
			clear()
			print('not found')
			
def google():
	global activeapp
	while activeapp == 'google':
		print('----------')
		print('Google')
		print('----------')
		from webbrowser import open
		a = input('type something: ')
		if a != 'home':
			url = f'https://www.google.ru/search?q={a}'
			url = url.replace(" ", "+")
			open(url)
		else:
			clear()
			activeapp = 'Home'

def clear():
    print("\033c", end="")


print('starting os...')
main_data = open(data_path, 'r')
data_list = [line.strip() for line in main_data]
main_data.close()
app = dict(google=data_list[3])
apps = list(app.keys())
appsi = list(app.values())
account = data_list[0]
RAM = data_list[2]
RAM = int(RAM)
fl = Bar("loading files", max=20)
for i in range(20):
    sleep(0.1)
    fl.next()
fl.finish()
st = Bar("starting", max=10)
for i in range(20):
    sleep(0.1)
    st.next()
st.finish()
clear()



while system != True:
	if account == 'True':
		password = data_list[1]
		print('----------Hi!----------')
		user_pass = getpass.getpass("Enter password: ")
		if user_pass == password:
			system = True
			clear()
		else:
			clear()
			print('Incorrect')
	else:
		print('--Create an account--')
		password = input('Password:')
		passcheck = input('Confirm password:')
		if password == passcheck:
			clear()
			print('Success!')
			print(f'Password: {password}')
			system = True
			account = True
		else:
			clear()
			print('Passwords do not match!')
			print('Try again.')
while active == True:
	print('----------HOME----------')
	command = input(f'[{DEVICE_NAME}]$')
	if command == 'google':
		if appsi[0] == 'True':
			activeapp = 'google'
			clear()
			google()
		else:
			clear()
			print('google is not installed.')
	elif command == 'appstore':
		activeapp = 'appstore'
		clear()
		appstore()
	elif command == 'end':
		active = False
		with open(data_path, 'r') as file:
			# Чтение всех строк из файла
			lines = file.readlines()
			account = str(account)
			RAM = str(RAM)
			lines[0] = account
			lines[1] = password
			lines[2] = RAM
			lines[3] = appsi[0]
			elements = (len(lines))
			for i in range(elements):
				lines[i] += '\n'
			# Записываем измененные строки в файл
			with open(data_path, 'w') as file:
				file.writelines(lines)
			st = Bar("saving...", max=10)
			for i in range(10):
				sleep(0.1)
				st.next()
				sleep(1)
				st.next()
			st.finish()
			print('end')
			sleep(1.5)
			clear()
	elif command == '!end':
		answer = input('Are you sure you want to exit without saving?(Y/n)')
		if answer == 'Y':
			active = False
		else:
			clear()
	elif command == 'help':
		clear()
		print('''Command list:
"app_name" - open an app
help - command list
appstore  - open App Store
end - save and exit
!end - exit without saving
sys.info - information about system
sys.logout - log out of your account(all data will be deleted)
''')
		exit = input('''----------
Enter to exit''')
		clear()
	elif command == 'sys.info':
		clear()
		print(DEVICE_NAME)
		print('PyOs v1.6')
		print(f'Free RAM:{RAM}/500mb')
		exit = input('''----------
Enter to exit''')
		clear()
	elif command == 'sys.logout':
		account = False
		clear()
		active = False
		with open(data_path, 'r') as file:
			# Чтение всех строк из файла
			lines = file.readlines()
			account = str(account)
			lines[0] = account
			lines[1] = ''
			lines[2] = '500'
			lines[3] = 'False'
			elements = (len(lines))
			for i in range(elements):
				lines[i] += '\n'
			# Записываем измененные строки в файл
			with open(data_path, 'w') as file:
				file.writelines(lines)
			print('end')
			sleep(1.5)
			clear()
	elif command == 'sys.check':
		clear()
		elements = (len(data_list))
		for i in range(elements):
			print(data_list[i])
		exit = input('''----------
Enter to exit''')
		clear()
	else:
		clear()
		print('command not found.')


		
