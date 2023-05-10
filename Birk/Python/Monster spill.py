## Importerer relevante kodebiblioteker

import os, sys, time, random

## Treg printing

def slow_type(t):
    typing_speed = 150 # printe hastighet i ord per minutt
    for l in t:
        sys.stdout.write(l) # skriver ut en bokstav om gangen
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed) # pause mellom hvert tegn

## Spiller klasse

class Player:
    # player egenskaper
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

    def __str__(self):
        return f"{self.navn} Level = {self.level} Influence = {self.influence} Strength = {self.strength} Defense = {self.defense} Speed = {self.speed} Luck = {self.luck} Red talent fragments = {self.red} Blue talent fragments = {self.blue} Green talent fragments = {self.green}"

# test player
birk = Player("Birk", 1, 30, 15, 5, 10, 9, 0, 0, 0)

## Monster klasse

class Monster:
    # monster egenskaper
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

# test monster    
kraftig_kjempe = Monster("Kraftig kjempe", 1, 20, 9, 10, 1, 3)

## Skade og blokkering kalkulator

def damage_calculator(strength, defense):
    return 2.8 ** (strength / defense) # regner ut skaden

def block_damage_calculator(strength, defense):
    return (2.8 ** (strength / defense)) * 0.25 # regner ut 25 prosent av skaden

## Kamp system

if birk.speed > kraftig_kjempe.speed: # sjekker hvem som starter
    turn = "Birk"
    
else:
    turn = "Enemy"

# test battle system
while birk.influence > 0 and kraftig_kjempe.influence > 0: # kjører så lenge begge har liv igjen
    enemy_action = None # resetter fiendens handling

    if turn == "Birk":
        print(f"[Liv igjen: {birk.influence}] \t [Fiendes liv igjen: {kraftig_kjempe.influence}] \n \n") # viser livet til spilleren og fienden
        slow_type("Det er din tur")
        player_action = input("\nHva vil du gjøre?\nAttack (a)\nBlock (b)") # spør spilleren hva han vil gjøre
        birk.influence = round(birk.influence) # runder av livet til spilleren

        if player_action == "a": # angriper fienden
            os.system('cls') # fjerner innholdet i terminalen
            slow_type(f"Du angriper {kraftig_kjempe.navn}")
            time.sleep(1) # venter 1 sekund
            
            if enemy_action == "b": # sjekker om fienden blokkerer
                slow_type(f"Du gjør {round(block_damage_calculator(birk.strength, kraftig_kjempe.defense))} skade") # viser skaden spilleren gjør
                kraftig_kjempe.influence -= round(block_damage_calculator(birk.strength, kraftig_kjempe.defense)) # trekker fra skaden fra fiendens liv
                slow_type(f"{kraftig_kjempe.navn} har {round(kraftig_kjempe.influence)} liv igjen") # viser fiendens liv
                time.sleep(2) # venter 2 sekunder
                turn = "Enemy" # endrer tur til fienden
                os.system('cls') # fjerner innholdet i terminalen

            else: # hvis fienden ikke blokkerer
                slow_type(f"\nDu gjør {round(damage_calculator(birk.strength, kraftig_kjempe.defense))} skade") # viser skaden spilleren gjør
                kraftig_kjempe.influence -= round(damage_calculator(birk.strength, kraftig_kjempe.defense)) # trekker fra skaden fra fiendens liv
                slow_type(f"\n{kraftig_kjempe.navn} har {round(kraftig_kjempe.influence)} liv igjen") # viser fiendens liv
                time.sleep(2) # venter 2 sekunder
                turn = "Enemy" # endrer tur til fienden
                os.system('cls') # fjerner innholdet i terminalen
        
        elif player_action == "b": # blokkerer angrepet til fienden
            os.system('cls') # fjerner innholdet i terminalen
            slow_type(f"\nDu gjør deg klar for angrepet til {kraftig_kjempe.navn}") # viser at spilleren blokkerer
            time.sleep(2) # venter 2 sekunder
            turn = "Enemy" # endrer tur til fienden
            os.system('cls') # fjerner innholdet i terminalen

        else:
            os.system('cls') # fjerner innholdet i terminalen
            slow_type(f"Skriv inn en gyldig handling") # viser at spilleren skrev inn en ugyldig handling
            time.sleep(2) # venter 2 sekunder
            os.system('cls') # fjerner innholdet i terminalen
    
    else: # hvis fienden starter
        print(f"[Liv igjen: {birk.influence}] \t [Liv igjen: {kraftig_kjempe.influence}] \n \n") # viser livet til spilleren og fienden
        slow_type(f"Det er {kraftig_kjempe.navn} sin tur") # viser at det er fiendens tur
        enemy_action = random.randint(1, 20) # velger en tilfeldig handling for fienden
        kraftig_kjempe.influence = round(kraftig_kjempe.influence) # runder av livet til fienden

        if enemy_action <= 15: # angriper spilleren
            slow_type(f"\n{kraftig_kjempe.navn} angriper deg") # viser at fienden angriper
            
            if player_action == "b": # sjekker om spilleren blokkerer
                slow_type(f"\n{kraftig_kjempe.navn} gjør {round(block_damage_calculator(kraftig_kjempe.strength, birk.defense))} skade på deg") # viser skaden fienden gjør
                birk.influence -= round(block_damage_calculator(kraftig_kjempe.strength, birk.defense)) # trekker fra skaden fra spillerens liv
                slow_type(f"\nDu har {round(birk.influence)} liv igjen") # viser spillerens liv
                time.sleep(2) # venter 2 sekunder
                turn = "Birk" # endrer tur til spilleren
                os.system('cls') # fjerner innholdet i terminalen
            
            else: # hvis spilleren ikke blokkerer
                slow_type(f"\n{kraftig_kjempe.navn} gjør {round(damage_calculator(kraftig_kjempe.strength, birk.defense))} skade på deg") # viser skaden fienden gjør
                birk.influence -= round(damage_calculator(kraftig_kjempe.strength, birk.defense)) # trekker fra skaden fra spillerens liv
                slow_type(f"\nDu har {round(birk.influence)} liv igjen") # viser spillerens liv
                time.sleep(2) # venter 2 sekunder
                turn = "Birk" # endrer tur til spilleren
                os.system('cls') # fjerner innholdet i terminalen
        
        elif enemy_action > 15: # blokkerer angrepet til spilleren
            enemy_action = "b" # endrer handlingen til fienden til å blokkere
            slow_type(f"\n{kraftig_kjempe.navn} gjør seg klar for angrepet ditt") # viser at fienden blokkerer
            time.sleep(2) # venter 2 sekunder
            turn = "Birk" # endrer tur til spilleren
            os.system('cls') # fjerner innholdet i terminalen
            
        elif enemy_action == 20:
            slow_type(f"\n{kraftig_kjempe.navn} har tatt en overdose av et hemmelig stoff") # viser at fienden har tatt en overdose
            slow_type(f"\n{kraftig_kjempe.navn} har dødd") # viser at fienden har dødd
            kraftig_kjempe.influence = 0 # setter livet til fienden til 0
            time.sleep(2) # venter 2 sekunder
            turn = "Birk" # endrer tur til spilleren
            os.system('cls') # fjerner innholdet i terminalen
