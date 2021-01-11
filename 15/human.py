'''
class human:
	def __init__(self, name, age, gender, weight, height):
		self.name = name
		self.age = age
		self.gender = gender
		self.weight = weight
		self.height = height

	def say_hello(self, say):
		print(say)

	def growing(self):
		self.age += 1

	def older_than_age(self, t_age):
		return self.age >= t_age

class Worker(human):
	def __init__(self, name, age, gender, weight, height, prof):
		super().__init__(name, age, gender, weight, height)
		self.prof = prof
	def work(self):
		print('I`m working')



pers1 = Worker('Andry', 17, 'man', 180, 80, 'kamenshic')
pers1.work()
pers1.say_hello('Hello world!')
print(pers1.prof)
'''