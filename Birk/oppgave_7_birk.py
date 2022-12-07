
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
        return kategori.pris * mengde
    
eple = Vare("Eple", "Pink", "Kilo", 20, 1)
appelsiner = Vare("appelsin", "Jaffa", "Kilo", 25, 1)
ananas = Vare("Ananas", "Hel", "Stk", 15, 1)

sum = 0
handler = True

while handler:
    print("Du kan kjøpe: eple, appelsiner, ananas")
    print(input("Hva vil du kjøpe? "))
    
    if input == "eple":
        print(input("Hvor mange kilo vil du kjøpe? "))
        print(eple.kjop(eple, input))
        print("Du har kjøpt " + input + " kilo epler for " + eple.kjop(eple, input) + "kr")
        sum += eple.kjop(eple, input)
        print(input("Vil du kjøpe noe mer? (Ja/Nei)"))
        if input == "Nei":
            handler = False
            print("Du har kjøpt for " + sum + "kr")
        
    elif input == "appelsiner":
        print(input("Hvor mange kilo vil du kjøpe? "))
        print(appelsiner.kjop(appelsiner, input))
        print("Du har kjøpt " + input + " kilo appelsiner for " + appelsiner.kjop(appelsiner, input) + "kr")
        sum += appelsiner.kjop(appelsiner, input)
        print(input("Vil du kjøpe noe mer? (Ja/Nei)"))
        if input == "Nei":
            handler = False
            print("Du har kjøpt for " + sum + "kr")
        
    elif input == "ananas":
        print(input("Hvor mange kilo vil du kjøpe? "))
        print(ananas.kjop(ananas, input))
        print("Du har kjøpt " + input + " kilo ananas for " + ananas.kjop(ananas, input) + "kr")
        sum += ananas.kjop(ananas, input)
        print(input("Vil du kjøpe noe mer? (Ja/Nei)"))
        if input == "Nei":
            handler = False
            print("Du har kjøpt for " + sum + "kr")
        
    else:
        print("Du har ikke valgt en vare som er tilgjengelig")