

class monster:
    def __init__(self,hp,lv,dmg,wk,xp,id,name):
        self.id = id
        self.hp = hp
        self.lv = lv
        self.dmg = dmg
        self.wk = wk
        self.xp = xp
        self.name = name

    def combat(self):
        hero.hp = hero.hp - self.dmg
        print(f"{hero.hp} liv igjen")


class hero(monster):
    def __init__(self,hp,lv,dmg,wk,xp,name):
        super().__init__(hp,lv,dmg,wk,xp,0,name)
    
    def victory(self):
        self.xp += monster.xp



class event:
    def __init__(self,monsterSpawn,monsterAmount,eventText,specialEvent,eventID):
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
            if self.eventId = 1
    


monster1 = monster(1,1,1,1,1,1,1)
monster2 = monster(1,1,1,1,1,1,1)
hero = hero(1,1,1,1,1,"geir")

monsterList = []
monsterList.append(monster1)
monsterList.append(monster2)


monsterList[0].combat()
