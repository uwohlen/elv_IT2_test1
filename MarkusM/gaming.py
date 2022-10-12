#monsterspill 1.0
import random as r
import sys, time
import os

def slow_type(t):
    typing_speed = 300 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(r.random()*10.0/typing_speed)

def slower_type(t,speed):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(1/speed)

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
        print(f"{self.name} angriper og gjør {self.dmg} skade. Du har {hero.hp} liv igjen")
        if hero.hp <=0:
            hero.death()

    def mcombat(self,amount): #mange monstre angriper
        hero.hp = hero.hp - self.dmg*amount
        print("du tar",self.dmg*amount,"skade")
        print(f"Du har {hero.hp} liv igjen")
        if hero.hp <=0:
            hero.death()

    def stats(self):
        clear()
        print(f"navn: {self.name}")
        print(f"liv: {self.hp}")
        print(f"level: {self.lv}")
        print(f"damage: {self.dmg}")
        print(f"xp: {self.xp}")
        print(f"svakhet: {self.wk}")
        time.sleep(2)
        print("")


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
                    monsterList[monsterID-1].hp = monsterList[monsterID-1].hp-self.dmg*hero.inv[itemSelected].dmg
                    print(f"Du angriper og gjør {self.dmg*hero.inv[itemSelected].dmg} skade")
                    print(f"{monsterList[monsterID-1].name} har {monsterList[monsterID-1].hp} liv igjen")


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
                                    time.sleep(0.9)
                                    jukseSpm = True
                                    print("")
                                    slow_type("Hacker epic games...")
                                    time.sleep(0.5)
                                    print("")
                                    slow_type("Infiltrerer fortnite_server...")
                                    time.sleep(0.5)
                                    print("")
                                    slow_type("Sletter ninja.png...")
                                    time.sleep(1)
                                    print("")
                                    clear()
                                    slow_type("Error. Trenger bankID-innlogging")
                                    time.sleep(1)
                                    print("")
                                    input("fødeslsnummer")
                                    input("passord")
                                    clear()
                                    slower_type("...",15)
                                    time.sleep(1)
                                    clear()
                                    slower_type("...",10)
                                    time.sleep(1)
                                    clear()
                                    slower_type("...",5)
                                    time.sleep(1)
                                    clear()
                                    slower_type("...",2)
                                    time.sleep(1)
                                    clear()
                                    
                                    slow_type("suksess!")
                                    time.sleep(0.5)
                                    print("")
                                    slow_type('"Tyler_Fortnite_Ninja_blevins.hp" = 0 ')
                                    slower_type("...",10)
                                    print("")
                                    monster3.hp = 0 

                                    if len(hero.inv) == 4:
                                        slow_type(f'hero.inventory.remove({hero.inv[3]}')
                                        hero.itemRemove(3)

                                    slow_type(f'{hero.name}.inventory.add(Fortnite_Builder_Plan)...')
                                    hero.itemAdd(Fortnite_Builder_Plan)
                                    time.sleep(0.5)
                                    print("")
                                    slow_type("Tyler_Fortnite_Ninja_Blevins.death...")
                                    time.sleep(0.5)
                                    print("")
                                    print("")
                                    print("Ninja: Stream sniping")
                                    time.sleep(1)
                                    print("")
                                    slow_type(f'{hero.name}.xp.set("tyler_Fortnite_Ninja_Blevins".xp")...')
                                    print("")
                                    time.sleep(1)
                                    print("Du fikk 40 xp!")
                                    time.sleep(0.5)
                                    hero.levelUp()
                                    time.sleep(0.5)
                                    hero.levelUp()
                                    time.sleep(0.5)
                                    hero.levelUp()
                                    time.sleep(0.5)
                                    hero.levelUp()
                                    time.sleep(0.5)

                                    print("Victory royale!")

                                    break
                                    

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
                    if monster3.hp <= 0:
                        print("Ninja: Stream sniping")
                        time.sleep(1)
                        slow_type("Du får 40 xp!")
                        for i in range(4):
                            hero.levelUp()
                            time.sleep(0.5)
                        print("Victory royale!")
                        time.sleep(2)
                        break
                
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
        if monsterID == 4: #rodrik bossfight
            time.sleep(0.5)
            clear()
            slow_type("Den gamle mannen angriper!")
            print("")
            time.sleep(1)
            print("Gjør 0 skade")
            time.sleep(0.5)
            print(f"Du har fortsatt {hero.hp} liv igjen")
            sspm = 0
            time.sleep(1.5)
            clear()
            while True:
                slow_type("Rodrik er utmattet")
                print("")

                a = self.combatAction()
                if a == "f":
                    print("Du gjør 9999 skade!")
                    time.sleep(1.5)
                    slow_type("Den gamle mannen dør!")
                    time.sleep(1)
                    clear()
                    break
                elif a == "r":
                    if sspm == 0:

                        slow_type("Hvorfor vil du stikke av?")
                        sspm +=1
                        time.sleep(1)
                        clear()
                    elif sspm == 1:
                        slow_type("Du ville dette")
                        time.sleep(1)
                        clear()
                elif a == "c":
                    gammelMann.stats()
            if monsterID == 10:
                global f
         
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
            #lage metode for å displaye hvilket item som er i bruk. Er det mulig å putte en if-setning
            #i en print funksjon? Evt displate x for i bruk, og mellomrom for ikke i bruk, eller (i bruk)?
            if len(self.inv) == 0:
                print("")
                print("Du har ingen items!")
                break
            print(f"-{hero.name}'s inventory-")
            print("")
            print("Skriv inn tallet du objektet du vil vite mer om,")
            print('eller skriv "b" for å gå tilbake')
            global itemSelected
            if len(self.inv) >= 1:
                print(f"1: {self.inv[0].name} {'(selected)' if itemSelected == 0 else ' '}")
                if len(self.inv) >= 2:
                    print(f"2: {self.inv[1].name} {'(selected)' if itemSelected == 1 else ' '}")
                    if len(self.inv) >= 3:
                        print(f"3: {self.inv[2].name} {'(selected)' if itemSelected == 2 else ' '}")
                        if len(self.inv) == 4:
                            print(f"4: {self.inv[3].name} {'(selected)' if itemSelected == 3 else ' '}")
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
                clear()
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
    def itemOptions(self,itemIndex):
        print(f"-{hero.inv[itemIndex].name}-")
        print("")
        print('trykk "s" for å se stats')
        print('trykk "k" for å kaste')
        print('trykk "b" for å bruke')
        print('trykk en annen for å gå tilbake')

        a = input(f"Hva vil du gjøre med {self.inv[itemIndex].name}?")
        clear()
        if a == "k":
            self.itemRemove(itemIndex)
        if a == "s":
            self.iStats(itemIndex)
        if a == "b":
            print(f"Du velger å bruke {hero.inv[itemIndex].name}")
            time.sleep(1)
            global itemSelected
            itemSelected = itemIndex
            


    def itemRemove(self,itemIndex):
        global itemSelected
        if len(self.inv) == 1:
            self.inv.clear()
            if itemSelected == itemIndex:
                print(f"Våpenet du bruker ble kastet. Når du får ett item, vil det bli valgt automatisk")
                itemSelected = 0

        else:
            del self.inv[itemIndex]
            if itemSelected == itemIndex:
                print(f"Våpenet du bruker ble kastet. {hero.inv[0].name} ble valgt automatisk.")
                itemSelected = 0
            elif itemSelected > itemIndex:
                itemSelected -= 1
            #testing:
            #print(itemSelected, "itemSelected")
            #print(itemIndex,"itemIndex")
            #VIKTIG. Finne ut hvilket item som brukes, og selecte det igjen.
            #Hvis feil våpen brukes, endre elif-koden over
        
        

    def iStats(self,i):
        print("")
        print(f"Navn: {self.inv[i].name}")
        print(self.inv[i].desc)
        print(f"Skade: {self.inv[i].dmg}")
    
    def stats(self):
        clear()
        print(f"liv: {self.hp}")
        print(f"level: {self.lv}")
        print(f"damage: {self.dmg}")
        print(f"xp: {self.xp}")
        time.sleep(2)
        print("")

    
    def victory(self,monsterID,monsterNr):
        #hvis ett monster dør:

        print(f"{monsterList[monsterID-1].name} døde")
        self.xp += monsterList[monsterID-1].xp
        print("du fikk",monsterList[monsterID-1].xp,"xp")
        while self.xp >= 10:
            time.sleep(0.5)
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
            slow_type("du vant!")
            time.sleep(3.4)
            return monsterKilled
        else:
            clear()
            print("kampen fortsetter")
            slow_type(f"det er {monsterNr} monstre igjen")
            print("")
            time.sleep(1)
            return monsterKilled #returnerer hvor mange monstre som er drept
        
    def combat(self,monsterID,monsterNr):
        monsterList[monsterID-1].hp = monsterList[monsterID-1].hp-self.dmg*hero.inv[itemSelected].dmg
        print(f"Du angriper og gjør {self.dmg*hero.inv[itemSelected].dmg} skade")
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
            clear()
            hero.invOpen()

    def combatAction(self):
        print("")
        time.sleep(1)
        print('trykk "f" for å sloss')
        print('trykk "r" for å stikke av')
        print('trykk "s" for å se stats')
        print('trykk "c" for å se fienden sine stats')
        print('trykk "i" for å åpne inventory')
        a = input("hva gjør du? ")
        clear()

        if a == "f":
            return "f"
        if a == "r":
            return "r"
        if a == "s":
            hero.stats()
        if a == "c":
            return "c"
        if a == "i":
            clear()
            hero.invOpen()
        
    def death(self):
        clear()
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

            #vanlige events
            slow_type(self.eventText)
            print("")
            print("")
            time.sleep(1)
            if self.monsterAmount == 1:
                if r.randint(1,6) == 1:
                    print("du reagerer fort og angriper!")
                    hero.combat(self.monsterSpawn,self.monsterAmount)
                

                while monsterList[self.monsterSpawn-1].hp > 0:
                    if r.randint(1,12) == 6:
                        print(f"{monsterList[self.monsterSpawn-1].name} har demens, og glemmer derfor å angripe")

                    else:
                        monsterList[self.monsterSpawn-1].combat()
                    
                    action = hero.combatAction()  #actions11
                    if action == "f":
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
                    
                    action = hero.combatAction()  #actions
                    if action == "f":
                        self.monsterAmount-=hero.combat(self.monsterSpawn,self.monsterAmount)
                        
                    if action =="r":
                        print("du stakk av")
                        hero.coward +=1
                        self.monsterAmount = 0
                        break
                    if action =="c":
                        monsterList[self.monsterSpawn-1].stats()
            clear()
        
            print("")
        elif self.specialEvent == True:
            if self.eventID == 1:   #spesialevent 1
                tMats = False
                while True:
                    hasMats = False
                    for i in range(len(hero.inv)):
                        if "Tre" in hero.inv[i].name:
                            hasMats = True
                            matsLocation = i
                            break
                    if hasMats == True and tMats == False:
                        slow_type(self.eventText)
                        print("")
                        print("")
                        slow_type("Ninja: Du har mats!!!")
                        print("")
                        slow_type("Kan jeg få? Jeg trenger for å drepe tFue i moisy mire")
                        print("")
                        time.sleep(0.5)
                        a = input('Gir du han? Skriv inn "y" for ja og "n" for nei')
                        if a == "y":
                            hero.itemRemove(i)
                            clear()
                            print(f"Ninja: takk {hero.name}")
                            print("")
                            tMats = True
                            event3.eventText = "Inne finner du Ninja fra Fortnite. Han er takknemlig for at du ga han mats, og planlegger å straks dra til moisty mire"
                            hero.itemAdd(fortniteScar)
                            print("Ninja ga deg en legendarisk scar fra Fortnite!")
                        if a =="n":
                            clear()
                            print("Ninja: Triste saker, trodde du var bedre enn dette. Nå kan jeg aldri drepe tFue.")
                            tMats = True
                            event3.eventText = "Inne finner du Ninja fra Fortnite. Han er sint fordi du ikke ga han mats, selv om du har det på deg. Du burde kanskje ikke bli her lenge"
                    else:
                        print(self.eventText)
                        a = hero.eAction()
                        if a == "c":
                            monsterList[self.monsterSpawn-1].stats()
                        if a == "f": #helten sloss mot tyler
                            clear()
                            print('Ninja: Feil valg')
                            hero.bossFight(self.monsterSpawn)
                            break
                            
                        if a == "r":
                            print("")
                            print("Ninja: Du løper fra meg???")
                            print("Du løp fra Ninja")
                            hero.coward +=1
                            break
            elif self.eventID == 2: #spesialevent 2
                fspm = 0
                while True:
                    slow_type(self.eventText)
                    print("")
                    a = hero.eAction()
                    clear()
                    if a == "c":
                        monsterList[self.monsterSpawn-1].stats()
                    if a == "f": #helten sloss mot den gamle mannen
                        clear()
                        if fspm == 0:
                            slower_type("... ",2)
                            time.sleep(1)
                            slower_type('"nei"',10)
                            print("")
                            time.sleep(1)
                            fspm +=1
                            eventGammelMann.eventText = "Rodrik lurer på hva du faktisk vil"
                            clear()
                        elif fspm == 1:
                            slower_type("... ",2)
                            time.sleep(1)
                            slower_type('"ikke"',10)
                            print("")
                            time.sleep(1)
                            fspm +=1
                            eventGammelMann.eventText = "Rodrik ser skrekkslagen ut"
                            clear()
                        elif fspm == 2:
                            slower_type("...",2)
                            time.sleep(2)
                            hero.bossFight(self.monsterSpawn)
                            break
                        #break
                        
                    if a == "r":
                        print("")
                        print('"Hade på badet!"')
                        time.sleep(0.5)
                        slow_type("Du gikk fra den gamle mannen")
                        time.sleep(1)
                        clear()
                        hero.coward +=1
                        break
            elif self.eventID == 204:
                while True:
                    slow_type(self.eventText)
                    print("")
                    time.sleep(1)
                    a = hero.combatAction()
                    if a == "c":
                        monsterList[self.monsterSpawn-1].stats()
                    elif a == "f":
                    
                        #sloss mot politimannen
                        sloss
                    elif a == "r":
                        #prøver å stikke av
                        sloss
                    if politi.hp <= 0:
                        vinn

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
            slow_type(self.eventText)
            time.sleep(1)
            print("")
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
            clear()
            if "i" in self.options and a == "i":
                hero.invOpen()
            if "n" in self.options and a == "n":
                if self.id == 1: #spesiell melding for event 1
                    print("Du forblir utenfor")
                    break
                elif self.id == 2:
                    print("Du går ikke ut")
                    wEventTomtHusIn.worldEvent()
                elif self.id == 3:
                    print("Du går videre")
                    global skipFactor
                    skipFactor =+1
                    break
                elif self.id == 201:
                    politiFight.event()
                    global pFight
                    pFight = True
                    break
                elif self.id == 202:
                    print("du åpner ikke kisten")
                    break
                elif self.id == 4:
                    print("Du plukker ikke opp sverdet")
                    break
                elif self.id == 5:
                    print("Du plukker ikke opp steinen")
                    break
                else: #ordinær melding
                    break

            if "y" in self.options and a =="y":
                if self.id == 1: #spesiell melding for event 1
                    print("Du går inn")
                    event3.event()
                    break
                elif self.id == 2: #spesiell melding for event 2
                    print("du går ut")
                    wEventTomtHusUt.worldEvent()
                    break
                elif self.id == 202:
                    hasScar = False
                    for i in range(len(hero.inv)):
                        if "Fortnite Scar" in hero.inv[i].name:
                            hasScar = True
                            break
                    if hasScar == True:
                        slower_type("...",2)
                        print("")
                        time.sleep(0.5)
                        slow_type("Kisten er tom :( ")
                        print("")
                        time.sleep(1)
                        clear()
                        break
                    else:
                        wEventTomtHuskiste.worldEvent()
                        break
                elif self.id == 203:
                    print("Velger å plukke opp Fortnite Scar")
                    hero.itemAdd(fortniteScar)
                    break
                elif self.id ==3:
                    eventGammelMann.event()
                    break
                elif self.id == 4:
                    clear()
                    print("Du plukker opp sverdet!")
                    hero.itemAdd(bandittSverd)
                    break
                elif self.id == 5:
                    clear()
                    print("Du plukker opp steinen")
                    hero.itemAdd(skarpStein)
                    break
                else: #ordinær melding
                    break
             
            if "c" in self.options and a =="c":
                if self.id ==1: #spesiell melding for evnent 1
                    if r.randint(1,2) == 1:
                        print("Du fant litt tre!")
                        print("")
                        hero.itemAdd(mats)
                    else:
                        print('"Ett hus"')
                        print("")
            if "s" in self.options and a =="s":
                hero.stats()

    def worldEvent(self):
        self.worldEventOptions()


