

class Vare:
    def __init__(self, kategori, underkategori, pristype, pris):
        self.kategori = kategori
        self.underkategori = underkategori
        self.pristype = pristype
        self.pris = pris

        
    def total(self, mengde):
        return (self.pris * mengde)
    


varer = [Vare('Eppler', 'Pink', 'kg', 20), Vare('Appelsiner', 'Jaffa', 'kg', 25), Vare('Annanas', 'hel', 'stk.', 15), Vare("Kaker", "sjokolade", "stk.", 50)]

pris = []
for i in varer:
    pris.append(0)

ferdig = False
total = 0

while not ferdig:
    
    print("Skriv:")
    for x in range(len(varer)):
        print(f"{x + 1} for {varer[x].kategori}")
    print(f"{x + 2} hvis du er ferdig")
    
    gyldig = False
    while not gyldig:
        try:
            inp = int(input())
            gyldig = True
        except:
            print("Ugyldig varenummer prøv igjen")

    if inp == len(varer) + 1:
        ferdig = True
        break
    
    print(f"Hvor mange {varer[inp - 1].pristype} {varer[inp - 1].kategori} vil du ha?")
    gyldig = False
    
    while not gyldig:
        try:
            stk = int(input())
            gyldig = True
        except:
            print("Ugyldig antall prøv igjen")
            
    pris[inp - 1] = pris[inp - 1] + varer[inp - 1].total(stk)
    total = total + varer[inp - 1].total(stk)
    
    
for x in range(len(varer)):
    if pris[x] == 0:
        continue
    else:
        print(f"{varer[x].kategori}, {int(pris[x] / varer[x].pris)}{varer[x].pristype}: {pris[x]}kr")
print(f"Slutt summen er: {total}kr")
    