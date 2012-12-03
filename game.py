
from sys import exit
import time
from random import randint
money = 0
health = 10
energy = 10
weapon = "Wooden Sword"
name = "No Name"



def intro():
        print "Name?"

        name_input = raw_input("--> ")
        

        print "Are you sure you want your name to be %r?" % name_input

        confirm = raw_input("--> ")

        if "yes" in confirm: 
                print "Okay here we go."
                home(True) 

        if "no" in confirm:
                introno()
        return name_input

def introno():
        print "Then what is your name?"

        name_input = raw_input("--> ")

        print "Are you sure you want your name to be %r?" % name_input

        confirm = raw_input("--> ")

        if "yes" in confirm: 
                print "Okay here we go."
                home(True) 

        if "no" in confirm:
                introno()

def home(intro):
        if intro == True:
                print """
                Welcome to your house, %r!
                Here you can buy weapons, sleep to regain energy, or buy food to regain health. 
                Your energy determines how much you can do before you have to go to sleep.
                You currently have %d money, %d health, and %d energy.
                """ % (name, money, health, energy)
                home(False)
        if intro == False:
                print "Would you like to sleep, buy food, or buy weapons?"
                home_action = raw_input("->  ")
                if home_action == "sleep":
                        sleep("home")
                if "weapon" in home_action or "weapons" in home_action:
                        buy_weapon() 
def lose_money(amount):
        lose_money_repeats = 0
        while lose_money_repeats <= amount and money >= 0:
                money = money - 1
                lose_money_repeats = lose_money_repeats + 1

def gain_energy(amount):
        gain_energy_repeats = 0
        while gain_energy_repeats <= amount and energy <= 10:
                energy = energy + 1
                gain_energy_repeats = gain_energy_repeats + 1

def lose_energy(amount):
        lose_energy_repeats = 0
        while lose_energy_repeats <= amount and energy >= 0:
                energy = energy - 1
                lose_energy_repeats = lose_energy_repeats + 1

def gain_health(amount):
        gain_health_repeats = 0
        while gain_health_repeats <= amount and health <= 10:
                health = health + 1
                gain_health_repeats = gain_health_repeats + 1

def lose_health(amount):
        lose_health_repeats = 0
        while lose_health_repeats <= amount and health >= 0:
                health = health - 1
                lose_health_repeats = lose_health_repeats + 1


