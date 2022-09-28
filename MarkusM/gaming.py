from ctypes.wintypes import HPALETTE



class monster:
    def __init__(self,hp,lv,dmg,wk,xp):
        self.hp = hp
        self.lv = lv
        self.dmg = dmg
        self.wk = wk
        self.xp = xp


class hero(monster):
    def __init__():
        super().__init__()
    
    def victory(self):
        self.xp += monster.xp



class event:
    def __init__(self,monsterSpawn,monsterAmount,eventText,specialEvent)
        self.monsterSpawn = monsterSpawn
        self.monsterAmount = monsterAmount
        self.eventText = eventText
        self.specialEvent = specialEvent

    def event(self):
        if self.specialEvent == False:
            print("")
            print(self.eventText)
            print("")
        elif self.specialEvent == True:
            print("")


