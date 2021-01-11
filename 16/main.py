from personages.Class import *
print('la, la')
name = input('Enter hero`s name: ')
ans = 0
while ans not in [1,2,3] :
	ans = int(input("Choose class: 1: Archer, 2: Knigth, 3: Wizard "))
	if ans == 1:
		hero = Archer(1)
	elif ans == 2:
		hero = Knight(1)
	elif ans == 3:
		hero = Wizard(1)
	else:
		print('Try again')
print(hero)

en1 = Knight(1)
try:
	en1.hp -= hero.attack()
except:
	hero.attack()
try:
	en1.hp -= hero.attack()
except:
	hero.attack()
try:
	en1.hp -= hero.attack()
except:
	hero.attack()

