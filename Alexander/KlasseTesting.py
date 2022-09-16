

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

s1 = mangekant(4) 
s1.input()
print(s1)         