import random

PIECES = [
    [[4, 5, 6, 8], [0, 1, 5, 9], [2, 4, 5, 6], [1, 5, 9, 10]]
    ]

class Game:
    def __init__(self, width, height):
        self.squares = [0 for i in range(width*height)]

        self.width = width
        self.height = height

        self.new_piece(True)

    def squares_filled(self):
        squares = self.squares.copy()

        for square in PIECES[self.current_piece][self.piece_rotation]:
            x = self.piece_x + square%4
            y = self.piece_y + square//4
            squares[y*self.width+x] = 1
        return squares

    def rotate_piece(self, delta):
        self.piece_rotation = (self.piece_rotation+delta)%4
        if self.collide():
            self.piece_rotation = (self.piece_rotation-delta)%4


    def move_piece(self, delta):
        self.piece_x += delta
        if self.collide():
            self.piece_x -= delta

    def drop(self):
        while not self.collide():
            self.piece_y += 1
        self.piece_y -= 1
        self.new_piece()

    def tick(self):
        self.piece_y += 1
        if self.collide():
            self.piece_y -= 1
            self.new_piece()

    def collide(self):
        for square in PIECES[self.current_piece][self.piece_rotation]:
            x = self.piece_x + square%4
            y = self.piece_y + square//4

            if x < 0 or x >= self.width:
                return True
            if y < 0 or y >= self.height:
                return True
            if self.squares[y*self.width+x]:
                return True
        return False

    def new_piece(self, first=False):
        if not first:
            for square in PIECES[self.current_piece][self.piece_rotation]:
                x = self.piece_x + square%4
                y = self.piece_y + square//4
                self.squares[y*self.width+x] = 1
            self.check_for_clear()

        self.current_piece = random.randint(0, len(PIECES)-1)
        self.piece_rotation = 0
        self.piece_x = self.width//2-2
        self.piece_y = 0
    
    def check_for_clear(self):
        for y in range(self.height-1, -1, -1):
            clear = True
            for x in range(self.width):
                if self.squares[y*self.width+x] == 0:
                    clear = False
            if clear:
                for yi in range(y, 0, -1):
                    for xi in range(self.width):
                        self.squares[yi*self.width+xi] = self.squares[(yi-1)*self.width+xi]