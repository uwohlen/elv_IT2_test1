import random
import os
import sys, time

def slow_type(t):
    typing_speed = 1500 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

class Monster: #konstruktør for monstere
    def __init__(self,navn,iq,juks):
        self.navn = navn
        self.iq = iq
        self.juks = juks

class Spiller: #konstruktør for karakterer
    def __init__(self,navn,iq,flaks):
        self.navn = navn
        self.iq = iq
        self.flaks = flaks
    
    def __str__(self):
        return(slow_type(f'Karakteren {self.navn} har en iq på hele {self.iq}.'))

arne = Spiller("Arne",140,1)
per = Spiller("Per",110,3)
greven = Monster("Greven",100,1)


'''slow_type('Velkommen til monster BlackJack!\n')'''
slow_type(f'En dag blir du sugd inn i en annen verden, og den eneste måten å komme seg hjem igjen er å spille BlackJack\n')
slow_type(f'Desverre for deg er du nødt til å bekjempe en rekke monstere for å seire og returnere hjem trygt\n')
print('\n')

print(f'[1]Karakter: {arne.navn}    IQ: {arne.iq}      Flaks: Middels')
print(f'[2]Karakter: {per.navn}     IQ: {per.iq}      Flaks: Høy')
print(f'[I]Info om egenskaper\n')

karakter = 0
while True:
    karakter = input('Velg hvilken karakter du vil bruke i ditt eventyr: ').lower()
    if karakter == "1":
        slow_type('Du valgte Arne, han er min favoritt :)                       \n')
        break
    elif karakter == "2":
        slow_type('Du valgte Per, han er en flink gutt :)                       \n')
        break
    elif karakter == "i":
        slow_type(f'IQ: Øker sjanse for å tape mindre penger\n')
        slow_type(f'Flaks: Øker sjanse for å vinne mer penger\n')
    else:
        slow_type("Bruh, du hadde 1 oppgave :/\n")

slow_type(f'Ditt første hinder er selveste Greven som er kjent i BlackJack verdenen for å knuse nybegynnere som deg!\n')
slow_type(f'Det sies at Monster-BlackJack er litt annerledes enn vanlig BlackJack, fordi man vinner kun når man har tatt livet til motstanderen sin\n')


def regler():
    slow_type(f'Generelle Blackjack regler\n')
    slow_type(f'\n')
    slow_type(f'Blackjack er et klassisk casinobordspill, og spilles av mange casinospillere verden over. \n') 
    slow_type(f'Kortspillets regler er enkle å lære seg: Målet er å få en kortverdi lik 21, eller nærmest. \n') 
    slow_type(f'Enkelt forklart fungerer spillet slik:\n')
 
    slow_type(f'● Før spillet starter må du legge en innsats på bordet. \n')
    slow_type(f'● Deretter blir det delt ut to kort hver til dealer og spiller.\n')
    slow_type(f'● Dealeren får ett av sine kort med billedsiden opp. \n')
    slow_type(f'● Etter de to første kortene er delt ut kan du velge om du ønsker å få tildelt et tredje kort. \n')
    slow_type(f'● Utfallet i kortspillet er basert på tilfeldigheter, noe som gjør spillet ekstra spennende. \n')
    slow_type(f'● Du spiller alene mot dealeren. \n')
    slow_type(f'● Du kan ikke overstige 21. \n')
    slow_type(f'● Blackjack kan spilles med to eller flere kortstokker (i noen spillvarianter bruker man opptil åtte kortstokker).\n')
    slow_type(f'● I mange Blackjack-varianter har du muligheten til å splitte hånden for å unngå å overstige verdien av 21. \n')
 
    slow_type(f'Dealeren avslører sine kort til sist, og det er da den som er nærmest 21 som vinner. \n')
 
    slow_type(f'Kortverdiene fungerer slik: \n')
 
    slow_type(f'● Alle tallkort er verdt sin egen verdi \n')
    slow_type(f'● Alle billedkort er verdt 10\n')
    slow_type(f'● Ess er verdt 1 eller 11, avhengig av spillet\n')



deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
vinn = 0
tap = 0
penger = 1000



def deal(deck): #Definerer funksjonen for å dele ut kort
    hand = []
    for i in range(2):
        random.shuffle(deck)
        kort = deck[random.randint(0,51)]
        if kort == 11:
            kort = "J"
        if kort == 12:
            kort = "Q"
        if kort == 13:
            kort = "K"
        if kort == 14:
            kort = "A"
        hand.append(kort)
    return hand



def play_again(): #Definerer funksjonen for å spille på nytt
    while True:
        again = input("Vil du spille igjen eller besøke butikken? [J]ja, [N]Nei og [B]Butikk : ").lower()
        if again == "j":
            clear()
            dealer_hand = []
            player_hand = []
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
            game()
            break
        elif again == "n":
            print("Greven var vel for skummel!\n")
            exit()
        elif again == "b":
            sjappe()



items = []
butikk = ["[G]glock9: 50.000$","[A]ammo: 5.000$","[V]vitaminer: 2.500$"]
bonus = 0
g = butikk.index("[G]glock9: 50.000$")
a = butikk.index("[A]ammo: 5.000$")
v = butikk.index("[V]vitaminer: 2.500$")

def sjappe():
    global penger
    global bonus
    clear()
    print(f'♣♠♦♥BUTIKK♥♦♠♣            Balanse: {penger}$')
    for i in range(len(butikk)):
        print(butikk[i])
    print("\n")
    while True:
        gjenstand = input(f'For å kjøpe gjenstander skriv bokstaven i parantesen til gjenstanden. \nFor å gå tilbake trykk[T]: ').lower()
        if gjenstand == "g" and penger >= 50000:
            items.append("Glock9")
            butikk.remove("[G]glock9: 50.000$")
            penger -= 50000
            slow_type("Takk for kjøpet!\n")                        
            slow_type(f'Din nye balanse er: {penger}$                                                      \n')
            break
        elif gjenstand == "g" and penger < 50000:
            slow_type("Du har ikke råd ha deg ut av sjappa mi, fattiglus!                                  \n")
            break
        if gjenstand == "a" and penger >= 5000:
            items.append("Ammo")
            butikk.remove("[A]ammo: 5.000$")
            penger -= 5000
            slow_type("Takk for kjøpet!\n")
            slow_type(f'Din nye balanse er: {penger}$                                                         \n')
            break
        elif gjenstand == "a" and penger < 5000:
            slow_type("Du har ikke råd ha deg ut av sjappa mi, fattiglus!                                  \n")
            break
        if gjenstand == "v" and penger >= 2500:
            items.append("Vitaminer")
            butikk.remove("[V]vitaminer: 2.500$")
            penger -= 2500
            bonus += 2
            slow_type("Takk for kjøpet!\n")
            slow_type(f'Din nye balanse er: {penger}$                                                         \n')
            break
        elif gjenstand == "v" and penger < 2500:
            slow_type("Du har ikke råd ha deg ut av sjappa mi, fattiglus!                                  \n")
            break
        elif gjenstand != ("g","a","v"):
            slow_type("Du skrev ikke inn en bokstav som samsvarer med noen av alternativene :(\n")
        if gjenstand == "t":
            break


                        


        game()



def total(hand): #Definerer funksjonen for å finne sum av utdelt kort
    total = 0
    for kort in hand:
        if kort == "J" or kort == "Q" or kort == "K":
            total+= 10
        elif kort == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += kort
    return total



def hit(hand): #Definerer funksjonen for å hitte hånden, altså få et ekstra kort delt ut
    random.shuffle(deck)
    kort = deck[random.randint(0,51)]
    if kort == 11:
        kort = "J"
    if kort == 12:
        kort = "Q"
    if kort == 13:
        kort = "K"
    if kort == 14:
        kort = "A"
    hand.append(kort)
    return hand



