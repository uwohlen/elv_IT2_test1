import util, food, random

class Character:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.print = False
        self.energy = 100

    def add_item(self, item):
        self.items.append(item)
        if self.print:
            util.slow(f"Ny ting lagt i sekken til {self.name}: {item.name}")

    def change_energy(self, delta):
        self.energy += delta
        if self.print:
            util.slow(f"Energi til {self.name}: {self.energy-delta} -> {self.energy}")

class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.print = True

    def look_for_food(self):
        choice = util.random_choice([70, 30])
        if choice == 0:
            food_found = util.random_choice(food.RANDOM)
            util.slow(f"Du fant {food_found.name}")
            choice = util.choice(["Ingenting", "Ta med maten"])
            if choice == 0:
                util.slow("Maten blir liggende")
            elif choice == 1:
                self.add_item(food_found)
        elif choice == 1:
            util.slow("Du fant ikke mat")

        self.change_energy(-(8 + random.randint(-5, 5)))

    def open_backpack(self):
        self.print_items()
        while True:
            choice = util.choice(["Lukk sekken", "Informasjon om ting", "Bruk ting", "Kast ting"])
            if choice == 0:
                util.slow("Sekken er lukket")
                return
            elif choice == 1:
                util.slow("Hvilken ting vil du ha informasjon om?")
                i = int(util.slow_input("> "))-1
                self.items[i].print_info()
            elif choice == 2:
                util.slow("Hvilken ting vil du bruke?")
                i = int(util.slow_input("> "))-1
                item = self.items[i]
                if not item.consumable:
                    util.slow(f"{item.name} kan ikke brukes")
                else:
                    item.consume()
            elif choice == 3:
                util.slow("Hvilken ting vil du kaste?")
                i = int(util.slow_input("> "))-1
                item = self.items.pop(i)
                util.slow(f"{item.name} er fjernet fra sekken")
                self.print_items()

    def print_items(self):
        util.slow("Ting i sekken:")
        for i, item in enumerate(self.items):
            util.slow(f"{i+1}: {item.name}")

    def print_status(self):
        util.slow(f"Energi: {self.energy}")