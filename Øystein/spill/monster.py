import character, weapon, random, ioutil

class Monster(character.Character):
    def __init__(self, name, max_hp, walk_speed, items, min_level):
        super().__init__(name, max_hp, 1, walk_speed)

        self.add_item(weapon.FIST)
        for item in items:
            self.add_item(item, True)
        self.min_level = min_level

    def attack(self, other, distance):
        viable_weapons = []
        all_weapons = self.all_weapons()
        for w in all_weapons:
            if distance - self.walk_speed < w.range:
                viable_weapons.append(w)
        if len(viable_weapons) > 0:
            w = random.choice(viable_weapons)
            if distance > w.range:
                distance = self.move(distance, w.range-distance)
            else:
                distance = self.move(distance, min(self.walk_speed, w.range-distance))
            w.attack(self, other, distance)
        else:
            distance = self.move(distance, -self.walk_speed)
            distance = self.move(distance, -self.walk_speed)
        return distance

# TODO: Monsterne trenger nye navn
MONSTERS = [
    (10, Monster("Monster", 5, 2, [], 1)),
    (20, Monster("Sverdmonster", 4, 2, [weapon.BROKEN_SWORD], 2)),
    (40, Monster("Buemonster", 4, 4, [weapon.WEAK_BOW] + [weapon.ARROW]*5, 3)),
    (80, Monster("Sverdmonster", 7, 2, [weapon.SWORD], 4)),
    (160, Monster("Buemonster", 7, 4, [weapon.BOW] + [weapon.ARROW]*5, 5)),
    (500, Monster("Stort monster", 10, 4, [weapon.SWORD, weapon.BOW], 7))
]

def spawn_monster(level):
    monsters = []
    for monster in MONSTERS:
        if monster[1].min_level <= level:
            monster[1].set_level(max(level-random.randint(0, 2), 1))
            monster[1].hp = monster[1].max_hp
            monster[1].dead = False
            monsters.append(monster)
    return ioutil.random_choice(monsters)