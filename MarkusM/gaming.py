
from itertools import combinations
import random as r


class monster: #konstruktør for monster
    def __init__(self,hp,lv,dmg,wk,xp,id,name):
        self.id = id
        self.hp = hp
        self.lv = lv
        self.dmg = dmg
        self.wk = wk
        self.xp = xp
        self.name = name

    def combat(self): #monster angriper
        hero.hp = hero.hp - self.dmg
        print(f"{hero.hp} liv igjen")
        if hero.hp <=0:
            hero.dead()

    def mcombat(self,amount): #mange monstre angriper
        hero.hp = hero.hp - self.dmg*amount
        print("du tar",self.dmg*amount,"skade")
        print(f"{hero.hp} liv igjen")
        if hero.hp <=0:
            hero.death()


class hero(monster):
    def __init__(self,hp,lv,dmg,wk,xp,name,dead,coward):
        super().__init__(hp,lv,dmg,wk,xp,0,name)
        self.dead = dead
        self.coward = coward
    
    def victory(self,monsterID,monsterNr):
        #hvis ett monster dør:

        print(f"{monsterList[monsterID-1].name} døde")
        self.xp += monsterList[monsterID-1].xp
        print("du fikk",monsterList[monsterID-1].xp,"xp")
        
        monsterNr = monsterNr-1
        monsterKilled = 1

        #sjanse for å drepe ett ekstra monster
        if monsterNr > 1:
            if r.randint(1,12)==12:
                print("du dreper enda ett monster!")
                monsterNr = monsterNr-1
                self.xp += monsterList[monsterID-1].xp
                print("du fikk",monsterList[monsterID-1].xp,"xp")
                monsterKilled = 2


        print("det er",monsterNr,"monstre igjen")

        if monsterNr == 0:
            print("du vant!")
        else:
            print("kampen fortsetter")
        return monsterKilled #returnerer hvor mange monstre som er drept
        
    def combat(self,monsterID,monsterNr):
        monsterList[monsterID-1].hp = monsterList[monsterID-1].hp-self.dmg
        if monsterList[monsterID-1].hp <= 0:
            return hero.victory(monsterID,monsterNr)
        
    
    def action(self):
        a = input("hva vil du gjøre? ")
    def combatAction(self):
        print("")
        print('trykk "f" for å sloss')
        print('trukk "r" for å stikke av')
        a = input("hva gjør du? ")

        print("")
        print("")
        print("")

        if a == "f":
            return "f"
        if a == "r":
            return "r"
        

    def death(self):
        print("du døde :(")
        print("på reisen din klarte du å:")
        print("siste stats:")

        hero.dead = True




        




class event:
    def __init__(self,monsterSpawn,monsterAmount,eventText,specialEvent,eventID):
        self.eventID = eventID
        self.monsterSpawn = monsterSpawn
        self.monsterAmount = monsterAmount
        self.eventText = eventText
        self.specialEvent = specialEvent

    def event(self):
        if self.specialEvent == False:
            print("")


            print(self.eventText)
            if self.monsterAmount == 1:
                #vanlige events
                if r.randint(1,6) == 1:
                    print("du reagerer fort og angriper!")
                    hero.combat(self.monsterSpawn,self.monsterAmount)
                

                while monsterList[self.monsterSpawn-1].hp >=0:
                    if r.randint(1,6) == 6:
                        print(f"{monsterList[self.monsterSpawn-1].name} har demens, og glemmer derfor å angripe")

                    else:
                        monsterList[self.monsterSpawn-1].combat()
                    
                    action = hero.combatAction()  #actions11
                    if action == "f":
                        print("du angriper")
                        hero.combatx(self.monsterSpawn,self.monsterAmount)
                        
                    if action =="r":
                        print("du stakk av")
                        hero.coward +=1
                        self.monsterAmount = 0
                
                #for eventer med fler enn ett monster
            elif self.monsterAmount <= 6:

                while self.monsterAmount > 0:

                    monsterList[self.monsterSpawn-1].mcombat(self.monsterAmount)
                    if hero.dead == True:
                        break
                    
                    print("")
                    action = hero.combatAction()  #actions
                    if action == "f":
                        print("du angriper")
                        self.monsterAmount-=hero.combat(self.monsterSpawn,self.monsterAmount)
                        
                    if action =="r":
                        print("du stakk av")
                        hero.coward +=1
                        self.monsterAmount = 0
                        

            print("")
        elif self.specialEvent == True:
            if self.eventId == 1:
                #spesialevent 1
                print("")

            else:
                print("feil. Fant ikke eventID")
class wEvent:
    def __init__(self,eventText,options,keyOptions):
        self.eventText = eventText
        self.options = options
        self.keyOptions = keyOptions


event1 = event(1,1,"Ett monster angriper deg!",False,101)
event2 = event(1,6,"En gjeng med monstere angriper deg!",False,102)

monster1 = monster(1,1,1,1,1,1,"gnom")
monster2 = monster(1,1,1,1,1,1,1)
hero = hero(30,1,1,1,1,"geir",False,1)

monsterList = []
monsterList.append(monster1)
monsterList.append(monster2)


event1.event()
hero.action()

event2.event()
