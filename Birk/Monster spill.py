import os, sys, time, random

def slow_type(t):
    typing_speed = 150 #wpm
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
    
#Test player
birk = Player("Birk", 1, 30, 15, 5, 10, 9, 0, 0, 0)

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
    
#Test monster    
kraftig_kjempe = Monster("Kraftig kjempe", 1, 20, 9, 10, 1, 3)

def damage_calculator(x, y):
    return 2.8 ** (x / y)

def block_damage_calculator(x, y):
    return (2.8 ** (x / y)) * 0.25

if birk.speed > kraftig_kjempe.speed:
    turn = "Birk"
    
else:
    turn = "Enemy"

#Test battle system
while birk.influence > 0 and kraftig_kjempe.influence > 0:
    enemy_action = None

    if turn == "Birk":
        print(f"[Liv igjen: {birk.influence}] \t [Fiendes liv igjen: {kraftig_kjempe.influence}] \n \n")
        slow_type("Det er din tur")
        player_action = input("\nHva vil du gjøre?\nAttack (a)\nBlock (b)")
        birk.influence = round(birk.influence)

        if player_action == "a":
            os.system('cls')
            slow_type(f"Du angriper {kraftig_kjempe.navn}")
            time.sleep(1)
            
            if enemy_action == "b":
                slow_type(f"Du gjør {round(block_damage_calculator(birk.strength, kraftig_kjempe.defense))} skade")
                kraftig_kjempe.influence -= round(block_damage_calculator(birk.strength, kraftig_kjempe.defense))
                slow_type(f"{kraftig_kjempe.navn} har {round(kraftig_kjempe.influence)} liv igjen")
                time.sleep(2)
                turn = "Enemy"
                os.system('cls')

            else:
                slow_type(f"\nDu gjør {round(damage_calculator(birk.strength, kraftig_kjempe.defense))} skade")
                kraftig_kjempe.influence -= round(damage_calculator(birk.strength, kraftig_kjempe.defense))
                slow_type(f"\n{kraftig_kjempe.navn} har {round(kraftig_kjempe.influence)} liv igjen")
                time.sleep(2)
                turn = "Enemy"
                os.system('cls')
        
        elif player_action == "b":
            os.system('cls')
            slow_type(f"\nDu gjør deg klar for angrepet til {kraftig_kjempe.navn}")
            time.sleep(2)
            turn = "Enemy"
            os.system('cls')

        else:
            os.system('cls')
            slow_type(f"Skriv inn en gyldig handling")
            time.sleep(2)
            os.system('cls')
    
    else:
        print(f"[Liv igjen: {birk.influence}] \t [Liv igjen: {kraftig_kjempe.influence}] \n \n")
        slow_type(f"Det er {kraftig_kjempe.navn} sin tur")
        enemy_action = random.randint(1, 20)
        kraftig_kjempe.influence = round(kraftig_kjempe.influence)

        if enemy_action <= 15:
            slow_type(f"\n{kraftig_kjempe.navn} angriper deg")
            
            if player_action == "b":
                slow_type(f"\n{kraftig_kjempe.navn} gjør {round(block_damage_calculator(kraftig_kjempe.strength, birk.defense))} skade på deg")
                birk.influence -= round(block_damage_calculator(kraftig_kjempe.strength, birk.defense))
                slow_type(f"\nDu har {round(birk.influence)} liv igjen")
                time.sleep(2)
                turn = "Birk"
                os.system('cls')
            
            else:
                slow_type(f"\n{kraftig_kjempe.navn} gjør {round(damage_calculator(kraftig_kjempe.strength, birk.defense))} skade på deg")
                birk.influence -= round(damage_calculator(kraftig_kjempe.strength, birk.defense))
                slow_type(f"\nDu har {round(birk.influence)} liv igjen")
                time.sleep(2)
                turn = "Birk"
                os.system('cls')
        
        elif enemy_action > 15:
            enemy_action = "b"
            slow_type(f"\n{kraftig_kjempe.navn} gjør seg klar for angrepet ditt")
            time.sleep(2)
            turn = "Birk"
            os.system('cls')
            
        elif enemy_action == 20:
            slow_type(f"\n{kraftig_kjempe.navn} har tatt en overdose av et hemmelig stoff")
            slow_type(f"\n{kraftig_kjempe.navn} har dødd")
            kraftig_kjempe.influence = 0
            time.sleep(2)
            turn = "Birk"
            os.system('cls')

# Utvikle kamp system
# Lage bevegelse system
