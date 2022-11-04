from mimetypes import init
import random
import os
import sys, time
from typing import Type

#termcolor
#playsoundxxxxx

def type(t):
    typing_speed = 500 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)


class Player:
    def __init__(self,name,health,strength,wallet = 0):
        self.name=name
        self.health=health
        self.strength=strength
        self.wallet=wallet



class Monster:
    def __init__(self):
        self.name=str
        self.health=int
        self.strength=int
        self.reward=int

    def spawn(self):
        monster_dict= {
            'Demon':[100,15,10],
            'Goblin':[50,10,5],
            'Devil':[200,20,40]
        }
        self.name=random.choice(list(monster_dict))
        ferdigheter=monster_dict.get(self.name)
        self.health=ferdigheter[0]
        self.strength=ferdigheter[1]
        self.reward=ferdigheter[2]



def kamp():

    monster=Monster()
    monster.spawn()
    type(f"Du møter på {monster.name} \nMonsteret har {monster.health}hp\n")
    while True:
        if monster.health <= 0:
            type("Monsteret har blitt bekjempet\n")
            spiller.wallet += monster.reward
            type(f'Du har tjent {monster.reward}\n' )
            type(f'Nå har du {spiller.wallet} kr\n')
            break
        elif spiller.health <= 0:
            type("Du døde \n")
            type("Du mistet alle pengene dine\n")
            type("Du vil nå respawne\n")
            spiller.wallet = 0
            spiller.health=100
            break
            
        type("Hva vil du gjøre\n")
        type("Slåss[fight] eller løpe bort[run]\n")
        bruker_input=input(":")
        if bruker_input == "fight":
            type("Du slo monsteret\n")
            monster.health -= spiller.strength
            spiller.health -= monster.strength
            if monster.health<=0:
                pass
            else:
                type(f'Du har {spiller.health}hp\nMonsteret har {monster.health} hp igjen\n')

        elif bruker_input == "run":
            type("Du rømte fra monsteret, du får ingenting i premie\n")
            break
        else:
            type("Velg et ordentlig alternativ\n")

def butikk():
    type("Velkommen til butikken\n Her får du kjøpt våpen og drikker\n")
    type("Sting : 15kr (+30hp,+15styrke)")
    type("\nKebab : 30kr (+50hp)")
    type("Hva vil du ha\n")
    type("[sting], [kebab], [tilbake]")
    while True:
        valg=input(":")
        if valg=="sting":
            if spiller.wallet>=15:
                spiller.wallet -= 15
                type("Du kjøpte Sting\n")
                spiller.health+=30
                spiller.strength+=15
                type(f'Du har {spiller.health}hp og styrke {spiller.strength}')
                type(f'Du har {spiller.wallet}kr igjen')
            else:
                type("Du har ikke råd\n")
                pass
        elif valg=="kebab":
            if spiller.wallet >=50:
                spiller.wallet -=50
                type("Du kjøpte kebab\n")
                spiller.health +=50
                type(f'Du har {spiller.health}hp og styrke {spiller.strength}')
                type(f'Du har {spiller.wallet}kr igjen')
            else:
                type("Du har ikke råd\n")
                pass
        elif valg=="tilbake":
            break


def spill():
    type("Hva vil du gjøre? \n")
    type("Vil du utforske[utforske], sjekke lommene dine[inventory] eller kjøpe noe fra butikken[butikk]\n")
    user_choice= input(": ")
    valg=["utforske","inventory","butikk"]
    if user_choice=="utforske":
        type("Du tar en spaser tur\n")
        hendelse= random.randint(1,1) #Kan legge til flere hendelser
        if hendelse == 1:
            kamp()
    elif user_choice=="inventory":
        inventory()
    elif user_choice=="butikk":
        butikk()
    else:
        type("Skriv et gyldig valg\n")





type("Velkommen til spillet \n")
type("Hva heter du")
navn_input=input(": ")
spiller=Player(navn_input,100,50)

while (True):
    spill()

