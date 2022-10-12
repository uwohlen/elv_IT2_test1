import character, util, food, random, weapon

class Player(character.Character):
    def __init__(self, name):
        super().__init__(name, 10)

        self.backpack_items = []
        self.other_items = []
        self.items = self.backpack_items + self.other_items

        self.backpack_size = 10

        self.add_item(weapon.FIST(2))
        self.add_item(weapon.SWORD)

    def add_item(self, item, backpack=False):
        if backpack:
            if len(self.backpack_items) == self.backpack_size:
                util.slow(f"Sekken er full")
                return
            self.backpack_items.append(item)
            util.slow(f"Ny ting lagt i sekken til {self.name}: {item.name}")
        else:
            self.other_items.append(item)
        self.items = self.backpack_items + self.other_items

    def remove_item(self, i, backpack=False):
        if backpack:
            item = self.backpack_items.pop(i)
            util.slow(f"{item.name} fjernet fra sekken til {self.name}")
        else:
            self.other_items.pop(i)
        self.items = self.backpack_items + self.other_items

    def attack(self, other):
        all_weapons = self.all_weapons()
        weapon_names = [weapon.name for weapon in all_weapons]
        i = util.choice(weapon_names, "Hvilket våpen bruker du?")
        all_weapons[i].attack(self, other)

    def look_for_food(self):
        choice = util.random_choice([70, 30])
        if choice == 0:
            food_found = util.random_choice(food.RANDOM)
            util.slow(f"Du fant {food_found.name}")
            food_found.print_info()
            choice = util.choice(["Spis maten", "Ta med maten", "La maten ligge"])
            if choice == 0:
                food_found.consume(self)
            elif choice == 1:
                self.add_item(food_found, True)
            elif choice == 2:
                util.slow("Maten blir liggende")
        elif choice == 1:
            util.slow("Du fant ikke mat")

        self.change_energy(-(8 + random.randint(-5, 5)))

    def look_for_monster(self, env):
        monster = env.spawn_monster()
        if monster != None:
            util.slow(f"Du fant {monster.name}")
            choice = util.choice(["Angrip monsteret", "Løp bort"])
            if choice == 0:
                character.combat(self, monster)
                if self.dead:
                    return
                reward = monster.reward()
                if reward != None:
                    util.slow(f"Du fant en {reward.name}")
                    reward.print_info()
                    choice = util.choice(["Ta den med", "La den bli liggende"])
                    if choice == 0:
                        self.add_item(reward, True)
                    else:
                        util.slow(f"{reward.name} blir liggende")
            elif choice == 1:
                util.slow("Du kom deg unna monsteret")
        else:
            util.slow("Du fant ikke et monster")

    def open_backpack(self):
        while True:
            self.print_items()
            choice = util.choice(["Lukk sekken", "Velg ting"])
            if choice == 0:
                util.slow("Sekken er lukket")
                return
            elif choice == 1:
                util.slow(f"Hvilken ting velger du? (1-{len(self.items)})")
                i = int(util.slow_input("> "))-1
                self.backpack_items[i].print_info()
                choices = ["Bruk"] if self.items[i].consumable else []
                choice = util.choice(choices + ["Kast", "Ingenting"], f"Hva vil du gjøre med {self.items[i].name}?")
                if choice == 0 and self.items[i].consumable:
                    self.backpack_items[i].consume(self)
                    self.remove_item(i, True)
                elif choice == int(self.items[i].consumable):
                    self.remove_item(i, True)

    def print_items(self):
        if len(self.backpack_items) == 0:
            util.slow("Sekken er tom")
            return
        util.slow("Ting i sekken:")
        for i, item in enumerate(self.backpack_items):
            util.slow(f"{i+1}: {item.name}")

    