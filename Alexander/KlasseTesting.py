import math

class mangekant:
    def __init__(self, kanter):
        self.lengder = [0] * kanter
        self.kanter = kanter
        
    def __str__(self):
        return f"Sideantall: {self.kanter}\nSidelengder: {str(self.lengder)}\nOmkrets: {self.omkrets()}"
        
    def input(self):
        for x in range(0, self.kanter):
            self.lengder[x] = float(input("Lengde av side {}: ".format(x + 1)))
            
    def omkrets(self):
        tmp = 0
        for x in range(0, self.kanter):
            tmp += self.lengder[x]
        return tmp

class rektangel(mangekant):
                
    def __init__(self):
        super().__init__(4)
    
    def __str__(self):
        return f"Rektangel med side lengder: {str(self.lengder)}\nOmkrets: {self.omkrets()}"
        
    def input(self):
        w = float(input("Bredden av rektangelen: "))
        h = float(input("Høyden av rektangelen: "))
        self.lengder[0] = self.lengder[2] = w
        self.lengder[1] = self.lengder[3] = h
        
class trekant(mangekant):
    
    def __init__(self):
        super().__init__(3)
        
    def areal(self):
        s = self.omkrets() / 2
        return round(math.sqrt(s * (s - self.lengder[0]) * (s - self.lengder[1]) * (s - self.lengder[2])), 2)
        
    
t1 = trekant()
t1.input()
print("Areal: ", t1.areal())