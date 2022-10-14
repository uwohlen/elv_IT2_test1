import random as rnd
import numpy as np

buffer = list('|   ')

# possible weapons to have in inventory
weapons = {
    "Sword": [3.5, 1, 1],
    "Bow": [1, 4, 10],
    "Throwing star": [2, 2, 5]
    # "weapon": [damage multiplier, 1 in x hit chance, range]
}

class Game():
    def __init__(self, Width, Height, player, Monsters):
        self.x = Height
        self.y = Width
        self.x += 1
        self.board = np.empty((self.x, self.y), dtype='str')
        
    def init(self, monsters, player): # initialise the game board by setting up pieces
        self.board.fill(' ')
        for x in range(0, len(monsters)):
            self.board[monsters[x].pos[0]][monsters[x].pos[1]] = 'M'
        self.board[player.pos[0]][player.pos[1]] = 'P'
        self.printBoard(player, monsters)

    
    def printBoard(self, player, monsters): # function for displaying the board to the terminal
        print("\n" * 20)
        for y in range(0, self.y):
            for i in range(0, self.x * 4 - 3):
                print('-', end='')
            print('')
            for x in range(0, self.x):
                tmp = buffer.copy()
                tmp[2] = self.board[x][y]
                print(''.join(tmp), end='')
            print('')
        for i in range(0, self.x * 4 - 3):
                print('-', end='')
        print(f'\nPlayer Health: {player.health}\nMonster Health: {monsters[0].health}')
        
    def G_round(self, player, monsters):
        action = input("Enter command:\n")
        
        if action == 'a':
            self.G_P_attack(player, monsters)
        elif action == 'm':
            self.G_P_move(player)
        elif action == 'e':
            self.G_P_Inventory(player)
            self.G_round(player, monsters)
        else:
            print("Invalid input")
            #monsters[0].health = 0
            #return
            self.G_round(player, monsters)
            
        if monsters[0].alive(game, player, monsters) != 1:
            return
        monster.playRound(player, self)
        self.printBoard(player, monsters)
    
    def G_P_attack(self, player, monsters):
        if len(monsters) == 1:
            x = 0
        else:
            tmp = input("Which Monster:\n")
            x = int(tmp) - 1
        player.attack(monsters[x])
    
    def G_P_move(self, player):
        x = 0
        y = 0
        direction = list(input("Enter movement commands:\n"))
        if len(direction) > 2:
            print("Invalid number of moves, only 2 allowed!!!")
            self.G_P_move(player)
        for i in direction:
            if i == 'a':
                x -= 1
            elif i == 'd':
                x += 1
            elif i == 'w':
                y += 1
            elif i == 's':
                y -= 1
            else:
                print("Invalid direction, only use w, a, s, d!!!")
                self.G_P_move(player)
        player.move(x, y, self)
    
    def G_P_Inventory(self, player):
        print(f"Use the numbers to select a weapon, you currently have: {player.inventory[0]}")
        for i in weapons:
            print(f"{list(weapons.keys()).index(i) + 1}. {i}")
        inp = int(input())
        player.inventory[0] = list(weapons.keys())[inp - 1]
        print(f"You selected {list(weapons.keys())[inp - 1]}")
        
        
