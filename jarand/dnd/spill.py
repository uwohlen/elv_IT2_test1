mobs = []
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

        print("you draw your bow")

        damage_dealt = self.ranged_damage

        print(f"and deal {damage_dealt} damage")
        return damage_dealt
    def meele_attack(self):
      print("b")

    def health_check(self):
      
      print(f"remaning health for {self.name} for {self.health}")

      if self.health <= 0:
        self.dead = True
        print("the blow was too big, you died :(")
        return self.dead

class Mobs(Unit):
    def __init__(self, name, health, base_attack, speed, dead:bool):
        super().__init__(name, health, base_attack, speed, dead)
    
    def mob_damage(self):
      global player_damage

      player_damage=self.base_attack
      return player_damage
    
    def health_check(self):

      print(f"remaning health for {self.name} for {self.health}")

      if self.health <= 0:
        self.dead = True
        print(f"the {self.name} died")
        mobs.pop(0)
        print(mobs[0].name)
       




player1 = Player("player1",10, 4, 3, False, 4, 4, 4)
slime = Mobs("slime", 2, 1, 4, False)
blue_slime1 = Mobs("blue slime", 2, 1, 4, False)
blue_slime2 = Mobs("blue slime", 2, 1, 4, False)
unit = Unit("unit",1,2,3,False)

mobs = [slime, blue_slime1, blue_slime2]

while (True):
  if len(mobs) == 0:
    print("you win!")
    break
  
  print(f"you meet {mobs[0].name}, ranged for ranged attack meele for meele attack")
  action = input("what to do? ")
  
  player1.health_check()
  if player1.dead == True:
    break
  
  #player turn
  if (action == "ranged"):
    player1.ranged_attack() 
    mobs[0].damage(damage_dealt)

  elif (action == "meele"):
    print("pog")

  else:
    print("bruh")
    break
  
  player1.health_check()
  if player1.dead == True:
    break
  
  mobs[0].health_check()
  
  #enemy turn
  mobs[0].mob_damage()
  player1.damage(player_damage)
