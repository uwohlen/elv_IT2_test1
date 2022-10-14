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
    
birk = Player("Birk", 1, 9, 15, 5, 10, 9, 0, 0, 0)
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
    
kraftig_kjempe = Monster("Kraftig kjempe", 1, 20, 9, 10, 1, 3)

print(kraftig_kjempe)

def damage_calculator(x, y):
    return 2.8 ** (x / y)

print(damage_calculator(birk.strength, kraftig_kjempe.defense))

battle = False

while battle == True:
    birk_turn = False
    kraftig_kjempe_turn = False
    print("Du sloss nå mot", kraftig_kjempe.navn)
    if birk.speed > kraftig_kjempe.speed:
        birk_tur = True
    else:
        kraftig_kjempe_tur = True
    
        while birk_turn == True:
            print("Det er din tur")
            action = print(input("Hva vil du gjøre? (a = attack, b = block)"))
            
            if action.casefold() == "a":
                print()
        
