'''
f = open("test.txt",'a')
f.write("\nMy name Valera")
f.close
'''
'''
f = open("test.txt",'r')
print(f.read())
f.close
'''
'''
f = open("test.txt",'r')
if len(f.readlines()) < 2:
    print('Our file is too small.')
else:
    f.seek(0)
    print(f.readlines()[1])
f.close()
'''
'''
f = open("test.txt",'r')
f.readlines(2)
print(f.read())
f.close
'''
'''
#не правильно проставленна ссылка
bloknot = open("17.01.2021.txt",'a+t')
bloknot.seek(0)
if bloknot.readlines() == []:
    bloknot.write('num name age\n')
a = int(input('Count of new data(lines)\n'))
for i in range(a):
    name = input('Name: ')
    age = int(input('Age: '))
    bloknot.seek(0)
    if bloknot.readlines() == ['num name age\n']:
        bloknot.write(f'1 {name} {age}\n')
    else:
        bloknot.seek(0)
        i = int(bloknot.readlines()[-1][0])
        bloknot.write(f'{i+1} {name} {age}\n')
bloknot.close()
'''
'''
with open("test.txt", 'a+t', encoding='utf-8') as f:
    f.seek(0)
    text = f.readlines()
    size = len(text)
    if size == 0:
        f.write("Номер,Имя,Возраст\n")
    a = int(input("Введите кол-во людей: "))
    for i in range(a):
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        f.write(f"Номер: {size+i-1}, Имя: {name}, Возраст: {age}\n")
'''

ans = input('ADD:+, delet:-')

