import random as r
import sys, time
import os

def slow_type(t):
    typing_speed = 15000 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(r.random()*10.0/typing_speed)

def slower_type(t,speed):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(r.random()*10.0/speed)

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

class monster: #konstruktør for monster
    def __init__(self,hp,lv,dmg,wk,xp,name):
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
    def stats(self):
        print("")
        print(f"navn: {self.name}")
        print(f"liv: {self.hp}")
        print(f"level: {self.lv}")
        print(f"damage: {self.dmg}")
        print(f"xp: {self.xp}")
        print(f"svakhet: {self.wk}")


class hero(monster):
    def __init__(self,hp,lv,dmg,wk,xp,name,dead,coward):
        super().__init__(hp,lv,dmg,wk,xp,name)
        self.dead = dead
        self.coward = coward
        self.inv = []

    def bossFight(self,monsterID):
        if monsterID == 3: #ninja bossfight
            print("")
            print("Ninja: Jeg skal ikke prøve hardt siden du er ny rundt disse kanter")
            print("Du angriper Ninja!")
            jukseSpm = False
            while monster3.hp > 0:
                print("")
                a = self.combatAction()

                if a == "f":
                    self.combat(monsterID,1)

                    if monsterList[monsterID-1].hp > 0:
                        if self.hp == 1:
                            if jukseSpm == False:
                                print("Ninja: Siden du har ett hp igjen lar jeg deg slå meg en gang til, for morro skyld.")
                                time.sleep(2)
                                slow_type("Vil du jukse?")
                                time.sleep(1)
                                print("")

                                a = input('Skriv "j" for ja og "n" for nei ')

                                if a == "j":
                                    time.sleep(0.5)
                                    slow_type("Du jukser")
                                    jukseSpm = True
                                    print("")
                                    time.sleep(0.9)
                                    slow_type("Hacker epic games...")
                                    print("")
                                    time.sleep(0.5)
                                    slow_type("Infiltrerer fortnite_server...")
                                    time.sleep(0.5)
                                    print("")
                                    slow_type("Sletter ninja.png...")
                                    time.sleep(1)
                                    print("")
                                    slow_type("Error. Trenger bankID-innlogging")
                                    time.sleep(1)
                                    print("")
                                    input("fødeslsnummer")
                                    input("passord")
                                    clear()
                                    slower_type("...",150)
                                    time.sleep(1)
                                    clear()
                                    slower_type("...",100)
                                    time.sleep(1)
                                    clear()
                                    slower_type("...",50)
                                    time.sleep(1)
                                    clear()
                                    slower_type("...",20)
                                    time.sleep(1)
                                    clear()
                                    
                                    slow_type("suksess!")
                                    time.sleep(0.5)
                                    print("")
                                    slow_type('"Tyler_Fortnite_Ninja_blevins.hp" = 0 ')
                                    slower_type("...",10)
                                    print("")





                                if a == "n":
                                    print("Du jukser ikke")
                                    jukseSpm = True
                            else:
                                hero.death()
                                hero.stats()
                                sys.exit()


                            

                        if self.hp > 1:
                            print("Ninja angriper")
                            print("Ninja dreper deg nesten i ett slag. Du har nå ett liv igjen")
                            self.hp = 1

                        
                if a == "r":
                    if r.randint(1,12) == 12:
                        print("")
                        print("Suksess! Du klare å stikke av!")
                        break
                    else:
                        print("")
                        print("Ninja: Du kan ikke stikka av fra meg!")
                if a == "c":
                    monster3.stats()
                    print("Ninja: Hvorfor ser du på meg på den måten?")
                    #utvide for å lage en alternativ slutt på kampan
                
            

            
        else:
            print("Feil. monsterID ikke funnet.")
            


    def levelUp(self):
        self.lv += 1
        print(f"du fikk en level! Du er har nå {self.lv} levler")

    def itemAdd(self,itemAdd):
        if len(self.inv) == 4:
            print("inventoriet er fullt! Du kaster det du prøvde å plukke opp.")
        else:
            self.inv.append(itemAdd)

    def invOpen(self):
        while True:
            #displayer listen av valg
            print("") 
            print("Skriv inn tallet du objektet du vil vite mer om,")
            print('eller skriv "b" for å gå tilbake')
            if len(self.inv) >= 1:
                print(f"1: {self.inv[0].name}")
                if len(self.inv) >= 2:
                    print(f"2: {self.inv[1].name}")
                    if len(self.inv) >= 3:
                        print(f"3: {self.inv[2].name}")
                        if len(self.inv) == 4:
                            print(f"4: {self.inv[3].name}")
                        else:
                            print("4: tom")
                    else:
                        print("2: tom")
                        print("3. tom")
                else:
                    print("2: tom")
                    print("3: tom")
                    print("4: tom")

                a = input("Hva gjør du?")
                print("")
                if a == "1": #vise stats til inventory
                    if len(self.inv) > 0:
                        self.itemOptions(0)
            
                elif a == "2":
                    if len(self.inv) > 1:
                        self.itemOptions(1)

                elif a == "3":
                    if len(self.inv) > 2:
                        self.itemOptions(2)
            
                elif a == "4":
                    if len(self.inv) > 3:
                        self.itemOptions(3)

                elif a == "b":
                    break
            elif len(self.inv) == 0:
                print("")
                print("Du har ingen items!")
                break
    def itemOptions(self,itemIndex):
        
        print("")
        time.sleep(0.5)
        print('trykk "s" for å se stats')
        print('trykk "k" for å kaste')
        print('trykk en annen for å gå tilbake')

        a = input(f"Hva vil du gjøre med {self.inv[itemIndex].name}?")

        if a == "k":
            self.itemRemove(itemIndex)
        if a == "s":
            self.iStats(itemIndex)


    def itemRemove(self,itemIndex):
        if len(self.inv) == 1:
            self.inv.clear()
        else:
            del self.inv[itemIndex]

    def iStats(self,i):
        print("")
        print(f"Navn: {self.inv[i].name}")
        print(self.inv[i].desc)
        print(f"Skade: {self.inv[i].dmg}")
    
    def stats(self):
        print("")
        print("")
        print(f"liv: {self.hp}")
        print(f"level: {self.lv}")
        print(f"damage: {self.dmg}")
        print(f"xp: {self.xp}")

    
    def victory(self,monsterID,monsterNr):
        #hvis ett monster dør:

        print(f"{monsterList[monsterID-1].name} døde")
        self.xp += monsterList[monsterID-1].xp
        print("du fikk",monsterList[monsterID-1].xp,"xp")
        while self.xp >= 10:
            self.xp -=10
            self.levelUp()
            
        
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

        if monsterNr == 0:
            print("du vant!")
        else:
            print("kampen fortsetter")
            print("det er",monsterNr,"monstre igjen")
            return monsterKilled #returnerer hvor mange monstre som er drept
        
    def combat(self,monsterID,monsterNr):
        monsterList[monsterID-1].hp = monsterList[monsterID-1].hp-self.dmg
        print(f"Du gjør {self.dmg} skade")
        print(f"{monsterList[monsterID-1].name} har {monsterList[monsterID-1].hp} liv igjen")
        if monsterList[monsterID-1].hp <= 0:
            return hero.victory(monsterID,monsterNr)
        
    
    def action(self):
        a = input("hva vil du gjøre?")
    def eAction(self):
        print("")
        time.sleep(0.5)
        print('trykk "f" for å sloss')
        print('trykk "c" for å sjekke stats til personen du møtte')
        print('trykk "s" for å se dine stats')
        print('trykk "r" for å stikke av')
        print('trykk "i" for å åpne inventory')
        a = input("hva gjør du? ")

        if a == "f":
            return "f"
        if a == "r":
            return "r"
        if a == "c":
            return "c"
        if a == "s":
            hero.stats()
        if a == "i":
            hero.invOpen()

    def combatAction(self):
        time.sleep(1)
        print('trykk "f" for å sloss')
        print('trykk "r" for å stikke av')
        print('trykk "s" for å se stats')
        print('trykk "c" for å se fienden sine stats')
        a = input("hva gjør du? ")

        print("")
        print("")
        print("")

        if a == "f":
            return "f"
        if a == "r":
            return "r"
        if a == "s":
            hero.stats()
        if a == "c":
            return "c"
        
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
                

                while monsterList[self.monsterSpawn-1].hp > 0:
                    if r.randint(1,6) == 6:
                        print(f"{monsterList[self.monsterSpawn-1].name} har demens, og glemmer derfor å angripe")

                    else:
                        monsterList[self.monsterSpawn-1].combat()
                    
                    action = hero.combatAction()  #actions11
                    if action == "f":
                        print("du angriper")
                        hero.combat(self.monsterSpawn,self.monsterAmount)
                        
                    if action =="r":
                        print("du stakk av")
                        hero.coward +=1
                        self.monsterAmount = 0
                        break
                    if action == "c":
                        monsterList[self.monsterSpawn-1].stats()
                
                #for eventer med fler enn ett monster
            elif self.monsterAmount >= 2:

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
                        break
                    if action =="c":
                        monsterList[self.monsterSpawn-1].stats()
                        

            print("")
        elif self.specialEvent == True:
            if self.eventID == 1:
                #spesialevent 1
                tMats = False
                while True:
                    hasMats = False
                    for i in range(len(hero.inv)):
                        if "Tre" in hero.inv[i].name:
                            hasMats = True
                            matsLocation = i
                            break
                    if hasMats == True and tMats == False:
                        print("")
                        print(self.eventText)
                        print("")
                        print("Tyler: Du har mats!!!")
                        print("Kan jeg få? Jeg trenger for å drepe tFue i moisy mire")
                        a = input('Gir du han? Skriv inn "y" for ja og "n" for nei')
                        if a == "y":
                            hero.itemRemove(i)
                            print("")
                            print(f"Ninja: takk {hero.name}")
                            tMats = True
                            event3.eventText = "Inne finner du Ninja fra Fortnite. Han er takknemlig for at du ga han mats, og planlegger å straks dra til moisty mire"
                            hero.itemAdd(fortniteScar)
                            print("Ninja ga deg en legendarisk scar fra Fortnite!")
                        if a =="n":
                            print("")
                            print("Triste saker, trodde du var bedre enn dette. Nå kan jeg aldri drepe tFue.")
                            tMats = True
                            event3.eventText = "Inne finner du Ninja fra Fortnite. Han er sint fordi du ikke ga han mats, selv om du har det på deg. Du burde kanskje ikke bli her lenge"
                    else:
                        print("")
                        print(self.eventText)
                        a = hero.eAction()
                        if a == "c":
                            monsterList[self.monsterSpawn-1].stats()
                        if a == "f": #helten sloss mot tyler
                            print("")
                            print('Ninja: Feil valg')
                            monster3.bossFight(self.monsterSpawn)
                            
                        if a == "r":
                            print("")
                            print("Ninja: Du løper fra meg???")
                            print("Du løp fra Ninja")
                            hero.coward +=1
                            break

            else:
                print("feil. Fant ikke eventID")

