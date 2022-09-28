import random as rnd
import numpy as np

buffer = list('|   ')

weapons = {
    "Sword": [3, 1, 1],
    "Bow": [1, 4, 10],
    "Throwing star": [2, 2, 5]
    # "weapon": [damage multiplier, 1 in x hit chance, range]
}

class Game():
    def __init__(self, Width, Height, Pxpos, Pypos):
        self.x = Height
        self.y = Width
        self.x += 1
        self.y += 1
        self.board = np.empty((self.x, self.y), dtype='str')
        self.Pxpos = Pxpos
        self.Pypos = Pypos
        
    def init(self, monster):
        self.board.fill(' ')
        self.board[4][0] = 'M'
        self.board[self.Pxpos][self.Pypos] = 'P'

    
    def printBoard(self):
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
        print('')

class Monster():
    
    def __init__(self):
        self.health = 150
        self.pos = [4, 0]
        
 
    def hit(self, amount):
        self.health -= amount
        
    def attack(self):
        return rnd.randint(0, 20)
    
class Player():
    
    def __init__(self, game):
        self.health = 100
        self.inventory = ["Sword", None, None, None]
        self.pos = [game.Pxpos, game.Pypos]
        
    def hit(self, amount):
        self.health -= amount
        
    def mrange(self, monster):
        dx = self.pos[0] - monster.pos[0]
        dy = self.pos[1] - monster.pos[1]
        return round(np.sqrt(dy ** 2 + dx ** 2), 2)
        
    def attack(self, monster):
        if self.mrange(monster) > weapons[self.inventory[0]][2]:
            print("You are too far away for this to be effective!!!")
            return
        amount = rnd.randint(0, 20)
        amount *= weapons[self.inventory[0]][0]
        if rnd.randint(1, weapons[self.inventory[0]][1]) != 1:
            print("Oh no you missed!!!")
            return
        monster.hit(amount)
        print(f"You did {amount} damage to the monster, he now has {monster.health} health!!!")
    
    def move(self, x, y, game):
        game.board[self.pos[0]][self.pos[1]] = ' '
        self.pos[0] += x
        self.pos[1] -= y
        game.board[self.pos[0]][self.pos[1]] = 'P'
        game.printBoard()
        
        
        
        
m = Monster() 
game = Game(5, 5, 2, 1)
p1 = Player(game)  
game.init(m)
game.printBoard()
p1.move(0, 0, game)
print(p1.mrange(m))
p1.attack(m)

    