class Monster():
    
    def __init__(self, xpos, ypos):
        self.health = 1
        self.pos = [xpos, ypos]
        
    def __len__(self): # used so that length of monster list refers to number of entries
        return 1
 
    def hit(self, amount):
        self.health -= amount
        
    def attack(self, player): # attack player, damage decreases with inverse square law proportional to distance from player
        initial = rnd.randint(10, 40)
        prange = np.sqrt((self.pos[0] - player.pos[0]) ** 2 + (player.pos[1] - self.pos[1]) ** 2)
        amount = int(initial / (prange ** 2))
        player.health -= amount
        if amount > 0:
            print(f"Oh No!!! A Monster did {amount} damage to you you now have {player.health} health left!!!")
    
    def move(self, player, game):
        # clear monster piece from board
        game.board[self.pos[0]][self.pos[1]] = ' '
        distance = [player.pos[0] - self.pos[0], player.pos[1] - self.pos[1]]
        
        # don't move if the range to the player is 1
        if np.sqrt(distance[0] ** 2 + distance[1] ** 2) == 1:
            self.pos[1] += int(distance[1])
            game.board[self.pos[0]][self.pos[1]] = 'M'
            game.printBoard()
            print("The monster didnt move")
            return
        
        # remove any 1s in the distance from player vector
        for x in range(len(distance)):
            if abs(distance[x]) == 1:
                distance[x] = 0
            if distance[x] == 0:
                distance.remove(distance[x])
                self.pos[1 - x] += int(distance[0] / abs(distance[0]))
                game.board[self.pos[0]][self.pos[1]] = 'M'
                #game.printBoard()
                return

        # make a unit vector with direction towards the player and magnitude of 1           
        tmp = lambda x: x / abs(x)
        distance = list(map(tmp, distance))
        # 50/50 if the monster moves on x or y axis
        random = rnd.randint(0, 1)
        if random == 1:
            self.pos[0] += int(distance[0])
        else:
            self.pos[1] += int(distance[1])
        game.board[self.pos[0]][self.pos[1]] = 'M'
        #game.printBoard()
        
    def playRound(self, player, game):
        prange = round(np.sqrt((player.pos[0] - self.pos[0]) ** 2 + (player.pos[1] - self.pos[1]) ** 2), 0)
        if rnd.randint(1, prange) == 1:
            self.attack(player)
        else:
            self.move(player, game)
            
    def alive(self, game, player, monsters):
        if self.health <= 0:
            game.board[self.pos[0]][self.pos[1]] = ' '
            game.printBoard(player, monsters)
            print("The monster is dead!!! You Win!!!")
            return 0
        else:
            return 1
        
class Player():
    
    def __init__(self, xpos, ypos):
        self.health = 100
        self.inventory = ["Throwing star", None, None, None]
        self.pos = [xpos, ypos]
        
    def hit(self, amount):
        self.health -= amount
        
    def mrange(self, monster): # distance player is from the monster
        dx = self.pos[0] - monster.pos[0]
        dy = self.pos[1] - monster.pos[1]
        return round(np.sqrt(dy ** 2 + dx ** 2), 2)
        
    def attack(self, monster):
        # make sure the weapon is in range
        if self.mrange(monster) > weapons[self.inventory[0]][2]:
            print("You are too far away for this to be effective!!!")
            return

        amount = rnd.randint(0, 20) # base damage
        amount *= weapons[self.inventory[0]][0] # base damage * damage multiplier of weapon
        if rnd.randint(1, weapons[self.inventory[0]][1]) != 1: # did you hit the monster?
            print("Oh no you missed!!!")
            return

        monster.hit(amount)
        print(f"You did {amount} damage to the monster, he now has {monster.health} health!!!")
    
    def move(self, x, y, game): # move based on dx and dy given in parameters
        game.board[self.pos[0]][self.pos[1]] = ' '
        self.pos[0] += x
        self.pos[1] -= y
        game.board[self.pos[0]][self.pos[1]] = 'P'
        #game.printBoard()
        
    def alive(self, game, player, monsters):
        if self.health > 0:
            return 1
        else:
            game.board[self.pos[0]][self.pos[1]] = ' '
            print("Oh no you died!!!")
            game.printBoard(player, monsters)
            return 0
   
print("Monster Spill")
print("Målet er å drepe monstret før han dreper deg")
print("Du har muligheten å enten flytte (m), angrepe (a) eller bytte våpen (e) når det er turen din")
print("for å flytte seg rundt bruker mann wasd knappene etter du har skrevett inn 'a'\n")    
        
        
monster = Monster(4, 0)
player = Player(4, 9)
game = Game(10, 10, player, monster)
game.init([monster], player)
cont = 1
while cont: 
    game.G_round(player, [monster])
    if not(player.alive(game, player, [monster])) or not(monster.alive(game, player, [monster])):
        cont = 0