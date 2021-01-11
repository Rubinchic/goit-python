#nomer 1
'''
Massiv = [1, 2, 3, 4, 5]
Summa = 0
 
def ma(x):  
    global Summa
    if x == len(Massiv):
        return    
    Summa  += Massiv[x]
    ma(x+1)
 
ma(0)
print('\nSumma = ', Summa)
'''

#nomer 2
'''
def reversedd(string):
    reversed_string = string[::-1]
    print(reversed_string)
 
reversedd('CAT')
'''

#nomer 3
'''
def factorial(chislo):
	sdf=1
	if chislo > 0: 
		for i in range(1, chislo+1):
			sdf = sdf*i
			print(i, sdf)
	else:
		print('eror')
	print(sdf)

factorial(int(input(': ')))
'''

#nomer 4
'''
asdfg=int(input('skiki?: '))
old_list=[]
new_list=[]
ciferka=0
while ciferka < asdfg:
	old_list.append(input('chto hochesh dobavit?: '))
	ciferka+=1

def delpot(old_list):
	global new_list
	for i in old_list:
		if i not in new_list:
			new_list.append(i)
			print(new_list)
delpot(old_list)
'''

#nomer 5
#a
'''
st = zip(
    [1000,900,500,400,100,90,50,40,10,9,5,4,1],
    ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
)
 
def rr(num):
    if num <= 0 or num >= 4000 or int(num) != num:
        raise ValueError('1 - 3999')
    result = []
    for d, r in st:
        while num >= d:
            result.append(r)
            num -= d
    return ''.join(result)

print(rr(int(input(': '))))
'''

#b

#nomer 6
'''
a = input('a: ')
b = input('b: ')
c = input('c: ')
a = float(a)
b = float(b)
c = float(c)
discriminant = b**2 - 4*a*c
print('Дискриминант = ' + str(discriminant))
if discriminant < 0:
    print('Корней нет')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))
'''