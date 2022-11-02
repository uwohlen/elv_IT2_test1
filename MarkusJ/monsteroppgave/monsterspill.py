# It imports the time, random, playsound and termcolor modules.
import time
import random
from playsound import playsound
from termcolor import cprint


#Player is a class with name, health points, attack points, an inventory, and cash
class Player:
    def __init__(self):
        self.name = str
        self.hp = 100
        self.attack = 20
        self.inventory = []
        self.cash = 0


#Monster is a class that has a name, hp, attack, and reward
class Monster:
    def __init__(self):
        self.name = str
        self.hp = int
        self.attack = int
        self.reward = int

    def create_monster(self):
        #creates a dictionary of monsters with their health, attack, and defense.
        monster_list = {
            'Joe Mama': [random.randint(1,1000),random.randint(1,50),random.randint(10,1000)],
            'Zombie': [50,10,25],
            'Spider': [25,5,10],
            'Axe Goblin': [40,30,30],
            'Skeleton': [35,15,20],
            'Dragon': [100,10,50]
        }

# Spawning a random monster from the monster_list dictionary.
        self.name = random.choice(list(monster_list))
        hp_attack_cash = monster_list.get(self.name)
        self.hp = hp_attack_cash[0]
        self.attack = hp_attack_cash[1]
        self.reward = hp_attack_cash[2]




def check_inventory():
    if player.inventory:
        print(player.inventory)
    else:
        print('You have nothing in your inventory')
    input('Press enter to exit inventory')


def weaponsdealer():
# A dictionary with the items that are in stock in the weaponsdealer.
    in_stock = {
        'knife (+10% ATK)': 10, #øker player.attack med 10%
        'handgun (+20% ATK)': 60, #øker player.attack med 20%
        'AK47 (+50% ATK)': 200, #øker player.attack med 50%
        'bazooka (+100% ATK)': 500, #øker player.attack med 100%
        'First aid kit (Full health)': 45, #setter player.hp til 100
        'kevlar vest (+100 HP)': 300 #øker player.hp med 100
    }

    print('You enter the shop, the weaponsdealer welcomes you.')
    print(f'You have {player.cash} cash.')
    print('Weapons available for purchase:')

    # Printing out the items in the in_stock dictionary.
    for key, value in in_stock.items():
        print(key, ':', value, 'cash')
    print('What would you like to buy? (Type exit to exit the shop)')

    # A while loop that runs until the user inputs 'exit'.
    while True:
        # Asking the user to input a string.
        item_to_buy = input()

        # Checking if the user inputs 'exit' and if they do, it breaks the while loop.
        if item_to_buy == 'exit':
            print('You exit the shop.')
            break
        # It checks if the item the user wants to buy is in the in_stock dictionary. If it is, it
        # checks if the user has enough cash to buy the item. If the user has enough cash, it prints
        # out a message saying that the user has purchased the item.
        if item_to_buy in in_stock.keys():
            if  not player.cash - in_stock[item_to_buy] < 0:
                print(f'You purchased {item_to_buy}')

                # Checking if the user has bought a specific item, and if they have, it adds the item
                # to their inventory and increases their attack or health.
                if item_to_buy == 'knife (+10% ATK)':
                    player.cash = player.cash - in_stock[item_to_buy]
                    player.attack = player.attack*1.1
                    player.inventory.append("Knife")

                elif item_to_buy == 'handgun (+20% ATK)':
                    player.cash = player.cash - in_stock[item_to_buy]
                    player.attack = player.attack*1.2
                    player.inventory.append("Handgun")

                elif item_to_buy == 'AK47 (+50% ATK)':
                    player.cash = player.cash - in_stock[item_to_buy]
                    player.attack = player.attack*1.5
                    player.inventory.append("AK47")

                elif item_to_buy == 'bazooka (+100% ATK)':
                    player.cash = player.cash - in_stock[item_to_buy]
                    player.attack = player.attack*2
                    player.inventory.append("Bazooka")

                elif item_to_buy == 'First aid kit (Full health)':
                    player.cash = player.cash - in_stock[item_to_buy]
                    player.hp = 100
                
                elif item_to_buy == 'kevlar vest (+100 HP)':
                    player.cash = player.cash - in_stock[item_to_buy]
                    player.inventory.append("Kevlar vest")
                    player.hp = player.hp + 100
            else:
                print('You don\'t have enough cash')
        else:
            cprint('Please input the name of the item you would like to purchase or exit the shop [exit]',"red", attrs=["bold"])



