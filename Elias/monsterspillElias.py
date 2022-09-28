from select import select


class Monster:
    def __init__(self, navn:str, hp:int = 0, skade_per_slag:int = 0, type:str = "", lokasjon:str = ""):
        self.navn = navn
        self.hp=hp
        self.skade_per_slag=skade_per_slag
        self.type = type
        self.lokasjon = lokasjon

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

