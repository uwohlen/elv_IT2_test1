import random 

print("Velkommen til dette spillet")
print("Maalet med spillet er å komme deg gjennom et hus")
print("I huset kan du finne vaapen, gjenstander, og monster :o")
print("For å bevege deg skriver du enten inn opp, ned, hoeyre, venstre")
print("Dersom du kommer i et rom med en gjenstand kan du skrive 'grip' for å plukke det opp eller bruke det")
print("I rom med monster foelger egen instruks")
navn_spiller = input("\nFoer du begynner må du skrive inn navnet ditt: ").capitalize()

class Monster: #lager en klasse for monsteret
    def __init__(self, navn:str="", hp:int = 0, skade_per_slag_maks:int = 0, liv:bool=True):
        self.navn = navn
        self.hp=hp
        self.skade_per_slag_maks=skade_per_slag_maks
        self.liv= liv

    def sjekkliv(self): #metode som sjekker om monsteret lever eller ikke
        if self.hp<=0:
            self.liv=False
            return True
        
    def gjooreSkade(self, Spiller): #metode som gjoer skade pa spilleren
        skade = random.randint(0, self.skade_per_slag_maks)
        Spiller.hp-=skade
        Spiller.sjekkliv()
        print(f"{navn_spiller} ble truffet av monsteret")
        print(f"{navn_spiller} mistet {skade} hp, så spilleren har nå {Spiller.hp} hp igjen!")

class Spiller: #klasse for spiller
    def __init__(self, navn:str, hp:int = 0, gjenstander:list = [], liv:bool=True):
        self.navn = navn
        self.hp = hp
        self.gjenstander = gjenstander
        self.liv = liv

    def sjekkliv(self): #sjekker om spilleren lever
        if self.hp<=0:
            self.liv=False
            print(f"Du tapte kampen og doede, rip /: Men du kan proeve igjen")
            igjen = input("Ja eller Nei?: ").lower().replace(" ", "")
            if igjen == "ja":
                kjoor()
                

            else: 
                print("too bad /:")
                exit()

    def spillerPotionofhealing(self): #metode for naar spilleren drikker Potion of Healing
        self.hp*=2 

    def printEgenskap(self): #metode som printer ut hvilke vaapen og skaden det gjoer
        tekst=""
        for i in self.gjenstander:
            tekst+=f"\nGjenstanden {i.navn} gjoer {i.skade} skade"
        print(tekst)

    def felle(self): #metode for naar spilleren traakker i en felle
        spiller.hp /= 2
        print(f'{navn_spiller} har naa {spiller.hp} liv')


class Vaapen(): #metode for vaapen
    def __init__(self, navn, skade):
        self.navn=navn
        self.skade=skade

class Gjenstand(): #klasse for gjenstand. Brukes for Potion of Healing
    def __init__(self,navn):
        self.navn=navn

class Rom: #klasse for rommet
    def __init__ (self, romnummer):
        self.romnummer = romnummer

#setter startverdier for spiller og setter opp monstere uten verdier.
#Dette blir satt opp naar programmet starter
start_hp_spiller = 100
spiller = Spiller(navn_spiller, start_hp_spiller,[Vaapen("knyttneve", 20)])
monster1 = Monster()
monster2 = Monster()
   
#lager en tom liste for oppsettet til romfordelingen
rom_liste = [[],[],[]]
rad_nr=0
kolonne_nr=0

#fordeler rommene gjennom en while loekke
tall=1
for i in range(3):
    rom_liste.append
    for j in range(3):
        rom = "rom"
        rom += str(tall)
        rom = Rom(tall)
        rom_liste[i].append(rom)
        tall+=1

"""
#romplassering
    |  [2][0] nr=7 |  [2][1] nr=8 |  [2][2] nr=9 |
    |  [1][0] nr=4 |  [1][1] nr=5 |  [1][2] nr=6 |
    |  [0][0] nr=1 |  [0][1] nr=2 |  [0][2] nr=3 |  
"""
naa_rom = rom_liste[0][0]
valg_muligheter=[]


