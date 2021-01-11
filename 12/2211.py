'''
def f(n, q):
    if n == 1:
        return 1
    else:
        return f(n - 1,q) * q
n = int(input(": "))
q = int(input(": "))
print(f(n,q))
'''
'''
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(5)
'''
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
'''
def is_pali(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_pali(s[1:-1])
print(is_pali(input('what? ')))
'''
'''
def lth(s):
	if s == '':
		return 0
	else:
		return 1+lth(s[:-1])

print(lth(input('chto? ')))
'''

def a_to_b(a,b):
    if a == b:
        return a
    else:
        return a_to_b(a,b-1) + b
print(a_to_b(1,6))
