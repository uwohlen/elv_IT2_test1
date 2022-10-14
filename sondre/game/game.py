import random
import time


# class for the player
class Player:
    # player variables
    def __init__(self):
        self.name = str
        self.hitpoints = 20
        self.strength = 2
        self.inventory = []
        self.weapon_slot = None
        self.head_slot = None
        self.chest_slot = None
        self.coins = 0
        self.in_fight = False
        self.alive = True
        self.score = 0


# class for monster
class Monster:
    # monster variables
    def __init__(self):
        self.name = str
        self.hitpoints = int
        self.strength = int
        self.reward = int

    def spawn_monster(self):
        # Dict with monster name as key, Hitpoints, strength and coins rewarded as values
        monster_names_dict = {
            'Ancient dragon': [35, 11, 25],
            'Bat': [3, 1, 2],
            'Rat': [2, 2, 3],
            'Fire elemental': [5, 5, 5],
            'Hydra': [3, 3, 4],
            'Mind flayer': [20, 8, 15],
            'Orc': [5, 3, 4],
            'Shadow': [8, 1, 4],
            'Zombie': [6, 2, 6],
            'Mystic': [random.randint(1, 15), random.randint(1, 6), random.randint(1, 10)]
        }
        # select a random monster, give the monster values for name, hitpoints and strength
        self.name = random.choice(list(monster_names_dict))
        hitpoints_strength_reward = monster_names_dict.get(self.name)
        self.hitpoints = hitpoints_strength_reward[0]
        self.strength = hitpoints_strength_reward[1]
        self.reward = hitpoints_strength_reward[2]


def write_highscore():
    with open('highscores.txt', mode='a') as f:
        highscore = f'{player.name}: {player.score}'
        f.write(f'\n{highscore}')


def read_highscores():
    with open('highscores.txt', mode='r') as f:
        for line in f:
            print(line)


# function for checking the players inventory
def check_inventory():
    # check if inventory is empty
    if player.inventory:
        # print contents of player inventory
        print('You have following items in your inventory:')
        for item in player.inventory:
            print(item)
    else:
        print('You have nothing in your inventory')
    # check if player has anything equipped
    if (player.head_slot, player.weapon_slot, player.chest_slot) is None:
        print('You have nothing equipped.')
    # check if player has anything equipped on their head slot
    if player.head_slot is not None:
        print(f'You have equipped {player.head_slot} in your head slot')
    # check if player has anything equipped in their weapon slot
    if player.weapon_slot is not None:
        print(f'You have equipped {player.weapon_slot} in your weapon slot')
    # check if player has anything equipped on their chest slot
    if player.chest_slot is not None:
        print(f'You have equipped {player.chest_slot} in your chest slot')

    if player.inventory:
        if player.in_fight:
            print('Type the name of an item to use it. Type exit to [exit] inventory')
            while True:
                item_to_use = input()
                print('')
                if item_to_use == 'Healing potion':
                    player.inventory.remove(item_to_use)
                    player.hitpoints = 20
                    print(f'You now have {player.hitpoints} HP')
                    break
                elif item_to_use == 'exit':
                    break
                else:
                    print('Invalid input, please try again')
    else:
        print('You have no items to use')

    # exit inventory
    time.sleep(1.5)
    input('Press [enter] to exit inventory')


# function for purchasing items
def add_to_slot(item, slot, price):
    # functon to process payment and equip item
    def payment(type_of_item):
        # subtract payment
        player.coins -= int(price)
        # check what kind of item the purchased item is
        if type_of_item == 'weapon':
            player.weapon_slot = item
        elif type_of_item == 'head':
            player.head_slot = item
        time.sleep(0.5)
        print(f'You purchased {item}.')
        time.sleep(1)
        print(f'{item} has been equipped')

    # check if item is a weapon
    if slot == 'weapon':
        # if a weapon is not equipped, buy and equip weapon
        if player.weapon_slot is None:
            payment('weapon')
        # if a weapon is already equipped, add equipped weapon to inventory, buy and equip new weapon
        else:
            player.inventory.append(player.weapon_slot)
            payment('weapon')
            print(f'{player.inventory[-1]} has been added to your inventory.')
    # check if item is a hat
    if slot == 'head':
        # if a hat is not equipped, buy and equip hat
        if player.head_slot is None:
            payment('head')
        # if a hat is already equipped, add equipped hat to inventory, buy and equip new hat
        else:
            player.inventory.append(player.head_slot)
            payment('head')
            print(f'{player.inventory[-1]} has been added to your inventory.')