class item:
    def __init__(self,name,desc,dmg):
        self.name = name
        self.desc = desc
        self.dmg = dmg



wEvent1 = wEvent("Du kommer til ett hus. Går du inn?",["y","n","i","c","s"],["y","n","i","c","s"],1)
wEventTomtHus = wEvent("Huset er tomt. Ninja sin døde kropp råtner på gulvet. Vil du gå ut?",["y","n"],["y","n"],2)
wEventTomtHusUt = wEvent("Poltiet: Dette er politiet, kom ut med hendene bak ryggen. Følger du det de sier?",["y","n"],["y","n"],201)
wEventTomtHusIn = wEvent("Ninja sin døde kropp råtner fortsatt på gulvet. Men du ser en Kiste! vil du åpne den?",["y","n"],["y","n"],202)
wEventTomtHuskiste = wEvent("I kisten fant du en scar!",["y","n"],["y","n"],203)
wEvent2 = wEvent("Videre på din reise finner du en by. En gammel mann sitter forran ett hus på en knirkete gyngestol. Går du bort til mannen?",["y","n"],["n","n"],3)
wEventBandittSverd = wEvent("Banditten mistet ett sverd! Vil du plukke det opp?",["y","n"],["n","n"],4)
wEventSkarpStein = wEvent("Gnomen mistet en skarp stein! Vil du plukke den opp?",["y","n"],["n","n"],5)

