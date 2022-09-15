def leggSammen(liste: list):
    """Summerer elementene i en liste. 
    En input, av typen liste, elementene må være av samme type. 
    En output, type returnert er avhengig av type elementer i input."""
    summen = liste[0]
    for i in range(1,len(liste)):
        summen += liste[i]
    return summen

class GrapesApples:
    def __init__(self,wGr, wAp):
        self.wGr = wGr
        self.wAp = wAp

    GRKG = 12
    APKG = 10

    def price(self):
        print("Total pris er: ",self.wGr*self.GRKG+self.wAp*self.APKG)