# function to buy and add non-equipable items to inventory
def add_to_inv(item_to_buy, price_slot):
    # buy item, add item to inventory
    player.coins -= int(price_slot[0])
    player.inventory.append(item_to_buy)
    print(f'You purchased {item_to_buy}')
    time.sleep(1)
    print(f'{item_to_buy} has been added to your inventory')


# shop function, called when the player wants to enter the shop
def shop():
    # Dictionary for in-stock items. Key is name of item, values are price and slot
    in_stock = {
        'Healing potion': [5, 'inv'],  # Heal player to full hp
        'Sword': [7, 'weapon'],  # Improve attack by 2
        'Crown of flowers': [7, 'head'],  # improve seduction by 15%
        'Axe': [15, 'weapon']  # improve attack by 4
    }

    print('You enter the shop, the shopkeeper welcomes you.')
    # shop loop
    while True:
        time.sleep(2)
        # print items available for purchase
        print('Items available for purchase:')
        time.sleep(1.5)
        for key, value in in_stock.items():
            print(key, ':', value[0], 'coins')
        time.sleep(2)
        # prompt user action
        print('What would you like to buy? (Type [exit] to exit shop, [inv] to check your inventory)')
        time.sleep(1)
        print(f'You have {player.coins} coins.')
        # get item to buy
        item_to_buy = input()
        print('')
        # exit shop
        if item_to_buy == 'exit':
            print('You exit the shop.')
            break
        # check inventory
        if item_to_buy == 'inv':
            check_inventory()
        # get value for item key
        price_slot = in_stock.get(item_to_buy)
        # check if input is valid. if not, prompt new input
        if item_to_buy in in_stock.keys():

            # check if player can afford item. if not, tell player they don't have enough coins
            if not player.coins - int(price_slot[0]) < 0:
                # check if item to purchase is in the inventory slot
                if price_slot[1] == 'inv':
                    add_to_inv(item_to_buy, price_slot)
                # check if item to purchase is a weapon
                if price_slot[1] == 'weapon':
                    add_to_slot(item_to_buy, price_slot[1], price_slot[0])
                # check if item to purchase is a hat
                if price_slot[1] == 'head':
                    add_to_slot(item_to_buy, price_slot[1], price_slot[0])
            else:
                print('You cannot afford this item')

        else:
            print('Please input the name of the item you would like to purchase.')


