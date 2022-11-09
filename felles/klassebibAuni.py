class Planet:
  """
  Klasse for å lage planet-objekter.

  Parametre:
    navn (str): Planetens navn
    solavstand (float): Avstand fra sola i millioner km
    radius (float): Planetens radius i km
    antallRinger = 0 (int): Antall ringer rundt planeten
  """

  def __init__(self, navn:str, solavstand:float, radius:float, antallRinger:int = 0):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius
    self.antallRinger = antallRinger
  
  def volum(self):
    from math import pi
    return (4/3) * pi * self.radius**3