def DrepeGreven():
    if "Ammo" in items:
        slow_type("Du tok frem en glock9 og gætta ned Greven. \nPå grunn av dine handlinger har du nå gjort tre snille barn fatherles :(\n")
        exit()
    if "Ammo" not in items:
        slow_type("Du må ha ammo, kan ikke drepe et monster uten kuler :)                                    \n")
        play_again()



def clear(): #Definerer funksjonen for å fjerne tekst i terminalen
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')



def print_results(dealer_hand, player_hand): #Definerer funksjonen for å printe ut midlertidlige resultater til terminalen
	'''clear()'''
	slow_type(f'Greven fikk: {str(dealer_hand)}, som tilsvarer: {str(total(dealer_hand))}\n')
	slow_type(f'Du har: {str(player_hand)}, som tilsvarer: {str(total(player_hand))}\n')

def gevinst():
    global penger
    global gamble
    global bonus
    penger += gamble * (1 + random.randint(0,bonus)/10)
    return penger

def tapepenger():
    global penger
    global gamble
    global bonus
    penger -= gamble
    return penger


def flaks():
    global penger
    global gamble
    if karakter == "1":
        n = random.randint(1,int(arne.flaks))
        if n > 2:
            penger += (1.1 + (int(arne.flaks)/10)) * gamble
        else:
            gevinst()
    if karakter == "2":
        n = random.randint(1,int(per.flaks))
        if n > 2:
            penger += (1.1 + (int(per.flaks)/10)) * gamble
        else:
            gevinst()


def iq():
    global penger
    global gamble
    global penger
    global gamble
    if karakter == "1":
        m = random.randint(1,int(arne.iq))
        if m > int(arne.iq)*0.7:
            penger -= (1 - (2 * int(arne.iq) / 1000)) * gamble
        else:
            tapepenger()
    if karakter == "2":
        m = random.randint(1,int(per.iq))
        if m > int(per.iq)*0.7:
            penger -= (1 - (2 * int(per.iq) / 1000)) * gamble
        else:
            tapepenger()


def blackjack(dealer_hand, player_hand): #Definerer funksjonen for å oppgi dersom noen har fått blackjack
    global vinn
    global tap
    global penger
    global gamble
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        slow_type("Gratulerer! Du fikk Blackjack!\n")
        vinn += 1
        flaks()
        slow_type(f'Din nye balanse er: {penger}$\n')
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)		
        slow_type("Desverre var Greven bare bedre enn deg og fikk Blackjack.\n")
        tap += 1
        iq()
        slow_type(f'Din nye balanse er: {penger}$\n')
        play_again()



def score(dealer_hand, player_hand): #Definerer funksjonen for å printe ut endelige resultater til terminalen
    global vinn
    global tap
    global penger
    global gamble
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        slow_type("Gratulerer! Du fikk Blackjack!\n")
        vinn += 1
        flaks()
        slow_type(f'Din nye balanse er: {penger}$\n')
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)		
        slow_type("Desverre var Greven bare bedre enn deg og fikk Blackjack.\n")
        tap += 1
        iq()
        slow_type(f'Din nye balanse er: {penger}$\n')
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        slow_type("Desverre busta du, altså gikk over 21, og dermed tapte :(\n")
        tap += 1
        iq()
        slow_type(f'Din nye balanse er: {penger}$\n')
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)			   
        slow_type("Greven busta, altså gikk over 21, og dermed vant du!\n")
        vinn += 1
        flaks()
        slow_type(f'Din nye balanse er: {penger}$\n')
    elif int(total(player_hand)) < int(total(dealer_hand)):
        print_results(dealer_hand, player_hand)
        slow_type("Beklager, hånden din er lavere enn Greven sin, og du taper!\n")
        tap += 1
        iq()
        slow_type(f'Din nye balanse er: {penger}$\n')
    elif int(total(player_hand)) > int(total(dealer_hand)):
        print_results(dealer_hand, player_hand)			   
        slow_type("Gratulerer, hånden din er høyere enn Greven sin, og dermed vant du!\n")
        vinn += 1
        flaks()
        slow_type(f'Din nye balanse er: {penger}$\n')
    