def sleep(location):
        if location == "home":
                print "Sleeping..."
                time.sleep(1)
                print "Sleeping..."
                time.sleep(1)
                print "Sleeping..."
                time.sleep(1)
                print "Sleeping..."
                time.sleep(1)
                print "Sleeping..."
                time.sleep(1)
                print "Sleeping..."
                time.sleep(1)
                print "Sleeping..."
                time.sleep(1)
                print "Sleeping..."
                time.sleep(1)
                print "Sleeping..."
                time.sleep(1)
                print "Sleeping..."
                time.sleep(1)
                energy = 10
                print "You got a good night's sleep! Your energy is now 10."
                home(False)

        if location == "forest":
                print "You have trouble falling sleep, but finally do."
                time.sleep(1)
                sleep_forest_randint = randint(1,5)
                if sleep_forest_randint <= 3:
                        print "Sleeping..."
                        time.sleep(1)
                        print "Sleeping..."
                        time.sleep(1)
                        print "Sleeping..."
                        time.sleep(1)
                        print "Sleeping..."
                        time.sleep(1)
                        print "Sleeping..."
                        time.sleep(1)
                        print """
                        You jolt awake from a nightmare. You hear rustling in the bushes, 
                        but you never find out what it is because you fall asleep.
                        """
                        time.sleep(2)
                        print "Sleeping..."
                        time.sleep(1)
                        print "Sleeping..."
                        time.sleep(1)
                        print "Sleeping..."
                        time.sleep(1)
                        print "Sleeping..."
                        time.sleep(1)
                        gain_energy(5)
                        print "You didn't have a very good night's sleep. At least you weren't eaten. Your energy is now %d." % energy

                if sleep_forest_randint >= 4:
                        print "Sleeping..."
                        time.sleep(1)
                        print "Sleeping..."
                        time.sleep(1)
                        print "Sleeping..."
                        time.sleep(1)
                        print "Sleeping..."
                        time.sleep(1)
                        print "Sleeping..."
                        time.sleep(1)
                        print """
                        You jolt awake from a nightmare. You hear rustling in the bushes.
                        Then, out of no where, you are attacked by Big Foot!
                        You try to attack, but are too groggy. Big Foot has already done 3
                        dammage! Quick, do you want to attack or flee?
                        """
                        lose_health(3)
                        action = raw_input("-->  ")
                        big_foot_health = 5
                        if action == "flee":
                                print "Stupid! You can't outrun Big Foot!"
                                lose_health(1)  
                        if action == "attack":
                                while health > 0 and big_foot_health > 0:
                                        print "You attack do %d damage!" % weapon(0)
                                        big_foot_health = big_foot_health - weapon(0)
                                        time.sleep(1)
                                        print "Big Foot is furious! He punches you and does 1 damage!"
                                        lose_health(1)
                                        print "Your health is now %d" % health
                                        time.sleep(1)
                        if health == 0:
                                print "You dumbass! You died!"
                                exit()
                        if big_foot_health == 0:
                                print "With your final blow, Big Foot comes tumbling down, creating a small earthquake!"
                                print "He has just enough energy to flee before you can finish him off!"

                if location == "grassland":
                        print "You find that it is surprisingly easy to fall asleep."
                        time.sleep(1)
                        sleep_grassland_radint = radint(1,5)

                        if sleep_grassland_radint <= 2:
                                print "Sleeping..."
                                time.sleep(1)
                                print "Sleeping..."
                                time.sleep(1)
                                print "Sleeping..."
                                time.sleep(1)
                                print "Sleeping..."
                                time.sleep(1)
                                print "Sleeping..."
                                print """
                                While you are sleeping you are awoken by a rustling in your campsite. You peek through a hole in your tent 
                                and see a group of bandits rummaging through your stuff. 
                                Do you want to hide or fight?
                                """
                                action = raw_input("--> ")
                                bandit_health = 2
                                if action == "hide":
                                        print "You servive but they beat you up and steal your lunch money."
                                        lose_money(50)
                                if action == "fight":
                                        while health > 0 and bandit_health > 0:
                                                print "Your attack does %d damage!" % weapon(0)
                                                bandit_health = bandit_health - weapon(0)
                                                time.sleep(1)
                                                print "The bandits skillfully counter and do 2 damage."
                                                lose_health(2)
                                                print "Your health is now %d." % health
                                                time.sleep(1)
                        if health == 0:
                                print "Silly boy, you died to some wimpy bandits."
                                exit()
                        if bandit_health == 0:
                                print "You finally slay the last of the bandits. As you search their bodies you find 100 money on their person."
                                gain_money(100)         


def fighting(location):
        if location == "forest":
                pass
        if location == "grass":
                pass
        if location == "desert":
                pass


# weapon = [damage, price, acuracy out of 5]
wooden_sword = [1, 0, 2]
sword1 = [3, 100, 3]
sword2 = [5, 200, 4]
sword3 = [10, 300, 3]
bow = [randint(1,10), 300, 5]
weapons = [wooden_sword, sword1, sword2, sword3, bow]
weapons_text = ['wooden_sword: 0', 'sword1: 100', 'sword2: 200', 'sword3: 300', 'bow: 300']


def buy_weapon():
        print "You can currently buy:", weapons_text
        choose_weapon = raw_input("What would you like to buy? -->  ")
        if 'wooden' in choose_weapon:
                weapon = wooden_sword
                print "You equiped wooden_sword."
        if 'sword1' in choose_weapon:
                if money >= 100:
                        lose_money(100)
                        weapon = sword1
                        print "You equiped sword1."
                elif money < 100:
                        print "You do not have enough money for this item."
        if 'sword2' in choose_weapon:
                if money >= 200:
                        lose_money(200)
                        weapon = sword2
                        print "You equiped sword2."
                elif money < 200:
                        print "You do not have enough money for this item."
        if 'sword3' in choose_weapon:
                if money >= 300:
                        lose_money(300)
                        weapon = sword3
                        print "You equiped sword3."
                elif money < 300:
                        print "You do not have enough money for this item."
        if 'bow' in choose_weapon:
                if money >= 300:
                        lose_money(300)
                        weapon = bow
                        print "You equiped bow."
                elif money < 300:
                        print "You do not have enough money for this item. Try again later."
        home(False)


def squareA2(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareA3(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareA4(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareA5(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareB1(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareB2(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareB3(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareB4(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareB5(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareC1(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareC2(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass
        
def squareC4(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareC5(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareD1(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareD2(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareD3(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareD4(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareD5(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareE1(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareE2(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareE3(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareE4(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

def squareE5(entered):
        if entered == "south":
                pass
        elif entered == "north":
                pass
        elif entered == "east":
                pass
        elif entered == "west":
                pass

name = intro()