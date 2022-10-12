import util

class Item:
    def __init__(self, name):
        self.name = name
        self.consumable = False
        self.weapon = False

    def print_info(self):
        util.slow("Denne tingen gjør ingenting")

    def consume(character):
        pass