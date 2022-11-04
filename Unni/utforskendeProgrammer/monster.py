from random import randint

class Monster:
    def __init__(self,navn,helse,styrke,svakhet):
        self.navn = navn
        self.helse = helse
        self.styrke = styrke
        self.svakhet = svakhet
        self.forfall = 10

    def sloss(self):
        self.helse = self.helse - self.forfall
    
    def oppStyrke(self,pluss):
        print("Mat, søvn og trening gjør underverker. Styrken øker.")
        self.styrke = self.styrke + pluss
        


monster1 = Monster("Gnarl",100,80,"Pixiedust")

class Spiller(Monster):
    def __init__(self,navn,helse,styrke, svakhet):
        super().__init__(navn,helse,styrke,svakhet)

spiller1 = Spiller("Hero",100,50,"Damsels in distress")


while (True):
    print()
    print(vars(spiller1))
    print("Mulige handlinger:")
    print("Gå en tur og se hva som hender (g)")
    print("Avslutt spillet (q)")
    svar = input("Hva vil du gjøre? ")

    if (svar == "q"):
        break
    elif (svar == "g"):
        hendelse = randint(1,3)
        if (hendelse == 1):
            spiller1.oppStyrke(10)
        elif (hendelse == 2):
            print("ikke ferdig, finn Pixiedust")
        else:
            print("ikke ferdig, sloss med monster1")


print("OK bye!")

"""
print(type(monster1))
print(vars(monster1))
print(type(spiller1))
print(vars(spiller1))
"""