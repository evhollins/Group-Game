from random import randint
# weapon = [damage, price, acuracy out of 5]
wooden_sword = [1, 0, 2]
sword1 = [3, 100, 3]
sword2 = [5, 200, 4]
sword3 = [10, 300, 3]
bow = [randint(1,10), 300, 5]
weapons = [wooden_sword, sword1, sword2, sword3, bow]
weapons_text = ['wooden_sword', 'sword1', 'sword2', 'sword3', 'bow']


def buy_weapon():
	weapons_action = raw_input("Would you like to buy or sell? -->  ")
	if weapons_action == "buy":
		print "You can currently buy:", weapons_text
		choose_weapon = raw_input("What would you like to buy? -->  ")
		if 'wooden' in choose_weapon:
			weapon = wooden_sword
			print "You equiped wooden_sword."
		if 'sword1' in choose_weapon:
			lose_money(100)
			weapon = sword1
			print "You equiped sword1."
		if 'sword2' in choose_weapon:
			lose_money(200)
			weapon = sword2
			print "You equiped sword2."
		if 'sword3' in choose_weapon:
			lose_money(300)
			weapon = sword3
			print "You equiped sword3."
		if 'bow' in choose_weapon:
			lose_money(300)
			weapon = bow
			print "You equiped bow."	

buy_weapon()