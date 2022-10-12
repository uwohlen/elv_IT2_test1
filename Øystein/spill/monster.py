import character, weapon, random, util, food

class Monster(character.Character):
    def __init__(self, max_hp, strength, rewards):
        super().__init__("Monster", max_hp)

        self.add_item(weapon.FIST(strength))
        self.rewards = rewards

    def attack(self, other):
        w = random.choice(self.all_weapons())
        w.attack(self, other)

    def reward(self):
        return util.random_choice(self.rewards)

MONSTER1 = Monster(5, 2, rewards=[(50, None), (50, food.APPLE)])
MONSTER2 = Monster(10, 1, rewards=[(50, None), (50, food.APPLE)])
RANDOM = [MONSTER1, MONSTER2]