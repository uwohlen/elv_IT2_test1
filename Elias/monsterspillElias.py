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

class Rom:
    def __init__(self, monster:bool=False, kiste:bool=False, gjenstand:bool=False, felle:bool=False):
        self.monster = monster
        self.kiste = kiste
        self.gjenstand = gjenstand
        self.felle = felle


#setter startverdier for spiller
start_hp_spiller = 100
skade_start = 5
spiller = Spiller(navn_spiller, start_hp_spiller, skade_start, "knyttneve")

monster1 = Monster("")

rom1 = Rom().kiste=True
rom2 = Rom().felle=True
rom3 = Rom().gjenstand="sverd"
rom4 = Rom().monster=True
rom5 = Rom().gjenstand="felle"
rom6 = Rom()
rom7 = Rom().gjenstand = "potion of healing"
rom8 = Rom()
rom9 = Rom().monster = True

rom_liste =  [
        [rom1, rom2, rom3],
        [rom4, rom5, rom6],
        [rom7, rom8, rom9],
]

naa_rom = rom_liste[0][0]