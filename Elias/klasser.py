from math import pi
class Planet:
    def __init__(self, navn, radius, avstand):
        self.navn = navn
        self.radius = radius
        self.avstam = avstand
    
    def areal(self):
        return pi*self.radius**2

mars=Planet("merkur",3445,34556)
print(mars.areal())