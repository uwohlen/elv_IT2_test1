import sys, time, random

def slow_type(t):
    typing_speed = 100 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)

class Player:
    def __init__(self, navn, level, influence, strength, defense, speed, luck, talent_fragments_red, talent_fragments_blue, talent_fragments_green):
        self.navn = navn
        self.level = level
        self.influence = influence
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.luck = luck
        self.red = talent_fragments_red
        self.blue = talent_fragments_blue
        self.green = talent_fragments_green
        
    def funksjon(self):
        print("Mitt navn er " + self.navn)
        
    def __str__(self):
        return f"{self.navn} Level = {self.level} Influence = {self.influence} Strength = {self.strength} Defense = {self.defense} Speed = {self.speed} Luck = {self.luck} Red talent fragments = {self.red} Blue talent fragments = {self.blue} Green talent fragments = {self.green}"
    
birk = Player("Birk", 1, 9, 11, 5, 10, 9, 0, 0, 0)
birk.funksjon()

birk.level = 1

print(birk)

class Monster:
    def __init__(self, navn, level, influence, strength, defense, speed, luck):
        self.navn = navn
        self.level = level
        self.influence = influence
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.luck = luck
        
    def __str__(self):
        return f"{self.navn} Level = {self.level} Influence = {self.influence} Strength = {self.strength} Defense = {self.defense} Speed = {self.speed} Luck = {self.luck}"
    