# fight function, called when player meets a monster
def fight():
    player.in_fight = True

    # attack function, makes sure strength of player is correct according to currently equipped items
    def attack():
        # check what weapon the player has equipped, update players strength accordingly
        if player.weapon_slot == 'Sword':
            player.strength = 4
        if player.weapon_slot == 'Axe':
            player.strength = 6
        # attack the monster
        monster.hitpoints -= player.strength
        player.score += player.strength

    # initialize new monster
    monster = Monster()
    # call function to spawn new monster
    monster.spawn_monster()
    # grammar check, makes sure the name of the monster is printed correctly with 'A' or 'An'
    if monster.name == ('Ancient dragon', 'Orc'):
        print(f'An {monster.name} has appeared!')
    else:
        print(f'A {monster.name} has appeared!')
    time.sleep(1)
    # print info about the monster to the player
    print(f'The {monster.name} has {monster.hitpoints} HP, '
          f'and {monster.strength} strength')
    print('The monster is fierce, a fight breaks out!')

    while True:
        # check if player is alive. if not, end game
        if player.hitpoints <= 0:
            print('You have died.')
            print('Game Over.')
            print(f'You got a score of {player.score}')
            write_highscore()
            print(f'Do you want to see the high score list? [y/n]')
            see_highscore = input()
            print('')
            if see_highscore == 'y':
                read_highscores()
            player.alive = False
            break

        # check if monster is alive. If not, grant the player the reward
        if monster.hitpoints <= 0:  # error is a pycharm visual error, does not occur in other editors
            print('The monster has been defeated!')
            # grant player reward
            player.coins += monster.reward
            time.sleep(2)
            print(f'You gained {monster.reward} coins for defeating the monster')
            time.sleep(1.5)
            print(f'You now have {player.coins} coins')
            # delete instance of monster to optimize memory usage
            player.in_fight = False
            del monster
            break

        # prompt player for action
        time.sleep(2)
        print('What do you want to do?')
        time.sleep(1)
        print('Options: Check your inventory [inv], Attack the monster [attack],\n'
              'Seduce the monster [seduce], Run away [run]')
        user_input = input()
        print('')
        # Check what the player wants to do

        # access inventory
        if user_input == 'inv':
            check_inventory()

        # attack the monster
        elif user_input == 'attack':
            print('You attack the monster')
            attack()
            player.hitpoints -= monster.strength
            # check if monster is alive.
            if not monster.hitpoints <= 0:  # error is a pycharm visual error, does not occur in other editors
                time.sleep(1)
                print(f'The monster has {monster.hitpoints} HP left')

            time.sleep(1)
            if player.hitpoints < 0:
                print('You have 0 HP left')
            else:
                print(f'You have {player.hitpoints} HP left')

        # try to seduce the monster
        elif user_input == 'seduce':
            print('You attempt to seduce the monster')
            # decide if the monster will be seduced, 15% chance of success
            # chance of seduction is 25% if player has 'Crown of flowers' equipped
            if player.head_slot == 'Crown of flowers':
                seduction_chance = 70
            else:
                seduction_chance = 85
            if random.randint(0, 100) >= seduction_chance:
                time.sleep(3)
                print("The monster is hypnotised by your moves, it leaves it's treasures behind.")
                player.coins += monster.reward
                time.sleep(1)
                # get reward from monster
                print(f'You gain {monster.reward} coins for seducing the monster.')
                time.sleep(1)
                print(f'You now have {player.coins} coins')
                player.in_fight = False
                # delete monster instance to optimize memory usage
                del monster
                # end fight
                break
            # execute if the attempt of seduction fails
            else:
                time.sleep(3)
                print('The monster is disgusted at your attempt of seduction, it attacks you')
                player.hitpoints -= monster.strength
                time.sleep(1)
                print(f'The monster has {monster.hitpoints} HP left')
                time.sleep(1)
                print(f'You have {player.hitpoints} HP left')

        # run away, player will get nothing
        elif user_input == 'run':
            print('You run away, you get nothing')
            player.in_fight = False
            # delete monster instance to optimize memory usage
            del monster
            # end fight
            break

        # prompt user if no valid input is detected
        else:
            print('Please provide a valid option.')
            print('Options: [inv], [attack[, [seduce], [run]')


# function for starting a new day
def new_day():
    # greetings to the player at the start of the day
    time.sleep(1.5)
    print(f'A new day awaits, Adventurer {player.name}!')
    time.sleep(2)
    print('What would you like to do this fine morning?')
    time.sleep(0.5)
    # prompt user for action
    print('Options: Check your inventory [inv], Explore the woods [explore], Shop for goodies in the store [shop]')
    # list of actions user can do
    actions = ['inv', 'explore', 'shop']
    user_input = ''
    # loop for executing actions. prompts user for new input if given input is not a valid action
    while user_input not in actions:
        # get input
        user_input = input()
        print('')
        # access inventory if player requests to
        if user_input == 'inv':
            check_inventory()
        # explore the woods if the player requests so
        elif user_input == 'explore':
            print('You go exploring in the woods.')
            time.sleep(2)
            # initiate fight with monster
            fight()
        # access shop if player requests so
        elif user_input == 'shop':
            shop()
        # prompt for new input if no valid input is provided
        else:
            print('Please provide a valid option.')
            print('Options: [inv], [explore], [shop]')


# greeting at start of game
print('Welcome adventurer!')
# name prompt
print('What is your name?')
name = input()
print('')
# initialize new player object
player = Player()
# set name of player to given input
player.name = name
print(f'Happy exploring {name}!')

# game loop, stats a new day as long as the player is alive
while player.alive is True:
    new_day()
