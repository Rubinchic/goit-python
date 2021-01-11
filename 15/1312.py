'''
class Vehicle:
	def __init__ (self, color, doors, tires):
		#constructor
		self.color = color
		self.doors = doors
		self.tires = tires

	def brake(self):
		return'Braking'

	def drive(self):
		return 'I`m driving!'
v = Vehicle("red",4,4)
print(v.brake())
print(v.color)
'''
'''
class Pp:
    def __init__(self, z, c):
        self.z = z
        self.c = c

    def prm(self):
        return (self.z + self.c) * 2

    def plm(self):
        return self.z * self.c

ppp = Pp(int(input(": ")), int(input(": ")))
print(ppp.prm())
print(ppp.plm())
'''
'''
from math import pi
class Circle:
	def __init__(self, r):
		self.r = r
	def s (self):
		return self.r ** 2 * pi
	def dl (self):
		return self.r *2 * pi
	def __gt__ (self,other):
		return self.r > other.r
	def __eq__ (self,other):
		return self.r ++ other.r
a = Circle(6)
b = Circle(6)
print(a>b,a<b,a!=b)
'''
'''
class Figura:
    def init(self,nazva):
        self.nazva = nazva
    def who(self):
        print(self.nazva)
    def str(self):
        return f"figure is a {self.nazva}"
class Pryamoygolnik(Figura):

    def init(self,a,b):
        super().init('Pryamoygolnik')
        self.a = a
        self.b = b
    
    def per(self):
        return (self.a + self.b)*2

    def str(self):
        return f'its {self.nazva} with {self.a} and {self.b}'


class Threeangle(Figura):

    def init(self,a,b,c):
        super().init('Threeangle')
        self.a = a
        self.b = b
        self.c = c
    
    def per(self):
        return self.a + self.b + self.c

t = Threeangle(1,1,1)
p = Pryamoygolnik(1,1)
print(t.nazva,'-',t.per())
print(p.nazva,'-',p.per())
print(t)
print(p)
'''
'''
class Dot:
	def __init__(self,x,y):
		self.x = x
		self,y = y
	def dlina(self, other):
		return((other.x - self.x)**2+(other.y - self.y)**2)**(1/2)
	def incircle(self,r):
		return self.x**2 +self.y**2 <= r
'''