import util

class Item:
    def __init__(self, name):
        self.name = name
        self.consumable = False

    def print_info(self):
        util.slow("Denne tingen gjør ingenting")

    def on_consume(character):
        pass