mats = item("Tre","Litt tre du fant. Ubrukelig",0)
fortniteScar = item("Fortnite Scar","Legendary scar assault rifle fra Fortnite. Gjør veldig mye skade",27)
starterPinne = item("Pinne","En veldig fin pinne. Ligner svært på en pistol",1)
Fortnite_Builder_Plan = item("Fortnite_Builder_Plan","?????????","????")
bandittSverd = item("Sverd","Ett helt ordinært sverd. Ble funnet på en banditts døde kropp.", 5)
skarpStein = item("Skarp Stein","En skarp stein du fant på en gnom",2)

event1 = event(1,1,"Ett monster angriper deg!",False,101)
event2 = event(2,3,"En gjeng med monstere angriper deg!",False,102)
event3 = event(3,1,"Inne finner du Ninja fra Fornite. Han spør om du har noe materialer til han. Til gjengjeld sier han at han kan gi deg noe spesielt tilbake.",True,1)
eventGammelMann = event(4,1,"Rodrik hilser deg velkommen.",True,2)
event4 = event(5,1,"En banditt angriper deg!",False,103)
politiFight = event(7,1,"Du sloss mot politiet!",True,204)


monster1 = monster(1,1,1,1,1,"Gnom")
monster2 = monster(1,1,1,1,1,"bob")
monster3 = monster(10,10,27,"boogie bomb",40,'Tyler "Fortnite Ninja" Blevins')
gammelMann = monster(1,1,0,"alt",1,"Rodrik")
monster4 = monster(10,2,2,"penger",2,"banditt")
shopkeeper = monster(100,10,40,"å være hyggelig",1,"Mohammed Zumbul")
politi = monster(104,10,10,"Fortnite Scar",17,"politimann")
tank = monster(20000,40,80,None,4000,"M1 A2 Abrahams main battle tank")




