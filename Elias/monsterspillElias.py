from ast import Str
from multiprocessing.sharedctypes import Value


class Monster:
    def __init__(self, navn:str, hp:int = 0, skade_per_slag:int = 0, type:str = "", lokasjon:str = "", liv:bool=True):
        self.navn = navn
        self.hp=hp
        self.skade_per_slag=skade_per_slag
        self.type = type
        self.lokasjon = lokasjon

        if self.hp<0:
            liv=True

class Spiller:
    def __init__(self, navn:str, hp:int = 0, skade_per_slag:int = 0, vaapen:str = "", gjenstander:list = []):
        self.navn = navn
        self.hp = hp
        self.skade_per_slag = skade_per_slag
        self.vaapen = vaapen
        self.gjenstander = gjenstander

print("velkommen til dette spillet")
print("maalet med spillet er å komme deg gjennom et hus")
print("i huset kan du finne vaapen, gjenstander, og monster :o")
print("for å bevege deg skriver du enten inn opp, ned, hoeyre, venstre")
navn_spiller = "roger" #input("skriv inn navnet ditt: ")





#setter startverdier for spiller
start_hp_spiller = 100
skade_start = 5
spiller = Spiller(navn_spiller, start_hp_spiller, skade_start, "knyttneve")

monster1 = Monster("")


class Rom:
    def __init__ (self, romnummer):
        self.romnummer = romnummer

rom_liste = [[],[],[]]

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

rom_liste[0][0].kiste=True
rom_liste[0][1].felle=True
rom_liste[0][2].gjenstand="sverd"
rom_liste[1][0].monster=True
rom_liste[1][1].gjenstand="felle"
rom_liste[2][0].gjenstand = "potion of healing"
rom_liste[2][2].monster = True

naa_rom = rom_liste[0][0]



def finnretning():
    mulige_retninger = "Du kan bevege deg "
    for i in range(3):
        for j in range(3):
            if naa_rom == rom_liste[i][j]:
                rad_nr = i 
                kolonne_nr = j

    if rad_nr == 0 or 1:
        mulige_retninger+="opp"

    if kolonne_nr<2:
        mulige_retninger+=", til høyre"
    if kolonne_nr > 0:
        mulige_retninger+=" eller til venstre"
        
    print(mulige_retninger)


                

    
finnretning()  

sant = True
"""
def kjoor():
    while sant==True:
         or "felle" or"gjenstand" or"monster"
        """
liste=dir(naa_rom)
for i in liste:
    if "_" not in i and i != "romnummer":
        verdi = i     
        
