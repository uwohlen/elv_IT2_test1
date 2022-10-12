class Unit:
  def __init__(self, name, health, base_attack, speed, dead:bool):
    self.name = name
    self.health = health
    self.base_attack = base_attack
    self.speed = speed
    self.dead = dead

  def damage(self, damage_taken):
    self.health = self.health - damage_taken

    

class Player(Unit):
    def __init__(self, name, health, base_attack, speed, dead:bool, armor, ranged, melee):
        super().__init__(name, health, base_attack, speed, dead)
        self.armor = armor
        self.ranged = ranged
        self.melee = melee
        self.ranged_damage = self.base_attack*self.ranged
        self.melee_damage = self.base_attack*self.melee
    
   

    def ranged_attack(self):
        global damage_dealt

        damage_dealt = self.ranged_damage

        return damage_dealt

class Mobs(Unit):
    def __init__(self, name, health, base_attack, speed, dead:bool):
        super().__init__(name, health, base_attack, speed, dead)
        

player1 = Player("player1",10, 4, 3, False, 4, 4, 4)
slime = Mobs("slime", 2, 1, 4, False)
unit = Unit("unit",1,2,3,False)



print(unit.name)
print(slime.name)