while True:
    starte_spill = input(f'Er du opp for utfordringen, eller trenger du kanskje regler til BlackJack først? [J]Ja / [N]Nei / [R]Regler: ').lower()
    if starte_spill == "j":
        break
    elif starte_spill == "n":
        slow_type(f'Vel jeg ville ikke gått unna denne sjansen om jeg var deg, men da får du vel bare kose deg i monsterverdenen haha')
        exit()
    elif starte_spill == "r":
        regler()

def game(): #Definerer spillets gang :)
    global vinn
    global tap
    global penger
    global gamble
    choice = 0
    clear()
    if penger < 50:
        penger += 100
    print("♣♠♦♥GREVENS BLACKJACK♥♦♠♣")
    slow_type(f' seiere: {vinn}       tap: {tap}\n')
    slow_type(f'Balanse: {penger}$\n')
    print("Dine gjenstander:")
    print(arne.flaks)
    print(per.flaks)
    for i in range(len(items)):
        print(items[i])
    print("\n")
    while True:
        gyldig = False
        while not gyldig:
            gamble = input(f'Skriv inn mengden $ du vil gamble: ')
            try:
                gamble = int(gamble)
                gyldig = True
            except ValueError:
                print("Du må skrive inn et heltall din bruh.")
        penger = int(penger)
        if gamble > penger:
            slow_type(f'Skulle ønske du hadde så mye penger lmao\n')
        elif gamble < 0:
            slow_type(f'Ayo? Du vil at Greven skal spandere betten for deg?\n')
        elif gamble <= penger:
            slow_type(f'Du betta: {gamble}\n')
            break
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    blackjack(dealer_hand, player_hand)
    slow_type(f'Du fikk kortene: {(player_hand)} som betyr at du har summen: {(total(player_hand))}\n')
    while choice != "a":
        if "Glock9" not in items:
            choice = input("Vil du: [H]Slå, [S]stå eller [A]Avslutte: ").lower()
        else:
            choice = input("Vil du: [H]Slå, [S]stå, [A]Avslutte eller [G]Glock9: ").lower()
        '''clear()'''
        if choice == "h":
            hit(player_hand)
            if total(player_hand) == 21:
                blackjack(dealer_hand, player_hand)
            slow_type(f'Du har: {str(player_hand)}, som tilsvarer: {str(total(player_hand))}\n')
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            if total(player_hand)>21:
                slow_type("Desverre busta du, altså gikk over 21, og dermed tapte :(\n")
                slow_type(f'Din nye balanse er: {penger}$\n')
                tap += 1
                penger -= gamble
                play_again()
        elif choice == "s":
            if total(dealer_hand) >= 17:
                score(dealer_hand,player_hand)
                play_again()
            else:
                while total(dealer_hand) < 17:
                    hit(dealer_hand)
                score(dealer_hand,player_hand)
                play_again()
        elif choice == "a":
            slow_type("Greven var vel for skummel!\n")
            exit()
        elif choice == "g" and "Glock9" in items:
            DrepeGreven()

if __name__ == "__main__":
    game()

#I fremtiden skal det legges til:
#oversikt over tap og seiere xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#Valuta xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#Valuta kan brukes for å drepe Greven xxxxxxxxxxxxxxxxxxxx
#Juks, flaks og iq skal spille en rolle
#Flaks skal gjøre at noen ganger så mister man ikke penger siden greven glemmer å ta dem
#Iq skal gjøre at man får ekstra bonuser/multipliers for gevinstene sine
#Juksing kan gjøre at greven ikke gir tilbake den summen man skal ha
#legge til voicelines for Greven basert på randint genererte nummere, disse blir printa etter hvert game
#legge til en butikk hvor du kan kjøpe oppgraderinger, og glock for å drepe Greven xxxxxxxxxxxxxxx