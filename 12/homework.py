#nomer 1
'''def sum(a,b):
	if a == b:
		return a
	else:
		return sum(a,b-1) + b
print(sum(1,5))'''

#nomer 2
'''
def rec_sum(a_1, d, n):
    if n == 0:
        return 0
    return a_1 + rec_sum(a_1 + d, d, n-1)
print(rec_sum(5, 5, 2))
'''

#nomer 3

#nomer 4
#A
'''
def fn(n):
	if n==1:
		return 1
	else:
		print(n)
		return fn(n-1)
print(fn(int(input(':'))))
'''

#B
'''
def count(a, b):  
    if a<b:
        count(a, b - 1)
        print(b)
    elif a>b:
        print(a)
        count(a - 1, b)
    else:
        print(a)
a = int(input())
b = int(input())
count (a, b)
'''

#C
'''
def ackermann(m,n):
     if m == 0:
          return (n + 1)
     elif n == 0:
          return ackermann(m - 1, 1)
     else:
          return ackermann(m - 1, ackermann(m, n - 1))
 
m=int(input('m\n'))
n=int(input('n\n'))
print('A(m,n)= '+str(ackermann(m,n)))
'''
#D
'''
def two(num):
	if num == 1:
		return 'YES'
	elif num < 1:
		return 'NO'
	else:
		return two(num/2)
print(two(16))
'''

#E
'''
def summ(n):
	if n<10:
		return n 
	else:
		return n%10 + summ(n//10)
print(summ(132))
'''
#F
'''
def csh(n):
	if (n<10):
		return n
	else:
		print(n%10)
		return csh(n//10)
print(csh(12))
'''
#G
'''
def csh(k):
  if k < 10:
    return str(k)
  else:
    return csh(k//10) + ' ' + str(k%10)
print(csh(123))
'''
#H
'''
def rec(n, i):
        if n < 2:
            return 'NO'
        elif n == 2: 
            return 'YES'
        elif n % i == 0:
            return 'NO'
        elif i < n // 2: 
            return rec(n, i + 1)
        else:
        	return 'YES'
print(rec(13, 2))
'''
#I
'''
def recursion(n, k):
    if k>(n/2):
        return n
    if (n % k) == 0:
        print(k)
        return recursion(n // k, k)
    else:
        return recursion(n, k+1)
print(recursion(13, 2)) 
'''
#J
'''
def palindrome(word):
	if len(word) == 1 or (len(word) == 2 and word[0] == word[1]):
		print('true')
	else:
		if word[0] == word[len(word)-1]:
			return palindrome(word[1] + word[len(word)-2])
		else:
			print('false')

palindrome(input('что скажешь? '))
'''
#K
'''
def nch(a,n=1):
    if (n>a):
        print('None')
    else:
        print(n,end=' ')
        nch(a,n+2)
nch(31)
'''
#L
'''
def print_odds(order = 0, saved = []):
    number = int(input("Number: "))
    if number != 0:
        order += 1
        if order & 1:
            saved.append(number)
        print_odds(order, saved)
    else:
        for current in saved:
            print(current)
print_odds()
'''
#M
'''
def print_max(max = 0):
    number = int(input("Number: "))
    if number != 0:
    	if number > max:
    		max = number
    	print_max(max)
    else:
    	print(max)
print_max()
'''
#N
'''
def medium(sum = 0, len = 0):
	element = int(input('Number: '))
	if element != 0:
		sum += element
		len += 1
		medium(sum, len)
	else:
		print(sum / len)
medium()
'''
#O
'''
def second_max(max = 0, smax = 0):
    number = int(input("Number: "))
    if number != 0:
    	if number > max:
    		smax = max
    		max = number
    	second_max(max, smax)
    else:
    	print(f'Second max is {smax}')
second_max()
'''
#P
'''
def scd(maximum = 0, num_maximal = 0, element = -1):
	if element != 0:
		element = int(input('Number: '))
		if element > maximum:
			maximum, num_maximal = element, 1
		elif element == maximum:
			num_maximal += 1
		scd(maximum, num_maximal, element)
	else:
		print(num_maximal)
scd()
'''
#Q
'''
def odn(counter = 0):
    number = int(input("Number: "))
    if number != 0 and number == 1:
    	counter += 1
    elif number == 0:
    	snumber = int(input("Number: "))
    	if snumber != 0:
    		counter += 1
    	else:
    		print(counter)
    		return
    odn(counter)
odn()
'''
#R
'''
def rn(n, k = 1, i = 0):
	if n >= i:
		print(k)
		i += 1
		if i == k*(k + 1) // 2:
			k += 1
		rn(n, k, i)
	else:
		return	
rn(5)
'''
#S






#T
'''
def iuh(a,b):
	if a > b + 1:
		return 0
	if a == 0 or b == 0:
		return 1
	return iuh(a,b - 1) + iuh(a - 1, b - 1)
print(iuh(5,8))
'''
#U
'''
def rec(n,a = 0):
    if n == 0:
    	return a
    else:
    	return rec(n//10,10*a+n%10)
print(rec(123))
'''