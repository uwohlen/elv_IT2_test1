"""
Sammenligner variabelen dictionary og funksjoner... 
med en variabel som bygger på en klasse med innebygd metode
UW
"""

mars={
    "navn":"Mars",
    "solavstand": 227.9,
    "radius": 3389.5
}

def rad(planet):
    print(planet["radius"])

rad(mars)

class Planet:
  def __init__(self, navn, solavstand, radius):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius

  def rad(self):
      print(self.radius)

jupiter = Planet("Jupiter",778.5,69911)

jupiter.rad()

