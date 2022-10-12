import util, food, random

class Character:
    def __init__(self, name, max_hp):
        self.name = name
        self.items = []
        self.energy = 100

        self.max_hp = max_hp
        self.hp = self.max_hp
        self.dead = False

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, i):
        self.items.pop(i)

    def change_energy(self, delta):
        self.energy = min(self.energy + delta, 100)
        util.slow(f"Energi til {self.name}: {self.energy-delta} -> {self.energy}")
        if self.energy <= 0:
            self.dead = True
            util.slow(f"{self.name} er død")

    def change_hp(self, delta):
        self.hp = min(self.hp + delta, self.max_hp)
        util.slow(f"HP til {self.name}: {self.hp-delta} -> {self.hp}")
        if self.hp <= 0:
            self.dead = True
            util.slow(f"{self.name} er død")

    def print_status(self):
        util.slow(f"Status til {self.name}")
        util.slow(f"Energi: {self.energy}%")
        util.slow(f"HP: {self.hp} (max: {self.max_hp})")

    def all_weapons(self):
        weapons = []
        for item in self.items:
            if item.weapon:
                weapons.append(item)
        return weapons

    def attack(self, other):
        pass

def combat(p1, p2):
    while True:
        p1.attack(p2)
        if p2.dead:
            return
        p2.attack(p1)
        if p1.dead:
            return