class Rektangel:
  """Klasse for å representere et rektangel"""
  def __init__(self, lengde, bredde):
    """Konstruktør"""
    self.lengde = lengde
    self.bredde = bredde
  
  def areal(self):
    """Metode for å beregne areal"""
    return self.lengde * self.bredde

class Kvadrat(Rektangel):
  """Klasse for å representere et kvadrat"""
  def __init__(self, sidekant):
    super().__init__(sidekant, sidekant)

kvadrat1 = Kvadrat(2)
kvadrat2 = Kvadrat(3)
rektangel1 = Rektangel(2, 3)
rektangel2 = Rektangel(4, 6)

print(kvadrat1.areal())
print(kvadrat2.areal())
print(rektangel1.areal())
print(rektangel2.areal())