"""
funksjon for aa sette startverdier
dersom spilleren doer, skal:
alle monstrene resettes
spilleren skal starte paa starten
rommene skal tilbakestilles
spilleren skal faa fullt hp og vaapnene nullstilles
"""
def settStartverdier():
    global naa_rom
    #lager monstere
    monster1 = Monster("Peder", 50, 40)
    monster2 = Monster("morbius", 169, 60)

    #legger til egenskaper ved de forskjellige rommene
    rom_liste[0][0].kiste=True
    rom_liste[0][1].felle=True
    rom_liste[0][2].gjenstand=Vaapen("sverd",40)
    rom_liste[1][0].monster=monster1
    rom_liste[1][1].gjenstand=Vaapen("tazer",50)
    rom_liste[2][0].gjenstand = Gjenstand("potion of healing")
    rom_liste[2][2].monster = monster2

    spiller.hp = start_hp_spiller
    spiller.gjenstander = [Vaapen("knyttneve", 20)]
    naa_rom = rom_liste[0][0]

#funksjon for aa printe ut mulige retninger spilleren kan gaa. Tar hensyn til "border" til huset. 
def finnretning():
    mulige_retninger = f"{navn_spiller} kan bevege deg "
    global rad_nr, kolonne_nr
    for i in range(3):
        for j in range(3):
            if naa_rom == rom_liste[i][j]:
                rad_nr = i 
                kolonne_nr = j
                break
   
    if (rad_nr == 0) or (rad_nr== 1):
        mulige_retninger+="opp"
        valg_muligheter.append("opp")
    if kolonne_nr<2:
        if "opp" in mulige_retninger:
            mulige_retninger+=", "
        mulige_retninger+="til hoeyre"
        valg_muligheter.append("hoeyre")
    if kolonne_nr > 0:
        if "hoeyre" in mulige_retninger or "opp" in mulige_retninger:
            mulige_retninger+=", "
        mulige_retninger+="til venstre"
        valg_muligheter.append("venstre")

    print(mulige_retninger)
    

#leter etter objekter i rommet
def finnVariabel():
    liste=dir(naa_rom)
    for i in liste:
        if "_" not in i and i != "romnummer":
            verdi = i
            return verdi

#funksjon for aa plukke opp en gjenstand
def plukkOppGjenstand():
    if finnVariabel()=="gjenstand":
        spiller.gjenstander.append(naa_rom.gjenstand)
        print(f"{naa_rom.gjenstand.navn} er plukket opp")

#funksjon for aa aapne en kiste 
def aapneKiste():
    liste = [Gjenstand("potion of healing"),Monster("Peder", 50, 40)]
    gjenstand = liste[random.randint(0, 1)]
    if gjenstand.navn=="potion of healing":
        print(f"Kisten inneholder en {gjenstand.navn} og {navn_spiller} faar dermed doblet livet sitt")
        spiller.spillerPotionofhealing()
        print()

    else: 
        print(f"\nI kisten var det et monster med navn {gjenstand.navn}")
        naa_rom.monster=gjenstand
        selveKampen()

#funksjon for aa lage en liste med alle vaapnene
def printVaapen():
    liste=[]            
    for i in spiller.gjenstander:
        liste.append(i.navn)
    return liste

#funksjon for selve kampen med monsteret
def selveKampen():
    print("Kampen har begynt!")
    print(f"\nDu tar det foorste slaget!")
    while naa_rom.monster.liv == True:
        mulige_vaapen = printVaapen()

        if printVaapen()[-1] == "knyttneve": 
            print("\nDu har dessverre ingen vaapen så du maa klare deg med knyttnevene. Skriv 'knyttneve' for aa slaa")
        else:
            print(f"\nDu kan bruke {', '.join(printVaapen())}. Faar aa bruke gjenstanden skriver du bare inn navnet paa gjenstanden")
            spiller.printEgenskap()

        print(f"Monsteret har {naa_rom.monster.hp} hp og du har {spiller.hp} liv!")
        slaa_valg=input("Hva velger du?: ")
        if slaa_valg in printVaapen():
            for i in range(len(mulige_vaapen)):
                if mulige_vaapen[i]==slaa_valg:
                    naa_rom.monster.hp -= spiller.gjenstander[i].skade
                    if (naa_rom.monster.sjekkliv())==True:
                        print(f"\n{navn_spiller} vant kampen! Gratulerer.")
                        break
                    print(f"\nDu gjorde {spiller.gjenstander[i].skade} skade paa monsteret, saa naa har det {naa_rom.monster.hp} liv!")
                    naa_rom.monster.gjooreSkade(spiller) 
        else: print("Skriv inn et gyldig alternativ")
    del(naa_rom.monster)

