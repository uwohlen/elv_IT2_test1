import util, monster

class Environment:
    def __init__(self, items, monsters):
        self.items = items
        self.monsters = monsters

    def spawn_monster(self):
        return util.random_choice(self.monsters)

START_ENVIRONMENT = Environment([], [(10, None), (40, monster.MONSTER1), (40, monster.MONSTER2)])