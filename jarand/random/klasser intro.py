import math as m

class Planet:
  def __init__(self, navn, solavstand, radius):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius

  def volum(self):
    return (4/3) * m.pi * self.radius**3

  def visInfo(self):
    print(f"Planeten {self.navn} er {self.solavstand} millioner km unna sola og har radius {self.radius} km.",self.volum())


jupiter = Planet("Jupiter", 778.5, 69911)

print(jupiter.volum())
jupiter.visInfo()