#funksjon for aa informere om at spilleren er i rom med et monster
#funksjonen stiller spoersmaal om spilleren vil sloss eller ikke
def monsterKamp():
    print(f'Du har kommet i et rom med et monster med navnet {naa_rom.monster.navn}')
    print(f'Du kan velge å loope eller å sloss!')
    fightorflight = input("Ja eller nei?: ").lower().replace(" ", "")

    if fightorflight == "ja":
        selveKampen()

    else: 
        print("\nNeivel, kanskje en annen gang")

#funksjonen til selve spillet
sant = True
def kjoor():
    settStartverdier()
    global sant, naa_rom, rad_nr, kolonne_nr, valg_muligheter
    while sant==True:
        valg_muligheter = [] #nullstiller valgmuligheter for hver iterasjon
        print(f"\n{navn_spiller} er rom nr {naa_rom.romnummer}")
        
        #sjekker om rommet har en gjenstand
        #printer hvilken gjenstand det, og hva den gjør
        if finnVariabel()!=None:
            if finnVariabel()=="gjenstand":
                if naa_rom.gjenstand.navn=="potion of healing":
                    print(f"Dette rommet har en/et {naa_rom.gjenstand.navn}")
                    print("Dersom du drikker den har faar du doblet livet ditt")
                    print("For aa drikke den maa du skrive 'drikk'")
                    valg_muligheter.append("drikk")
                else:
                    print(f"Dette rommet har en/et {naa_rom.gjenstand.navn}, som gir {naa_rom.gjenstand.skade} skade per treff")
                    print("For aa plukke det opp maa du skrive 'plukk opp'")   
                    valg_muligheter.append("plukkopp")
                    
            if finnVariabel()=="kiste":
                print(f"Dette rommet har en/et {finnVariabel()}")
                valg_muligheter.append("aapne")
                print("For aa aapne kisten skriver du inn aapne")
            if finnVariabel()=="felle":
                print(f"ooups, {navn_spiller} traakket i en felle og mistet halve livet")
                spiller.felle()
            if finnVariabel()=="monster":
                monsterKamp()

        else:
            print("Dette rommet har ingenting!")

        #dersom monsteret i det siste rommet ikke er der, har man har vunnet
        #og da stopper while-loekken aa kjoere
        try: 
            rom_liste[2][2].monster
        except:
            sant=False
            print("Du vant spillet")
            break
        
        #printer ut hvilke retninger spilleren kan gaa
        finnretning()

        valg = input(f"Hva vil {navn_spiller} gjøre: ").lower().replace(" ", "")
        
        #sjekker om inputen var et gyldig valg
        if valg not in valg_muligheter:
            print("\nSkriv inn et gyldig alternativ")
 
        else:
            if valg == "opp":
                rad_nr +=1
            elif valg == "hoeyre":
                kolonne_nr +=1
            elif valg == "venstre":
                kolonne_nr -=1

            if valg == "plukkopp":
                plukkOppGjenstand()
                delattr(naa_rom, "gjenstand")
                valg_muligheter.remove("plukkopp")
            
            if valg == "aapne":
                aapneKiste()
                delattr(naa_rom, "kiste")
                valg_muligheter.remove("aapne")

            if valg == "drikk":
                spiller.spillerPotionofhealing()
                print(f"{navn_spiller} har nå {spiller.hp} liv!")
                delattr(naa_rom, "gjenstand")
                valg_muligheter.remove("drikk")
        #oppdaterer naa_rom
        naa_rom=rom_liste[rad_nr][kolonne_nr]
        
#spillet kjoeres
kjoor()
