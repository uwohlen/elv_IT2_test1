import item, random, ioutil

class Weapon(item.Item):
    def __init__(self, name, damage, damage_variance, hit_probability, range, projectile = None):
        super().__init__(name)
        self.weapon = True

        self.damage = damage
        self.damage_variance = damage_variance
        self.hit_probability = hit_probability
        self.range = range
        self.projectile = projectile

    def attack(self, attacker, defender, distance):
        ioutil.slow(f"{attacker.name} bruker {self.name} på {defender.name}")
        if self.projectile != None:
            if not attacker.remove_single_item(self.projectile, True):
                ioutil.slow(f"{attacker.name} mangler {self.projectile.name}")
                return
        if distance > self.range:
            ioutil.slow(f"{attacker.name} bommer, avstanden er for stor")
            return
        if random.random() <= self.hit_probability:
            ioutil.slow(f"{attacker.name} treffer")
            damage = max(self.damage + random.randint(0, self.damage_variance*2) - self.damage_variance, 1) * attacker.level
            defender.change_hp(-damage)
            return
        ioutil.slow(f"{attacker.name} bommer")

    def print_info(self):
        ioutil.slow(f"Info om {self.name}")
        ioutil.slow(f"Skade: {self.damage} (avhenger også av ditt nivå)")
        ioutil.slow(f"Sjanse for å treffe: {self.hit_probability*100}%")
        ioutil.slow(f"Rekkevidde: {self.range} meter")
        if self.projectile != None:
            ioutil.slow(f"Du trenger {self.projectile.name} for å kunne bruke {self.name}")

class Projectile(item.Item):
    def __init__(self, name, max_stack, weapon_name):
        super().__init__(name)
        self.stackable = True
        self.max_stack = max_stack
        self.weapon_name = weapon_name

    def print_info(self):
        ioutil.slow(f"Du trenger {self.name} for å kunne bruke {self.weapon_name}")

ARROW = Projectile("Pil", 8, "Bue")

FIST = Weapon("Knyttneve", 1, 1, 0.9, 0.7)
BROKEN_SWORD = Weapon("Ødelagt sverd", 3, 1, 0.75, 1)
SWORD = Weapon("Sverd", 5, 1, 0.7, 1.5)
WEAK_BOW = Weapon("Svak bue", 1, 0, 0.6, 8, ARROW)
BOW = Weapon("Bue", 3, 0, 0.7, 20, ARROW)

