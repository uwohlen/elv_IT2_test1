import item, util

class Food(item.Item):
    def __init__(self, name, energy, needs_to_be_cooked):
        super().__init__(name)
        self.consumable = True

        self.energy = energy
        self.needs_to_be_cooked = needs_to_be_cooked
        self.cooked = False

    def print_info(self):
        util.slow(f"{self.name} gir deg {self.energy} energi")

    def on_consume(self, character):
        util.slow(f"Du spiser {self.name}")
        character.change_energy(self.energy)

APPLE = Food("Eple", 15, False)
MONSTER_MEAT = Food("Monsterkjøtt", 90, True)
RASPBERRY = Food("Bringebær", 10, False)
STRAWBERRY = Food("Jordbær", 10, False)
BLUEBERRY = Food("Blåbær", 10, False)

RANDOM =        [
    (20, APPLE), 
    (2, MONSTER_MEAT), 
    (10, RASPBERRY), 
    (10, STRAWBERRY), 
    (10, BLUEBERRY)
    ]