class wEvent:
    def __init__(self,eventText,options,keyOptions,id):
        self.eventText = eventText
        self.options = options
        self.keyOptions = keyOptions
        self.id = id
    
    def worldEventOptions(self):
        
        while True:
            print("")
            print(self.eventText)
            if "y" in self.options:
                if self.id == 1: #spesiell melding for event 1
                    print('trykk "y" for å gå inn')
                else: #ordinær melding
                    print('trykk "y" for ja')
            
            if "n" in self.options:
                if self.id == 1: #spesiell melding for event 1
                    print('trykk "n" for å bli utenfor')
                else: #ordinær melding
                    print('trykk "n" for nei')
            if "i" in self.options:
                print('trykk "i" for å åpne inventoriet')
            
            if "c" in self.options:
                if self.id == 1: #spesiell melding for event 1
                    print('trykk "c" for å undersøke huset')
                else: #ordinær melding
                    print('trykk "c" for å sjekke  stats til personen du møtte')
            if "s" in self.options:
                print('trykk "s" for å se dine stats')

            a = input("Hva gjør du? ")
            if "i" in self.options and a == "i":
                hero.invOpen()
            if "n" in self.options and a == "n":
                if self.id == 1: #spesiell melding for event 1
                    print("Du forblir utenfor")
                    break
                else: #ordinær melding
                    break

            if "y" in self.options and a =="y":
                if self.id == 1: #spesiell melding for event 1
                    print("Du går inn")
                    event3.event()
                    break
                else: #ordinær melding
                    break
             
            if "c" in self.options and a =="c":
                if self.id ==1: #spesiell melding for evnent 1
                    if r.randint(1,2) == 1:
                        print("")
                        print("Du fant litt tre!")
                        hero.itemAdd(mats)
                    else:
                        print("")
                        print("Ett hus")
            if "s" in self.options and a =="s":
                hero.stats()

    def worldEvent(self):
        print("")

        self.worldEventOptions()


        print("")