def battle():
# It creates a monster object and spawns a random monster from the monster_list dictionary.
    monster = Monster()
    monster.create_monster()

    # It prints out the name of the monster, the monsters health and the monsters attack.
    print(f'A {monster.name} has appeared!')
    print(f'The {monster.name} has {monster.hp} HP, 'f'and {monster.attack} attack')


    while True:
        # It checks if the monster has been defeated, and if it has, it prints out a message saying
        # that the monster has been defeated. It then adds the monsters reward to the players cash. It
        # then prints out a message saying that the monster dropped the reward and how much cash the
        # player now has. It then checks if the player has more than 1000 cash, and if they do, it
        # calls the winner function and exits the monster_game. It then deletes the monster object.
        if monster.hp <= 0:
            print('The monster has been defeated!')
            player.cash += monster.reward
            print(f'The {monster.name} dropped {monster.reward} cash for you to take.')
            print(f'You now have {player.cash} cash')
            if player.cash >= 500:
                winner()
                exit()
            del monster
            break

        print('What do you want to do?')
        print('Check your inventory ',end='')
        cprint('[inv]',"yellow",attrs=["bold"],end='') 
        print(', Attack the monster ',end='')
        cprint('[attack]',"yellow",attrs=["bold"],end='')
        print(', Run away ',end='')
        cprint('[run]',"yellow",attrs=["bold"])

        # Asking the user to input a string.
        user_input = input()
        # It checks if the user inputs 'inv' and if they do, it calls the check_inventory function.
        if user_input == 'inv':
            check_inventory()

        # It checks if the user inputs 'attack' and if they do, it prints out a message saying that
        # the user attacks the monster. It then subtracts the players attack from the monsters health.
        # It then subtracts the monsters attack from the players health. It then checks if the monster
        # has been defeated, and if it has, it does nothing. It then checks if the player has been
        # defeated, and if they have, it prints out a message saying that the player has died. It then
        # prints out a message saying that the monster_game is over. It then exits the monster_game. It then prints
        # out a message saying how much health the monster has left. It then prints out a message
        # saying how much health the player has left.
        elif user_input == 'attack':
            print('You attack the monster')
            monster.hp -= player.attack
            player.hp -= monster.attack

            if monster.hp <= 0:
                pass

            elif player.hp <= 0:
                print("YOU DIED!")
                time.sleep(1)
                print("GAME OVER")
                exit()

            else:
                print(f'The monster has {monster.hp} HP left')
            
                # This is checking if the players health is less than or equal to 49, and if it is, it
                # prints out a message saying how much health the player has left in red. If the
                # players health is not less than or equal to 49, it prints out a message saying how
                # much health the player has left in green.
                if player.hp <= 49:
                    cprint(f'You have {player.hp} HP left',"red", attrs=["bold"])
            
                else:
                    cprint(f'You have {player.hp} HP left',"green", attrs=["bold"])
            
        
        # Checking if the user inputs 'run' and if they do, it prints out a message saying that the
        # user runs away. It then deletes the monster object. It then breaks the while loop.
        elif user_input == 'run':
            print('You ran away, you got nothing')
            del monster
            break
        else:
            cprint('Please provide a valid option.',"red", attrs=["bold"])
            cprint('Options: inv, attack, run',"red", attrs=["bold"])



def new_day():

    print('What would you like to do?')
    time.sleep(0.5)

    # A while loop that runs until the user inputs a valid option.
    print('Options: Explore the woods for monsters ',end='')
    cprint('[explore]',"yellow",attrs=["bold"],end='')
    print(', Check your inventory ',end='')
    cprint('[inv]',"yellow",attrs=["bold"],end='') 
    print(', Shop for weapons and healing in the weaponstore ',end='')
    cprint('[shop]',"yellow",attrs=["bold"])

    actions = ['inv', 'explore', 'shop']
    user_input = ''

    # Checking if the user_input is in the actions list. If it is not, it will run the code inside the
    # while loop.
    while user_input not in actions:
       # Asking the user to input a string, and if the user inputs 'inv', it calls the check_inventory
       # function.
        user_input = input()
        if user_input == 'inv':
            check_inventory()

        # Checking if the user inputs 'explore' and if they do, it prints out a message saying that
        # the user goes exploring in the woods. It then waits for 1 second. It then checks if a random
        # number between 0 and 100 is less than or equal to 99. If it is, it calls the battle
        # function. If it is not, it prints out a message saying that the user found a Raygun. It then
        # adds the Raygun to the players inventory. It then increases the players attack by 100.
        elif user_input == 'explore':
            print('You go exploring in the woods.')
            time.sleep(1)
            if random.randint(0, 50) <= 49:
                battle()
            else: 
                print('You found a Raygun')
                player.inventory.append('Raygun')
                player.attack = player.attack*100

        # It checks if the user inputs 'shop' and if they do, it calls the weaponsdealer function.
        elif user_input == 'shop':
            weaponsdealer()

        else:
            cprint('Please provide a valid option.',"red", attrs=["bold"])
            print('Options: inv, explore, shop')


#This function prints out a message and plays a sound when the player wins the monster_game
def winner():
        print('GG')
        print('You have successfully fought your way through the forrest')
        playsound('goat.mp3')
        


# Asking the user to input a string, and then it creates a player object and sets the
# players name to the string the user inputted. It then prints out a message saying good luck and the
# players name.
print('What is your name?')
name = input()
player = Player()
player.name = name
print(f'Good luck {name}, your mission is to fight your way through the forrest')


# Creating an infinite loop that calls the new_day function.
while True:
    new_day()