import math as m

class Planet:
  def __init__(self, navn, solavstand, radius):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius

  def volum(self):
    return (4/3) * m.pi * self.radius**3

  def overflate(self):
    return 4 * m.pi * self.radius**2


jupiter = Planet("Jupiter", 778.5, 69911)
mars = Planet("mars", 45.5, 5311)

print(mars.volum())
print(mars.overflate())