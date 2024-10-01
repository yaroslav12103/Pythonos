import os
from progress.bar import ChargingBar as Bar
from time import sleep
import getpass
from UIKit import UIDevice
import random
#import colorama
#from colorama import Fore, Back, Style


DEVICE_NAME = str(UIDevice.currentDevice.name)

data_path = 'data/main_data.txt'
Version = 'PyOs v1.8'


activeapp = 'Home'
system = False
active = True

#def install(appstorecommand):
#	global RAM
#	clear()
#	b = 0
#	try:
#		while apps[b] != appstorecommand:
#			b += 1
#		if appsi[b] == ‘False’:
#			appsi[b] = ‘True’
#			fl = Bar(f’Installing {appstorecommand}...’, max=10)
#			RAM -= 56
#			for i in range(20):
#				sleep(0.1)
#				fl.next()
#			fl.finish()
#			sleep(1)
#			print(‘Sucsses!’)
#			exit = input(‘’’-———
#Enter to continue’’’)
#			clear()
#		elif appsi[b] == ‘True’:
#			answer = input(f’Do you want to delete «{appstorecommand}»?(Y/n)’)
#			if answer == ‘Y’:
#				RAM += 56
#				appsi[b] = ‘False’
#				fl = Bar(f’Uninstalling {appstorecommand}...’, max=20)
#				for i in range(5):
#					sleep(0.1)
#					fl.next()
#					sleep(0.6)
#					fl.next()
#					sleep(1)
#					fl.next
#				fl.finish()
#				sleep(1)
#				print(‘Sucsses!’)
#				exit = input(‘’’-———
#Enter to continue’’’)
#				clear()
#	except:
#		print(‘not found’)

#def appstore():
#	global activeapp, RAM
#	while activeapp == ‘appstore’:
#		print(‘-———‘)
#		print(‘App Store’)
#		print(‘-———‘)
#		l = len(apps)
#		for i in range(l):
#			print(f’{apps[i]} - {appsi[i]}’)
#		appstorecommand = input(‘@‘)
#		if appstorecommand == ‘home’:
#			clear()
#			activeapp = ‘Home’
#		elif appstorecommand == ‘blocknote’:
#			if appsi[1] == ‘False’:
#				os.mkdir(‘blocknote’)
#				install(appstorecommand)
#			elif appsi[1] == ‘True’:
#				for filename in os.listdir(‘blocknote’):
#					file_path = os.path.join(‘blocknote/‘, filename)
#					if os.path.isfile(file_path):
#						os.remove(file_path)
#				os.rmdir(‘blocknote’)
#				install(appstorecommand)
#		else:
#			install(appstorecommand)

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

def blocknote():
	global activeapp
	while activeapp == 'blocknote':
		print('----------')
		print('Blocknote')
		print('-------------')
		files = os.listdir('./blocknote')
		for item in files:
			print(item)
		print('-------------')
		note = input('filename:(or type create to create new file)')
		if note != 'home' and note != 'create':
			try:
				with open(f'./blocknote/{note}', 'r+') as file:
					clear()
					print(note)
					text = file.read()
					print('***********************')
					print(text)
					print('***********************')
					task = input('add,clear,back,remove,rename or str_edit:')
					#add, editstring, clear, remove, back, create
					if task == 'add':
						wta = input('type your note:')
						file.write(wta + '\n')
						clear()
						print(note)
						file.close()
						with open(f'./blocknote/{note}', 'r') as file:
							text = file.read()
							print('***********************')
							print(text)
							print('***********************')
							file.close()
							exit = input('''----------
Enter to exit''')
							clear()
					elif task == 'clear':
						with open(f'./blocknote/{note}', 'w') as file:
							file.write('')
						clear()
					elif task == 'back':
						clear()
					elif task == 'remove':
						os.remove(f'./blocknote/{note}')
						clear()
					elif task == 'rename':
						new_name = input('Enter new file name:')
						os.rename(f'blocknote/{note}', f'blocknote/{new_name}')
						clear()
						print('Succes!')
						print(f'{note} -> {new_name}')
						exit = input('''----------
Enter to exit''')
						clear()
					elif task == 'str_edit':
						clear()
						with open(f'./blocknote/{note}', 'r') as file:
							lines = file.readlines()
							print('***********************')
							num = 0
							for item in lines:
								print(f'{num}.{item}')
								num += 1
							print('***********************')
							file.close()
							num = int(input('line number:'))
							change = input('note:')
							lines[num] = change
						file.close
						with open(f'./blocknote/{note}', 'w') as file:
							file.writelines(lines)
						file.close()
						clear()
						with open(f'./blocknote/{note}', 'r') as file:
							text = file.read()
							print('***********************')
							print(text)
							print('***********************')
							file.close()		
							exit = input('''----------
Enter to exit''')
							clear()
					else:
						clear()
						print('invalid task')
			except:
				clear()
				print('invalid file name')
		elif note == 'create':
			filename = input('name:')
			file = open(f'./blocknote/{filename}', 'a')
			file.close
			clear()
		else:
			clear()
			activeapp = 'Home'


def clear():
    print("\033c", end="")


print('starting os...')
main_data = open(data_path, 'r')
data_list = [line.strip() for line in main_data]
main_data.close()
#Приложения---------------------------
app = dict(google=data_list[3], blocknote=data_list[4])
#-------------------------------------
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
	elif command == 'blocknote':
		if appsi[1] == 'True':
			activeapp = 'blocknote'
			clear()
			blocknote()
		else:
			clear()
			print('blocknote is not installed.')
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
			lines[4] = appsi[1]
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
		print(Version)
		print(f'Free RAM:{RAM}/500mb')
		print('')
		print('''Changelog:
PyOs v1.8
-bugfixes
-new app 'blocknote'
''')
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
		


		
