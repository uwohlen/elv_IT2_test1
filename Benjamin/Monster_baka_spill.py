class Monster:
    def __init__(self,navn,iq,juks):
        self.navn = navn
        self.iq = iq
        self.juks = juks
    
    def visInfo(self):
        print(f'Monsteret {self.navn} liker ikke å tape, og med sin iq på {self.iq}, vil han knuse deg!')
        print(f'{self.navn} kan muligens jukse litt, men {self.navn} er et monster, hva skal du gjøre?')


class Spiller:
    def __init__(self,navn,iq,):
        self.navn = navn
        self.iq = iq
    
    def visInfo(self):