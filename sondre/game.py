import random
import time


# class for the player
class Player:
    def __init__(self):
        self.name = str
        self.hitpoints = 20
        self.strength = 2
        self.inventory = []
        self.weapon_slot = str
        self.head_slot = str
        self.chest_slot = str
        self.coins = 0


# class for monster
class Monster:

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


# function for checking the players inventory
def check_inventory():
    # check if inventory is empty
    if player.inventory:
        print(player.inventory)
    else:
        print('You have nothing in your inventory')
    # exit inventory
    input('Press enter to exit inventory')


def shop():
    # Dictionary for in-stock items. Key is name of item, value is price
    in_stock = {
        'Healing potion': 5,  # Heal player to full hp
        'Sword': 7,  # Improve attack by 2
        'Crown of flowers': 7,  # improve seduction by 10%
    }

    print('You enter the shop, the shopkeeper welcomes you.')
    time.sleep(1)
    print('Items available for purchase:')
    for key, value in in_stock.items():
        print(key, ':', value, 'coins')
    print('What would you like to buy? (Type exit to exit shop)')
    while True:
        item_to_buy = input()
        if item_to_buy == 'exit':
            print('You exit the shop.')
            break
        if item_to_buy in in_stock.keys():
            if not player.coins - in_stock[item_to_buy] < 0:
                print(f'You purchased {item_to_buy}')
            else:
                print('You cannot afford this item')
        else:
            print('Please input the name of the item you would like to purchase.')


def fight():
    # call function to spawn new monster
    monster = Monster()
    monster.spawn_monster()
    #
    if monster.name == ('Ancient dragon', 'Orc'):
        print(f'An {monster.name} has appeared!')
    else:
        print(f'A {monster.name} has appeared!')
    time.sleep(1)
    print(f'The {monster.name} has {monster.hitpoints} HP, '
          f'and {monster.strength} strength')
    print('The monster is fierce, a fight breaks out!')
    fight_actions = ['inv', 'attack', 'seduce', 'run']
    while True:
        if monster.hitpoints <= 0:
            print('The monster has been defeated!')
            player.coins += monster.reward
            print(f'You gained {monster.reward} coins for defeating the monster')
            print(f'You now have {player.coins} coins')
            del monster
            break
        print('What do you want to do?')
        print('Options: Check your inventory [inv], Attack the monster [attack],\n'
              'Seduce the monster [seduce], Run away [run]')
        user_input = input()
        if user_input == 'inv':
            check_inventory()
        elif user_input == 'attack':
            print('You attack the monster')
            monster.hitpoints -= player.strength
            player.hitpoints -= monster.strength
            if monster.hitpoints <= 0:
                pass
            else:
                print(f'The monster has {monster.hitpoints} HP left')
            print(f'You have {player.hitpoints} HP left')
        elif user_input == 'seduce':
            print('You attempt to secude the monster')
            if random.randint(0, 100) >= 85:
                print("The monster is hypnotised by your moves, it leaves it's treasures behind.")
                player.coins += monster.reward
                print(f'You gain {monster.reward} coins for seducing the monster.')
                print(f'You now have {player.coins} coins')
            else:
                print('The monster is disgusted at your attempt of seduction, it attacks you')
                player.hitpoints -= monster.strength
                print(f'The monster has {monster.hitpoints} HP left')
                print(f'You have {player.hitpoints} HP left')
        elif user_input == 'run':
            print('You run away, you get nothing')
            del monster
            break
        else:
            print('Please provide a valid option.')
            print('Options: inv, attack, seduce, run')


def new_day():
    time.sleep(1.5)
    print(f'A new day awaits, Adventurer {player.name}!')
    time.sleep(2)
    print('What would you like to do this fine morning?')
    time.sleep(0.5)
    print('Options: Check your inventory [inv], Explore the woods [explore], Shop for goodies in the store [shop]')
    actions = ['inv', 'explore', 'shop']
    user_input = ''
    while user_input not in actions:
        user_input = input()
        if user_input == 'inv':
            check_inventory()
        elif user_input == 'explore':
            print('You go exploring in the woods.')
            time.sleep(2)
            exploration_action = random.randint(1, 1)
            if exploration_action == 1:
                fight()
            elif exploration_action == 2:
                print('You found an item')
            elif exploration_action == 3:
                print('You found nothing')
        elif user_input == 'shop':
            shop()
        else:
            print('Please provide a valid option.')
            print('Options: inv, explore, shop')


print('Welcome adventurer!')
print('What is your name?')
name = input()
player = Player()
player.name = name
print(f'Happy exploring {name}!')

while True:
    new_day()
