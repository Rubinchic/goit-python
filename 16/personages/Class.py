from datetime import *
class Human:
	def __init__(self, title, hp, stamina, speed, level, attack, reload, last_attack):
		self.title = title
		self.stamina = stamina
		self.hp = hp
		self.speed = speed
		self.level = level
		self.attack = attack
		self.reload_time = reload
		self.last_attack = None
	def chack_attack(self):
		if self.last_attack and datetime.now()-self.last_attack<timedalta(microseconds=self.reload_time):
			return False
		else:
			return True

	def attack(self):
		if self.chack_attack():
			self.last_attack = datetime.now()
			print("boom")
			return self.attack
		else:
			print('None')
			return 0 

	def __str__(self):
		return f"Race: {self.title}"

class Archer(Human):
	def __init__(self,level):
		self.title = "Archer"
		super().__init__(self.title,
						80+level*20, 
						95+level*5,
						3,
						level,
						35+level*5,
						150)


class Knight(Human):
	def __init__(self, level):
		self.title = "Knight"
		super().__init__(self.title,
						130+level*20, 
						85+level*5,
						1,
						level,
						55+level*5,
						100)


class Wizard(Human):
	def __init__(self, level):
		self.title = "Wizard"
		super().__init__(self.title,
						80+level*10, 
						105+level*10,
						5,
						level,
						45+level*5,
						150)