hero = hero(30,1,1,1,1,"geir",False,1)


itemSelected = 0
skipFactor = 0
badOmen = False
arrestert = False
pFight = False

monsterList = []
monsterList.append(monster1)
monsterList.append(monster2)
monsterList.append(monster3)
monsterList.append(gammelMann) #id = 4
monsterList.append(monster4)
monsterList.append(shopkeeper)
monsterList.append(politi) 
monsterList.append(tank) #id = 8
"""

slow_type("Velkommen til dette spillet")
time.sleep(1)
print("")
hero.name=input("Hva heter du?")
print("")
slower_type("ok",5)
time.sleep(0.5)
print("")
slow_type("Du får en pinne for å komme i gang")
time.sleep(1)
clear()
hero.inv.append(starterPinne)

#teste inventory:
#hero.inv.append(starterPinne)
#hero.inv.append(starterPinne)
#ero.inv.append(starterPinne)

#hero.invOpen()


#🤓
"""

hero.itemAdd(fortniteScar)
wEventTomtHus.worldEvent()
if pFight == False:
    #ringe saul??
    #wEventAdvokat()
    #Hvis man tar plea deal kommer man i arbeidsleir, ellers havner man i fengsel som om man hadde sloss mot politet
    print("")

"""
event1.event()
if monster1.hp == 0:
    wEventSkarpStein.worldEvent()
time.sleep(2)
clear()

event2.event() #flere monstere

#event3.event()
wEvent1.worldEvent() #huset

#spillets gang:
time.sleep(2)
clear()
if monster3.hp <= 0: #om ninja er død
    wEventTomtHus.worldEvent() 
    #if pFight == True:
        #sloss mot politiet
        #if arrestert = False:
            #finne en datamaskin for å spille among us/fortnite
        #else:
            #fengsel
            #if hero.inv has fortnitebuilderplan and mats:
                #bygge seg ut av fengsel
            #else:
                #sitte i fengsel til man dør av alder
    #else:
        #arbeidsleir. Ende opp med samme ending som fight med shopkeeper uten badomen?

else: #om man ikke velger å sloss mot ninja
    wEvent2.worldEvent() #gammel mann i byen
    if gammelMann.hp <= 0: #lagrer badOmen for å sloss med djevel
        badOmen = True
    clear()
    print("Du går videre!")
    time.sleep(1)
    event4.event() #banditt
    time.sleep(1)
    if monster4.hp <= 0:
        wEventBandittSverd.worldEvent() #bandittsverd
    time.sleep(2)
    
    #butikk. Kjøpe eller snakke med inbyggere
    #if fight med shopkeeper and badomen == True:
        #djevel bossfight
    #elif fight med shopkeeper:
        #ta over butikken
        #kjøpe opp flere og flere butikker
        #adventure capitalism type beat
    #else:
        #if skipfactor = 3:
            #fuck you for å skippe alt
            #fighte meg. garantert å tape?
        #else:
            #????
"""
#legge til at itemet blir deselecta når ett item blir fjernet. - skal være fikset, men vet ikke sikkert

#VIKTIG! kan ikke se hvor mye skade fiende gjør
#Redesigne combatUI. Skrive skade og hvem som angriper i en setning - fikset, men kanskje ikke helt fornøyd?