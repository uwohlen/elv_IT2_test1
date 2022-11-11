import random
import time


player_name = str(input("what is your name? "))

class Monster:
    def __init__(self, name, hp, attack, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.speed = speed

class Player(Monster):
    def __init__(self, name, hp, attack, speed):
        super().__init__(name, hp, attack, speed)

class Attack_moves:
    def __init__(self, damage):
        self.damage = damage

class Gun(Attack_moves):
    def __init__(self, damage):
        super().__init__(damage = 3)


gun = Gun(3)

max_player_hp = 17

# max_goblin_hp = 5

# max_spider_hp = 3

# max_metapod_hp = 100

# max_helldawg_hp = 14

# max_dragon_hp = 20

player = Player(player_name, 17,4,4)

goblin = Monster("goblin",5,2,5)

spider = Monster("spider", 3, 5, 3)

metapod = Monster("metapod", 100, 1, 1)

helldawg = Monster("helldawg", 14, 7, 6)

dragon = Monster("dragon", 20, 16, 14)

monsters = [goblin, spider, metapod, helldawg, dragon]


def menu():
    loading()
    player_choice = input(f'what would you like to do {player_name}, go into the dungeon [dungeon], use skillpoints [skillpoints], sleep? [sleep] ')
    loading()
    if player_choice == "dungeon":
        battle()
        loading()
    elif player_choice =="skillpoints":
        loading()
        print("skillpoints aint a thing yet")
    elif player_choice == "sleep":
        loading()
        player.hp = max_player_hp
        print("you now have", player.hp, "hp")
        menu()
    else: print("you didnt write either dungeon, skillpoints or sleep")


def battle():
    global ran_monster
    ran_monster = monsters[random.randint(0,4)]
    print(f'you encounter a {ran_monster.name}')
    print(f'the monster has {ran_monster.hp} hp, {ran_monster.attack} attack')
    if player.speed > ran_monster.speed:
        player_turn()
    elif ran_monster.speed > player.speed:
        monster_turn()


def player_turn():
    global ran_monster
    print(player_name, "s turn")
    choosen_action = str(input("what do you want to do? [attack] [run away]"))
    loading()
    if choosen_action == "attack":
        ran_monster.hp = ran_monster.hp - (gun.damage + player.attack)
        print(f'{ran_monster.name} lost, {(gun.damage + player.attack)}, hp left is', ran_monster.hp)
        if ran_monster.hp <= 0:
            print("you won")
            next_action = str(input("do you want to continue exploring the dungeon [explore] or return to the tavern and sleep to recover hp [tavern]"))
            if next_action == "explore":
                battle()
            elif next_action =="tavern":
                menu()
            else:
                print("we assume you want to return to the tavern ")
        else:
            monster_turn()
    elif choosen_action == "run away":
        print(f'you run away from the {ran_monster.name} and return to the tavern')
        print(f'you have {player.hp} left and might want to sleep to regain some hp')
        menu()


def monster_turn():
    global ran_monster
    print(f'{ran_monster.name}s turn')
    loading()
    player.hp = player.hp - ran_monster.attack
    print(f'{ran_monster.name} attacked')
    print(player_name,"took", ran_monster.attack, "damage", player_name, "has", player.hp, "hp left")
    if player.hp <= 0:
            print("you lost")
    else:
        player_turn()


def loading():
    for i in range(1, 2):
        print("...")
        time.sleep(i)


menu()
