import random
import time

class Monster:
    def __init__(self):
        self.navn = str
        self.helse = int
        self.styrke = int

    def monstre(self):
        monster_typer = {
            'Boros': [100000, 456760],
            'Dragen Eragon': [3000, 786],
            'Rotte': [60, 8],
            'Goblin': [250, 35],
        }
        self.navn = random.choice(list(monster_typer))
        stats = monster_typer.get(self.navn)
        self.helse = stats[0]
        self.styrke = stats[1]

class Spiller:
    def __init__(self):
        self.navn = str
        self.helse = 1000000
        self.styrke = 1000000000 

def introScene():
  directions = ["venstre","høyre","fram"]
  print("Hvilken vei tar du?")
  userInput = ""
  while userInput not in directions:
    print("Muligheter: venstre/høyre/fram")
    userInput = input()
    if userInput == "venstre":
      skikkelse() 
    elif userInput == "høyre":
      vill_mann()
    elif userInput == "fram":
      vill_mann()
    else: 
      print("Vennligst velg en av mulighetene.")

def vill_mann():
  print("Oisann, det viser seg at du gikk deg vill og endte opp på samme sted")
  time.sleep(1.5)
  introScene()

def skikkelse(): #VENSTRE valg
    directions = ["fram","tilbake"]
    print("Du ser en skummel skikkelse i mørket foran deg. Du blir redd. Hvilken vei går du?")
    userInput = ""
    while userInput not in directions:
        print("Options: fram/tilbake")
        userInput = input()
        if userInput == "fram":
            kamp() #
        elif userInput == "tilbake":
            introScene()
        else:
            print("Ikke et alternativ.")

def kamp():

    monster = Monster()
    monster.monstre()

    if monster.navn == ('Rotte', 'Goblin'):
        print(f'En {monster.navn} har dukket opp!')
    else:
        print(f'En {monster.navn} har dukket opp!')
    time.sleep(1)
    print(f' {monster.navn} har {monster.helse} HP, '
          f'og {monster.styrke} styrke')
    print('Monstre blir sinna og gjør seg klar for å slå tilbake!')
    while True:
        if monster.helse <= 0:
            print('Du har nedkjempet monsteret!')
            time.sleep(1)
            print("Du har vunnet One-Punch-Man simulator, Gratulerer!")
            del monster
            break
        print('Hva vil du gjøre?')
        print('Muligheter: Punch monster [punch]')
        user_input = input()
        if user_input == 'punch':
            sykdom = random.randint(1, 10)
            if sykdom == 1:
              print("Før du fikk Punchet så stivnet armen din, pustingen ble tung... du døde du av hjerteinfarkt")
              print("Game Over")
              break
            else:
              pass
            print('ONE PUNCH!!')
            monster.helse -= spiller.styrke
            spiller.helse -= monster.styrke
            if monster.helse <= 0:
                pass
            else:
              print(f'Monsteret har {monster.helse} HP igjen')
              print(f'Du har {spiller.helse} HP igjen')
        else:
          print("Ikke en mulighet")

print("Hei velkommen til One Punch Man simulator!")
time.sleep(1.5)
print("Etter å ha vært svak hele livet ditt velger du å trene, og etter at du har løpt 10km tatt 100 squats og 100 push ups så har du blitt sterk")
time.sleep(2)
print("Men plutselig befinner du deg fortapt i en skog")
time.sleep(2)
print("Du kan velge å gå i flere retninger for å komme deg ut")
time.sleep(2)
print("La oss starte med hva du heter: ")
navn = input()
spiller = Spiller()
spiller.navn = navn
print("Lykke til, " +navn+ ".")
introScene()