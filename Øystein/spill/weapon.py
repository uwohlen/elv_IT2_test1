import item, random, util

class Weapon(item.Item):
    def __init__(self, name, attack_name, damage, damage_variance, hit_probability):
        super().__init__(name)
        self.weapon = True

        self.attack_name = attack_name
        self.damage = damage
        self.damage_variance = damage_variance
        self.hit_probability = hit_probability

    def attack(self, attacker, defender):
        util.slow(f"{attacker.name} bruker {self.name} på {defender.name}")
        if random.random() <= self.hit_probability:
            util.slow(f"{attacker.name} treffer")
            damage = self.damage + random.randint(0, self.damage_variance*2) - self.damage_variance
            defender.change_hp(-damage)
        else:
            util.slow(f"{attacker.name} bommer")

FIST = lambda strength: Weapon("Knyttneve", "Slå", strength, 1, 0.9)
SWORD = Weapon("Sverd", "Slå", 3, 1, 0.75)