class item:
    def __init__(self,name,desc,dmg):
        self.name = name
        self.desc = desc
        self.dmg = dmg



wEvent1 = wEvent("Du kommer til ett hus. Går du inn?",["y","n","i","c","s"],["y","n","i","c","s"],1)
mats = item("Tre","Litt tre du fant. Ubrukelig",0)
fortniteScar = item("Fornite Scar","Legendary scar assault rifle fra Fortnite. Gjør veldig mye skade",27)
starterPinne = item("Pinne","En veldig fin pinne. Ligner svært på en pistol",1)

event1 = event(1,1,"Ett monster angriper deg!",False,101)
event2 = event(2,3,"En gjeng med monstere angriper deg!",False,102)
event3 = event(3,1,"Inne finner du Ninja fra Fornite. Han spør om du har noe materialer til han. Til gjengjeld sier han at han kan gi deg noe spesielt tilbake.",True,1)

monster1 = monster(10,1,1,1,1,"gnom")
monster2 = monster(1,1,1,1,1,"bob")
monster3 = monster(10,10,27,"boogie bomb",100,'Tyler "Fortnite Ninja" Blevins')


hero = hero(30,1,1,1,1,"geir",False,1)

monsterList = []
monsterList.append(monster1)
monsterList.append(monster2)
monsterList.append(monster3)


print("")

hero.bossFight(3)

#hero.inv.append(starterPinne)
#event1.event()
#wEvent1.worldEvent()
"""
event1.event()
hero.action()

event2.event()

event3.event()
"""