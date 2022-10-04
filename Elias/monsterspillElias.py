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
            liv=False
            print("Du doede")

class Spiller:
    def __init__(self, navn:str, hp:int = 0, skade_per_slag:int = 0, vaapen:str = "", gjenstander:list = []):
        self.navn = navn
        self.hp = hp
        self.skade_per_slag = skade_per_slag
        self.vaapen = vaapen
        self.gjenstander = gjenstander

print("Velkommen til dette spillet")
print("Maalet med spillet er å komme deg gjennom et hus")
print("I huset kan du finne vaapen, gjenstander, og monster :o")
print("For å bevege deg skriver du enten inn opp, ned, hoeyre, venstre")
print("Dersom du kommer i et rom med en gjenstand kan du skrive 'grip' for å plukke det opp eller bruke det")
print("I rom med monster foelger egen instruks")
navn_spiller = "roger"#input("\nFoer du begynner må du skrive inn navnet ditt: ")


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


valg_muligheter=[]

rad_nr=0
kolonne_nr=0

def finnretning():
    mulige_retninger = f"{navn_spiller} kan bevege deg "
    global rad_nr, kolonne_nr
    for i in range(3):
        for j in range(3):
            if naa_rom == rom_liste[i][j]:
                rad_nr = i 
                kolonne_nr = j
                break
   
    if rad_nr == 0 or 1:
        mulige_retninger+="opp"
        valg_muligheter.append("opp")
        if kolonne_nr<2:
            mulige_retninger+=", til hoeyre"
            valg_muligheter.append("hoeyre")
        if kolonne_nr > 0:
            mulige_retninger+=" eller til venstre"
            valg_muligheter.append("venstre")
    print(mulige_retninger)
    
sant = True

def finnVariabel():
    liste=dir(naa_rom)
    for i in liste:
        if "_" not in i and i != "romnummer":
            verdi = i
            return verdi

def kjoor():
    global naa_rom, rad_nr, kolonne_nr
    while sant==True:
        print(f"\n{navn_spiller} har kommet inn i rom nr {naa_rom.romnummer}")
        if finnVariabel()!=None:
            print(f"Dette rommet har en/et {finnVariabel()}")
        else:
            print("Dette rommet har ingenting!")

        finnretning()

        valg = input(f"Hva vil {navn_spiller} gjøre: ").lower()

        if valg not in valg_muligheter:
            print("\nSkriv inn et gyldig alternativ")
            valg = input(f"Hva vil {navn_spiller} gjøre: ").lower()
        
        elif valg == "opp":
            rad_nr +=1
        elif valg == "hoeyre":
            kolonne_nr +=1
        elif valg == "venstre":
            kolonne_nr -=1
    
        naa_rom=rom_liste[rad_nr][kolonne_nr]

kjoor()
