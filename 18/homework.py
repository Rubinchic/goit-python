import os
f = open('allnames_f.txt','w')
f.close
start = 1
do = int(input('1:Создать файл\n2:Записать строку в определенный файл\n3:Записать строку во все существующие файлы\n4:Записать несколько строк в определенный файл\n5:Записать несколько строк во все существующие файлы\n6:Очистить определенный файл\n7:закончить работу\n8:Вывести все названия текстовых файлов\n'))
while start != 0:
	if do == 1:
		name = input('Название файла: ')
		f = open(f"{name}.txt",'a')
		name1 = f.name
		f.close
		f = open('allnames_f.txt','a')
		f.write(f'\n{name1}')
		f.close
		do = int(input('1:Создать файл\n2:Записать строку в определенный файл\n3:Записать строку во все существующие файлы\n4:Записать несколько строк в определенный файл\n5:Записать несколько строк во все существующие файлы\n6:Очистить определенный файл\n7:закончить работу\n8:Вывести все названия текстовых файлов\n'))
	elif do == 2:
		name = input('Введите название файла: ')
		st = input('Что вы хотите ввести: ')
		f = open(f'{name}.txt','a')
		f.write(f'\n{st}')
		name1 = f.name
		f.close
		f = open('allnames_f.txt','a')
		f.write(f'\n{name1}')
		f.close
		do = int(input('1:Создать файл\n2:Записать строку в определенный файл\n3:Записать строку во все существующие файлы\n4:Записать несколько строк в определенный файл\n5:Записать несколько строк во все существующие файлы\n6:Очистить определенный файл\n7:закончить работу\n8:Вывести все названия текстовых файлов\n'))
	elif do == 3:
	elif do == 4:
		name = input('Название файла: ')
		f = open(f'{name}.txt','a')
		name1 = f.name
		col = int(input('Сколько строк? '))
		for i in range(0, col):
			st = input('Что вы хотите ввести: ')
			f.write(f'\n{st}')
		f.close
		f = open('allnames_f.txt','a')
		f.write(f'\n{name1}')
		f.close
		do = int(input('1:Создать файл\n2:Записать строку в определенный файл\n3:Записать строку во все существующие файлы\n4:Записать несколько строк в определенный файл\n5:Записать несколько строк во все существующие файлы\n6:Очистить определенный файл\n7:закончить работу\n8:Вывести все названия текстовых файлов\n'))
	elif do == 6:
		name = input('Название файла: ')
		os.remove(f'{name}.txt')
		f = open(f'{name}.txt','w')
		f.close
		do = int(input('1:Создать файл\n2:Записать строку в определенный файл\n3:Записать строку во все существующие файлы\n4:Записать несколько строк в определенный файл\n5:Записать несколько строк во все существующие файлы\n6:Очистить определенный файл\n7:закончить работу\n8:Вывести все названия текстовых файлов\n'))
	elif do == 7:
		start = 0
	elif do == 8:
		f = open('allnames_f.txt','r')
		print(f.read())
		f.close
		do = int(input('1:Создать файл\n2:Записать строку в определенный файл\n3:Записать строку во все существующие файлы\n4:Записать несколько строк в определенный файл\n5:Записать несколько строк во все существующие файлы\n6:Очистить определенный файл\n7:закончить работу\n8:Вывести все названия текстовых файлов\n'))
	else:
		print('Eror!')
		do = int(input('1:Создать файл\n2:Записать строку в определенный файл\n3:Записать строку во все существующие файлы\n4:Записать несколько строк в определенный файл\n5:Записать несколько строк во все существующие файлы\n6:Очистить определенный файл\n7:закончить работу\n8:Вывести все названия текстовых файлов\n'))



