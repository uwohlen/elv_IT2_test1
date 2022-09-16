

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
        
    
r1 = rektangel()
r1.input()
print(r1)