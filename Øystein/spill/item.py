import ioutil

class Item:
    def __init__(self, name):
        self.name = name
        self.consumable = False
        self.weapon = False
        self.stackable = False
        self.max_stack_size = 10

    def print_info(self):
        ioutil.slow("Denne tingen gjør ingenting")

    def consume(self, character):
        pass