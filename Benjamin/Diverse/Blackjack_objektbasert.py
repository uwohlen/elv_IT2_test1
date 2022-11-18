class Kort:
    def __init__(self, verdi, slag):
        self.verdi = verdi
        self.slag = slag
    
for i in range(2,15):
    i = Kort(i,'♥')
for i in range(15,28):
    i = Kort(i - 13,'♦')
for i in range(28,41):
    i = Kort(i - 26,'♠')
for i in range(41,54):
    i = Kort(i - 39,'♣')

print(i.verdi)

