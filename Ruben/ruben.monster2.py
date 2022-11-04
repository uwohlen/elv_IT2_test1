import random
import time

# Tekstbasert spill, spill mot computeren med forskjellige angrepsmetoder
# Angrip med «Light attack» og lad opp mana for å bruke sterkere angrep
# Den første som når 0 liv taper


# Variabler for spiller og computeren:
player_HP = 100
player_mana = 0
comp_HP = 70
comp_mana = 0


class Player(): 
    # Angrep for klassen:
    def light_atk(self):
        attack = random.randint(1, 20) # Gir en verdi mellom 1 og 20
        return attack 
   
    def heavy_attack(self):
        heavy_atk = random.randint(22, 42)
        return heavy_atk
   
    def heal(self):
        healing = random.randint(6, 30)
        return healing


# Hvem som starter:
def first_go(): 
    go = random.randint(0, 1)
    if go == 0:
        return 'Comp'
    else:
        return name


print(f"This is a turn-based RNG game where you battle the almighty!")
time.sleep(2) # Forsinker output med 2 sekunder
name = input("First, what is your name? ")
turn = first_go()


# To forskjellige objekter i Player()-klassen:
player = Player()
comp = Player()

# Variabler til computeren:
comp_attack_light = comp.light_atk()
comp_heavy_attack = comp.heavy_attack()
comp_healer = comp.heal()

comp_abilities = [comp_attack_light, comp_heavy_attack]


# Fortsetter så lenge spiller og computerens HP er over 0:
while player_HP > 0 and comp_HP > 0:
    print(f"\n{turn}'s turn")
    #DIN TUR
    if turn != 'Comp':
        action = int(input("What will you do?\n1) Light Attack\n2) Heavy Attack\n3) Heal\n"))
        # Når det er din tur, representerer «1» «2» og «3» angrep^
        if action == 1:
            player_light_attack = player.light_atk() # Lager en ny variabel returnert fra angrepet
            comp_HP = comp_HP - player_light_attack # Regner hvor ut mye liv motstander har igjen etter angrepet
            player_mana += 10 # Man får 10 mana hver gang man bruker «Light attack»
            time.sleep(1)
            print(f"\n{name} just did {player_light_attack} damage!")
            print(f"{name} now has {player_HP} health and {player_mana} mana")
            time.sleep(1)
            print(f"The computer now has {comp_HP} health and {comp_mana} mana")
            turn = 'Comp' # Nå er det computerens tur
        
        elif action == 2 and player_mana >= 20: # Fungerer bare hvis du har 20 eller mer mana
            player_heavy_attack = player.heavy_attack()
            comp_HP = comp_HP - player_heavy_attack
            player_mana -= 20 # Dette angrepet bruker 20 mana
            time.sleep(1)
            print(f"\n{name} just did {player_heavy_attack} damage!")
            print(f"{name} now has {player_HP} health and {player_mana} mana")
            time.sleep(1)
            print(f"The computer now has {comp_HP} health and {comp_mana} mana")
            turn = 'Comp'
        
        elif action == 3 and player_mana >= 15: # Fungerer bare med 15 mana eller mer
            player_heal = player.heal()
            player_HP += player_heal # Regner hvor mye livet ditt er helbredet
            player_mana -= 15 # 15 mana per bruk
            time.sleep(1)
            print(f"\n{name} just healed themselves for {player_heal}")
            turn = 'Comp'
        
        elif action == 2 or action == 3 and player_mana < 15:
            print(f"\n{name} you have {player_HP} health and {player_mana} mana")
            print(f"\n{name} your mana is too low, please choose 1) Light Attack: ")
        
        else:
            print(f"Please enter a correct action")
        
    # COMPUTER ACTION
    else:
        if comp_mana >= 20: # Når computeren har mer enn 20 mana, bruken den «Heavy attack»
            comp_heavy_attack = comp.heavy_attack()
            player_HP = player_HP - comp_heavy_attack
            comp_mana -= 20
            time.sleep(1)
            print(f"\nThe computer just did {comp_heavy_attack} damage")
            print(f"{name} now has {player_HP} health and {player_mana} mana")
            time.sleep(1)
            print(f"The computer now has {comp_HP} health and {comp_mana} mana")
            turn = name # Nå er det vår tur
        
        elif comp_HP < 25 and comp_mana >= 15: # Når computeren har mindre enn 25 liv, vil den begynne å helbrede
            comp_healing = comp.heal()
            comp_HP += comp_healing
            comp_mana -= 15
            time.sleep(1)
            print(f"\nThe comp has healed themselves for {comp_healing}")
            print(f"{name} now has {player_HP} health and {player_mana} mana")
            time.sleep(1)
            print(f"The computer now has {comp_HP} health and {comp_mana} mana")
            turn = name

        else:
            comp_norm_attack = comp.light_atk() # Hvis computeren ikke kan gjøre angrepene før, gjør den «Light attack»
            player_HP = player_HP - comp_norm_attack
            comp_mana += 10
            time.sleep(1)
            print(f"\nComp just did {comp_norm_attack} damage!")
            print(f"\n{name} now has {player_HP} health and {player_mana} mana")
            print(f"The computer now has {comp_HP} health and {comp_mana} mana")
            turn = name


# Hvis en spillers liv faller under eller blir 0, printer den vinneren:
if player_HP <= 0:
    print(f"\nComputer has won this round!")
elif comp_HP <= 0:
    print(f"\n{name} has won this round!")

