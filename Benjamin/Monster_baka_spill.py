class Monster:
    def __init__(self,navn,iq,juks):
        self.navn = navn
        self.iq = iq
        self.juks = juks
    
    def visInfo(self):
        print(f'Monsteret {self.navn} liker ikke å tape, og med sin iq på {self.iq}, vil han knuse deg!')
        print(f'{self.navn} kan muligens jukse litt, men {self.navn} er et monster, hva skal du gjøre?')


class Spiller:
    def __init__(self,navn,iq,flaks):
        self.navn = navn
        self.iq = iq
        self.flaks = flaks
    
    def __str__(self):
        return(f'Karakteren {self.navn} har en iq på hele {self.iq}!')
    
arne = Spiller("Arne", 140,0)
per = Spiller("Per", 110,1)

print(arne)
print(f'{per}, men Per har til gjengjeld super mye flaks!')
karakter = input(print(f'Velg hvilken karakter du vil ha: For Arne trykk 1, og for Per trykk 2 '))