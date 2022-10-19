import ioutil, math

class Character:
    def __init__(self, name, start_hp, level, walk_speed):
        self.name = name

        self.items = []
        self.backpack_items = []
        self.other_items = []
        self.backpack_size = 10
        self.other_stacks = []
        self.backpack_stacks = []

        self.start_hp = start_hp
        self.max_hp = start_hp
        self.hp = self.max_hp
        self.hp_increase = 1.3

        self.dead = False

        self.level = level
        self.walk_speed = walk_speed
        self.xp = 0

    def add_item(self, item, backpack=False):
        if backpack:
            if item.stackable:
                for i, other_item in enumerate(self.backpack_items):
                    if item == other_item and self.backpack_stacks[i] < item.max_stack_size:
                        self.backpack_stacks[i] += 1
                        return True
            if len(self.backpack_items)-1 >= self.backpack_size:
                return False
            self.backpack_items.append(item)
            self.backpack_stacks.append(1)
        else:
            if item.stackable:
                for i, other_item in enumerate(self.backpack_items):
                    if item == other_item and self.backpack_stacks[i] < item.max_stack_size:
                        self.backpack_stacks[i] += 1
                        return True
            self.other_items.append(item)
            self.backpack_stacks.append(1)
        self.items = self.backpack_items + self.other_items
        return True

    def remove_item(self, i, backpack=False):
        if backpack:
            item = self.backpack_items[i]
            if item.stackable and self.backpack_stacks[i] > 1:
                self.backpack_stacks[i] -= 1
            else:
                self.backpack_items.pop(i)
                self.backpack_stacks.pop(i)
        else:
            item = self.other_items[i]
            if item.stackable and self.other_stacks[i] > 1:
                self.other_stacks[i] -= 1
            else:
                self.other_items.pop(i)
                self.other_stacks.pop(i)
        self.items = self.backpack_items + self.other_items

    def remove_single_item(self, item, backpack=False):
        if backpack:
            for i in range(len(self.backpack_items)-1, -1, -1):
                if self.backpack_items[i] == item:
                    self.backpack_stacks[i] -= 1
                    if self.backpack_stacks[i] == 0:
                        self.backpack_items.pop(i)
                        self.backpack_stacks.pop(i)
                    return True
        else:
            for i in range(len(self.other_items)-1, -1, -1):
                if self.other_items[i] == item:
                    self.other_stacks[i] -= 1
                    if self.other_stacks[i] == 0:
                        self.other_items.pop(i)
                        self.other_stacks.pop(i)
                    return True
        return False

    def change_hp(self, delta):
        self.hp = min(self.hp + delta, self.max_hp)
        ioutil.slow(f"HP til {self.name}: {self.hp-delta} -> {self.hp}")
        if self.hp <= 0:
            self.dead = True
            ioutil.slow(f"{self.name} er død")

    def all_weapons(self):
        weapons = []
        for item in self.items:
            if item.weapon:
                weapons.append(item)
        return weapons

    def add_xp(self, opponent):
        self.xp += opponent.level
        old_level = self.level
        while self.xp >= self.level * 2:
            self.xp -= self.level * 2
            self.set_level(self.level + 1, True)

    def set_level(self, level, print_changes=False):
        oldlevel = self.level
        self.level = level
        oldhp = self.max_hp
        self.max_hp = math.ceil(self.start_hp * (self.hp_increase ** (level - 1)))
        if print_changes:
            ioutil.slow(f"{self.name} har gått opp i nivå")
            ioutil.slow(f"Nivå: {oldlevel} -> {self.level}")
            ioutil.slow(f"HP: {oldhp} -> {self.max_hp}")

    def move(self, distance, delta):
        delta = round(max(delta, 0.5-distance), 1)
        if delta > 0:
            ioutil.slow(f"{self.name} beveger seg {delta} meter lengre unna")
        elif delta < 0:
            ioutil.slow(f"{self.name} beveger seg {-delta} meter nærmere")
        else:
            return distance
        ioutil.slow(f"Avstanden er nå {distance+delta} meter")
        return distance+delta

    def print_info(self):
        ioutil.slow(f"Info om {self.name}")
        ioutil.slow(f"Nivå: {self.level}")
        ioutil.slow(f"HP: {self.hp}")
        ioutil.slow(f"Gangfart: {self.walk_speed}")
        ioutil.slow(f"Våpen: {', '.join([w.name for w in self.all_weapons()])}")

    def attack(self, other):
        pass

def combat(p1, p2, distance):
    while True:
        distance = p1.attack(p2, distance)
        if p2.dead:
            p1.add_xp(p2)
            p1.hp = p1.max_hp
            return
        distance = p2.attack(p1, distance)
        if p1.dead:
            p2.add_xp(p1)
            p2.hp = p2.max_hp
            return