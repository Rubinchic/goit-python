import math as m

#print('введи две стороны треугольника чтобы узнать какая будет у него гипотенуза!')

#a=int(input("первая сторона: "))
#b=int(input("вторая сторона: "))
#c=m.sqrt(a**2+b**2)
#print(f'гипотенуза такого треугольника будет равняться {c}')

#___________________________________________________________________________

#a=int(input("введи любое число: "))

#print(f"The next numder for the number {a} is {a+1}")
#print(f"The previous number for the number {a} is {a-1}")

#___________________________________________________________________

#a=int(input("введи любое количества минут чтобы узнать сколько это секунд: "))

#print(f"{a} минут это {a*60} секунд")

#_________________________________________________

#a=int(input("введи секунды: "))
#print(f'{a} секунд это {a//60} минут и {a%60} секунд')

#___________________________________________________

#sec = int(input('enter the number of seconds: '))
#sec1 = sec
#mins = sec//60
#sec = sec - mins*60
#hrs = mins//60
#mins = mins - hrs*60
#days = hrs//24
#hrs = hrs - days*24

#print(f'{sec1} seconds is:')
#print(f'{days} days;')
#print(f'{hrs} hours;')
#print(f'{mins} minutes;')
#print(f'{sec} seconds.')

#_____________________________________________________

#students=int(input("сколько учеников ели яблоки? "))
#apples=int(input('сколько яблок было в корзинке? '))

#eat=apples//students
#corzinka=students%apples

#print(f'каждый ученик ел по {eat} яблок')
#print(f'в корзинке осталось {corzinka} яблок')

#_______________________________________________________

#print('Длина Московской кольцевой автомобильной дороги — 109 километров. Байкер Вася стартует с нулевого километра МКАД и едет со скоростью...')
#speed=int(input('какая скорость? '))
#print(f' ...и едет со скоростью {speed} километров в час.')

#time=int(input('сколько он ехал? '))
#print(f'На какой отметке он остановится через {time} часов?')

#s=speed*time
#o=s%109

#print(f'он остановиться на отметке {o} километров')

#_____________________________________________________________

#a=int(input('введи число: '))
#print(f'{a%10}')

#_________________________________________________________

#wins = int(input('enter a number of wins: '))
#draws = int(input('enter a number of draws: '))
#looses = int(input('enter a number of looses: '))

#score = wins*3 + draws

#print(f'score: {score}')

#______________________________________________________

#age=int(input('сколько вам лет? '))
#gender=input('gender: ')

#if age>=18 and gender=='w':
#	print('welcome')
#	print('free')
#elif age>=18 and gender=='m':
#	print('welcome, price: 100 uah')
#else: 	
#	print('deny')

#____________________________________________

#a=int(input('first number: '))
#b=int(input('second number: '))
#c=input(' -, +, /, *, //, %, ** ')

#if c=='-':
#	print(f'{a-b}')
#elif c=='+':
#	print(f'{a+b}')
#elif c=='/':
#	print(f'{a/b}')
#elif c=='*':
#	print(f'{a*b}')	
#elif c=='//':
#	print(f'{a//b}')
#elif c=='%':
#	print(f'{a%b}')
#elif c=='**':
#	print(f'{a**b}')
#else:
#	print('EROR')

#____________________________________________________

#a=int(input('number: '))

#f=a%3
#b=a%5

#if f==0 and b==0:
#	print('FizzBuzz')
#elif f==0:
#	print('Fizz')
#elif b==0:
#	print('Buzz')
#else:
#	print(f'{a}')

#_______________________________________________________

#print('  *  ')
#print(' ***  ')
#print('*****')
#print(' *** ')
#print('  *  ')

#print('  *\n ***\n*****\n ***\n  *')

#________________________________________________________

