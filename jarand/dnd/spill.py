import random
mobs = []
class Unit:
  def __init__(self, name, health, base_attack, accuracy, dead:bool):
    self.name = name
    self.health = health
    self.base_attack = base_attack
    self.accuracy = accuracy
    self.dead = dead

  def damage(self, damage_taken):
    self.health = self.health - damage_taken
    

    

class Player(Unit):
  def __init__(self, name, health, base_attack, accuracy, dead:bool, armor, ranged, melee):
      super().__init__(name, health, base_attack, accuracy, dead)
      self.armor = armor
      self.ranged = ranged
      self.melee = melee
      self.ranged_damage = self.base_attack*self.ranged
      self.melee_damage = self.base_attack*self.melee
  
  

  def ranged_attack(self):
      global damage_dealt
      if self.accuracy+random.randint(0,50)>50:
        print("you draw your bow ", end="")

        damage_dealt = self.ranged_damage

        print(f"and deal {damage_dealt} damage")
      else:
        print("missed!")
        damage_dealt=0
      return damage_dealt

  def melee_attack(self):
    global damage_dealt
    if self.accuracy+random.randint(0,75)>50:
      print("you charge with your sword ", end="")

      damage_dealt = self.melee_damage

      print(f"and deal {damage_dealt} damage")
    else:
      print("missed!")
      damage_dealt=0
    return damage_dealt

  def health_check(self):

    if self.health <= 0:
      self.dead = True
      print("the blow was too big, you died :(")
      return self.dead


class Mobs(Unit):
    def __init__(self, name, health, base_attack, accuracy, dead:bool):
        super().__init__(name, health, base_attack, accuracy, dead)
    
    def mob_damage(self):
      global player_damage

      player_damage=self.base_attack
      print(f"{self.name} fling towards you dealing {player_damage} damage")
      return player_damage
    
    def health_check(self):

      print(f"remaning health for {self.name} for {self.health}")

      if self.health <= 0:
        self.dead = True
        print(f"the {self.name} died, ", end="")
        mobs.pop(0)
        if len(mobs) > 0:
          print(f"and {mobs[0].name} takes its place")



player1 = Player("player1",20, 4, 25, False, 4, 4, 2)
slime = Mobs("slime", 8, 1, 4, False)
blue_slime1 = Mobs("blue slime", 8, 2, 4, False)
blue_slime2 = Mobs("blue slime", 8, 2, 4, False)
monke = Mobs("monke", 25, 5, 4, False)
unit = Unit("unit",1,2,3,False)

mobs = [slime, blue_slime1, blue_slime2, monke]


while (True):
  
  print(f"{mobs[0].name} is in front of you, ranged for ranged attack melee for melee attack")
  action = input("what to do? ")
  
  #player turn
  if (action == "ranged"):
    player1.ranged_attack() 
    mobs[0].damage(damage_dealt)

  elif (action == "melee"):
    player1.melee_attack() 
    mobs[0].damage(damage_dealt)

  else:
    print("bruh")
    break
  
  player1.health_check()
  if player1.dead == True:
    break
  
  mobs[0].health_check()
  
  if len(mobs) == 0:
    print("you win!")
    break

  #enemy turn
  mobs[0].mob_damage()
  player1.damage(player_damage)

  player1.health_check()
  print(f"remaning health for {player1.name} for {player1.health}")
  if player1.dead == True:
    break
