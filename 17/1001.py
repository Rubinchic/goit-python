#factorial
'''
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

print(fac(int(input("number: "))))
'''

'''
def subsetsRecur(current,sset):
	if sset:
		return subsetsRecur(current, sset[1:])+subsetsRecur(current+[sset[0]],sset[1:])
return [current]
print(subsetsRecur([][2,3,4]))
'''

'''
class figura:
	def __init__(self, tittle):
		self.tittle = tittle

class pr(figura):
	def __init__(self, a, b):
		self.a = a
		self.b = b
		super().__init__("rec")

	def per(self):
		return (self.a + self.b)*2

	def ar(self):
		return self.a * self.b

class tr(figura):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		super().__init__('trian')

	def per(self):
		return self.a + self.b + self.c

	def ar(self):
		return

pr = pr(5,5)
tr = tr(3,3,6)
'''


class Matrix:
	def __init__(self, mas, ls):
		self.mas = mas
		self.ls = ls
		