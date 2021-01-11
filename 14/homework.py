
#1
'''
def calc():
	dst=input('+ or - or / or * ?')
	if dst == "+": 
		x = lambda x, y: x + y
		print(x(int(input()),int(input())))
	elif dst == "-": 
		x = lambda x, y: x - y
		print(x(int(input()),int(input())))
	elif dst == "/": 
		x = lambda x, y: x / y
		print(x(int(input()),int(input())))
	elif dst == "*": 
		x = lambda x, y: x * y
		print(x(int(input()),int(input())))
calc()
'''

#2
'''
result = [(1, 6.06), (2, 6.23), (3, 7.03), (4, 6.88), (5, 6.43), (6, 6.57)]
print(result)
result.sort(key=lambda x:x[1],reverse=True)
print(result)
result.sort(key=lambda x:x[1])
print(result)
'''
#3
'''
a = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x : x % 2 == 0, a)))
print(list(filter(lambda x : x % 2 != 0, a)))
'''
#4
'''
from turtle import *
speed('fastest') 
rt(-90) 
angle = 40
def y(sz, level):    
    if level > 0: 
        colormode(255)  
        pencolor(0, 255//level, 0) 
        fd(sz) 
        rt(angle)  
        y(0.8 * sz, level-1)    
        pencolor(0, 255//level, 0) 
        lt( 2 * angle ) 
        y(0.8 * sz, level-1)   
        pencolor(0, 255//level, 0)
        rt(angle) 
        fd(-sz) 
y(int(input()), int(input()))
'''