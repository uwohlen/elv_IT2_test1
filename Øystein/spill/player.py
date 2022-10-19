import random, character, monster, ioutil, weapon

class Player(character.Character):
    def __init__(self, name):
        super().__init__(name, 10, 1, 4)

        self.backpack_items = []
        self.other_items = []
        self.items = self.backpack_items + self.other_items

        self.backpack_size = 10

        self.add_item(weapon.FIST)

    def add_item(self, item, backpack=False):
        if super().add_item(item, backpack):
            if backpack:
                ioutil.slow(f"Ny ting lagt i sekken til {self.name}: {item.name}")
            return
        ioutil.slow(f"Sekken er full")
        self.print_items()
        choice = ioutil.choice(["Ja", "Nei", f"Vil du bytte ut noe i sekken med {item.name}"])
        if choice:
            ioutil.slow(f"Hvilken ting vil du bytte ut? (1-{len(self.backpack_items)})")
            i = ioutil.range_input(1, len(self.backpack_items), is_float=False)
            self.remove_item(i, True)
            self.add_item(item, True)

    def remove_item(self, i, backpack=False):
        if backpack:
            item = self.backpack_items.pop(i)
            ioutil.slow(f"{item.name} fjernet fra sekken til {self.name}")
        else:
            self.other_items.pop(i)
        self.items = self.backpack_items + self.other_items

    def attack(self, other, distance):
        ioutil.slow(f"Avstand: {distance} meter")
        ioutil.slow(f"Du kan bevege deg før du angriper")
        distance = self.walk(distance)
        all_weapons = self.all_weapons()
        weapon_names = [weapon.name for weapon in all_weapons]

        while True:
            i = ioutil.choice(["Beveg deg"] + weapon_names, "Hvilket våpen bruker du?")
            if i == 0:
                return self.walk(distance, False)
            all_weapons[i-1].print_info()
            choice = ioutil.choice(["Bruk våpenet", "Bruk et annet våpen"])
            if choice == 0:
                all_weapons[i-1].attack(self, other, distance)
                break

        return distance

    def walk(self, distance, nothing_option=True):
        choices = ["Gå nærmere", "Gå lengre unna"]
        if nothing_option:
            choices.append("Bli stående")
        choice = ioutil.choice(choices)
        if choice == 0:
            ioutil.slow("Hvor mye nærmere vil du gå?")
            end = min(self.walk_speed, distance-0.5)
            distance -= ioutil.range_input(0, end, f"Antall meter (0-{end}): ")
        elif choice == 1:
            ioutil.slow("Hvor mye lengre unna vil du gå?")
            end = min(self.walk_speed, 20-distance)
            distance += ioutil.range_input(0, end, f"Antall meter (0-{end}): ")
        elif choice == 2:
            return distance
        distance = round(distance, 1)
        ioutil.slow(f"Ny avstand: {distance} meter")
        return distance

    def look_for_monster(self):
        combat = False
        monster_found = monster.spawn_monster(self.level)
        ioutil.slow(f"Du fant {monster_found.name}")
        monster_found.print_info()
        choice = ioutil.choice(["Angrip monsteret", "Unngå monsteret"])
        if choice == 0:
            ioutil.slow("Hvor nærme monsteret går du før du begynner å angripe?")
            ioutil.slow("(Nærmere -> Større risiko for å bli oppdaget)")
            desired_distance = ioutil.range_input(0.5, 20, "Antall meter (0.5 - 20): ")
            distance = 20
            while desired_distance < distance:
                if random.random() > 0.03:
                    distance -= 1
                else:
                    ioutil.slow("Monsteret oppdaget deg")
                    character.combat(monster_found, self, distance)
                    combat = True
                    return
            if not combat:
                character.combat(self, monster_found, desired_distance)
                combat = True
        elif choice == 1:
            choice = ioutil.random_choice([90, 10])
            if choice == 0:
                ioutil.slow("Du kom deg unna monsteret")
            elif choice == 1:
                ioutil.slow("Monsteret oppdaget deg")
                character.combat(monster_found, self, random.random()*9 + 1)
                combat = True
        if combat and not self.dead:
            self.loot_monster(monster_found)

    def loot_monster(self, dead_monster):
        choice = ioutil.choice(["Se etter ting", "Gå bort"], "Vil du se i tingene til monsteret?")
        if choice == 1:
            return
        if len(dead_monster.backpack_items) == 0:
            ioutil.slow(f"{dead_monster.name} har ingenting")
            return
        while True:
            ioutil.slow(f"Tingene til {dead_monster.name}")
            for i, item in enumerate(dead_monster.backpack_items):
                if item.stackable:
                    ioutil.slow(f"{i+1}: {item.name} x{self.backpack_stacks[i]}")
                else:
                    ioutil.slow(f"{i+1}: {item.name}")
            ioutil.slow(f"Hvilken ting velger du (1-{len(dead_monster.backpack_items)}, eller gå videre (0)?")
            i = ioutil.range_input(0, len(dead_monster.backpack_items), "> ", False)
            if i == 0:
                return
            i -= 1
            remove, add = self.print_item(dead_monster.backpack_items[i])
            if add:
                self.add_item(dead_monster.backpack_items[i], True)
            if remove:
                dead_monster.remove_item(i, True)

    def open_backpack(self):
        while True:
            self.print_items()
            if len(self.backpack_items) == 0:
                return
            choice = ioutil.choice(["Lukk sekken", "Velg ting"])
            if choice == 0:
                ioutil.slow("Sekken er lukket")
                return
            elif choice == 1:
                ioutil.slow(f"Hvilken ting velger du? (1-{len(self.backpack_items)})")
                i = ioutil.range_input(1, len(self.backpack_items), "> ", False)-1
                remove, _ = self.print_item(self.backpack_items[i], True)
                if remove:
                    self.remove_item(i, True)

    def print_item(self, item, in_backpack = False):
        item.print_info()
        choices = ["Bruk"] if item.consumable else []
        if in_backpack:
            choices += ["Kast", "Ingenting"]
        else:
            choices += ["Ta den med", "La den ligge"]
        choice = ioutil.choice(choices, f"Hva vil du gjøre med {item.name}?")
        if item.consumable:
            choice -= 1
        remove = False
        add = False
        if choice == -1:
            item.consume(self)
            remove = True
        elif choice == 0 and in_backpack:
            remove = True
        elif choice == 0 and not in_backpack:
            remove = True
            add = True
        return remove, add

    def print_items(self):
        if len(self.backpack_items) == 0:
            ioutil.slow("Sekken er tom")
            return
        ioutil.slow("Ting i sekken:")
        for i, item in enumerate(self.backpack_items):
            if item.stackable:
                ioutil.slow(f"{i+1}: {item.name} x{self.backpack_stacks[i]}")
            else:
                ioutil.slow(f"{i+1}: {item.name}")