
class Vare:
    def __init__(self, kategori, underkategori, pristype, pris, mengde):
        self.kategori = kategori
        self.underkategori = underkategori
        self.pristype = pristype
        self.pris = pris
        self.mengde = mengde
        
    def __str__(self):
        return f"{self.kategori} {self.underkategori} {self.pristype} {self.pris} {self.mengde}"
    
    def kjop(kategori, mengde):
        return int(kategori.pris) * int(mengde)
    
eple = Vare("eple", "Pink", "Kilo", 20, 1)
appelsiner = Vare("appelsin", "Jaffa", "Kilo", 25, 1)
ananas = Vare("ananas", "Hel", "Stk", 15, 1)

sum = 0
handler = True

while handler:
    print("Du kan kjøpe: eple, appelsiner, ananas")
    vare = input("Hva vil du kjøpe? ")
    
    if vare == "eple":
        mengde = input("Hvor mange kilo vil du kjøpe? ")
        print(Vare.kjop(eple, mengde))
        print("Du har kjøpt ", mengde," kilo epler for ", Vare.kjop(eple, mengde), "kr")
        sum += Vare.kjop(eple, mengde)
        fortsett = input("Vil du kjøpe noe mer? (Ja/Nei)")
        if fortsett == "Nei":
            break
        
    elif vare == "appelsiner":
        mengde = input("Hvor mange kilo vil du kjøpe? ")
        print(Vare.kjop(appelsiner, mengde))
        print("Du har kjøpt ", mengde," kilo appelsiner for ", Vare.kjop(appelsiner, mengde), "kr")
        sum += Vare.kjop(appelsiner, mengde)
        fortsett = input("Vil du kjøpe noe mer? (Ja/Nei)")
        if fortsett == "Nei":
            break
        
    elif vare == "ananas":
        mengde = input("Hvor mange kilo vil du kjøpe? ")
        print(Vare.kjop(ananas, mengde))
        print("Du har kjøpt ", mengde," kilo ananas for ", Vare.kjop(ananas, mengde), "kr")
        sum += Vare.kjop(ananas, mengde)
        fortsett = input("Vil du kjøpe noe mer? (Ja/Nei)")
        if fortsett == "Nei":
            break
        
    else:
        print("Du har ikke valgt en vare som er tilgjengelig")