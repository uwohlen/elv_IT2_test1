import random
import os
import sys, time

def slow_type(t):
    typing_speed = 1500 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    
def fast_type(t):
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

slow_type(f'Du har blitt sugd inn i en annen verden, og den eneste måten å komme deg hjem igjen er å spille BlackJack\n')
slow_type(f'Desverre for deg er du nødt til å bekjempe en rekke monstere for å seire og returnere hjem trygt\n')
print('\n')

slow_type('Hvilken karakter vil du bruke i ditt eventyr?\n')
print(f'[1]Karakter: {arne.navn}    IQ: {arne.iq}      Flaks: Middels')
print(f'[2]Karakter: {per.navn}     IQ: {per.iq}      Flaks: Høy')
print(f'[I]Info om egenskaper\n')

karakter = 0
while True:
    karakter = input('Skriv inn tilsvarende symbol: ').lower()
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
    clear()
    fast_type(f'GENERELLE REGLER MONSTER-BLACKJACK\n')
    fast_type(f'\n')
    fast_type(f'Blackjack er et klassisk casinobordspill, og spilles av mange casinospillere verden over. \n') 
    fast_type(f'Kortspillets regler er enkle å lære seg: Målet er å få en kortverdi lik 21, eller nærmest. \n') 
    fast_type(f'Enkelt forklart fungerer spillet slik:\n')
 
    fast_type(f'● Før spillet starter må du legge en bet på bordet. \n')
    fast_type(f'● Deretter blir det delt ut to kort hver til monsteret og deg.\n')
    fast_type(f'● Etter de to første kortene er delt ut kan du velge om du ønsker å få tildelt et tredje kort. \n')
    fast_type(f'● Utfallet i kortspillet er basert på tilfeldigheter, noe som gjør spillet ekstra spennende. \n')
    fast_type(f'● Du spiller alene mot monsteret. \n')
    fast_type(f'● Du kan ikke overstige 21. \n')
    fast_type(f'● Monsteret avslører sine kort til sist, og det er da den som er nærmest 21 som vinner. \n')
    fast_type(f'● Dersom begge to har like høy hånd, vinner monsteret. \n')
    
    fast_type(f'\n')
    fast_type(f'VERIDIER PÅ KORT: \n')
    fast_type(f'● Alle tallkort er verdt sin egen verdi \n')
    fast_type(f'● Alle billedkort er verdt 10\n')
    fast_type(f'● Ess er verdt 11 når du har en hånd vært under 11, og 1 når hånden din er over 11\n')

    fast_type('\n')
    fast_type(f'TREKK\n')
    fast_type(f'I Monster-BlackJack kan du velge ett av disse trekkene når det er din tur:\n')
    fast_type(f'● Slå: Bruk dette trekket for flere kort.\n')
    fast_type(f'● Stå: Du avstår fra å få flere kort.\n')
    fast_type(f'● Avslutt: Du avslutter spillet og forblir evig i monsterverdenen.\n')

    fast_type('\n')
    fast_type(f'HVORDAN VINNE?\n')
    fast_type(f'Det finnes tre utfall som gjør at du vinner dette populære kortspillet:\n')
    fast_type(f'1. Din hånd er høyere enn monsterets hånd til slutt, uten at verdien går over 21.\n')
    fast_type(f'2. Du får ekte Blackjack/21 før monsteret (ess + 10 eller billedkort).\n')
    fast_type(f'3. Monsterets hånd overstiger 21. \n')



deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
vinn = 0
tap = 0
penger = 1000000



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
    again = input("Skriv noe for å spille igjen: ")
    if again == str or int:
        clear()
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()


class Gjenstander: #konstruktør for gjenstander
    def __init__(self,navn,pris,iq,flaks,bonus):
        self.navn = navn
        self.pris = pris
        self.iq = iq
        self.flaks = flaks
        self.bonus = bonus

glock = Gjenstander("[G]Glock9",50000,0,0,0)
ammo = Gjenstander("[A]Ammo",5000,0,0,0)
vitaminer = Gjenstander("[V]Vitaminer",2500,0,0,1)
super_vitaminer = Gjenstander("[S]Super-Vitaminer",25000,0,0,2)
iq_tabletter = Gjenstander("[I]IQ-Tabletter",10000,20,0,0)
guds_velsignelse = Gjenstander("[GV]Guds-Velsignelse",15000,0,2,0)

items = []
butikk = [glock,ammo,vitaminer,super_vitaminer,iq_tabletter,guds_velsignelse]
bonus = 0

def sjappe():
    global penger
    global bonus
    clear()
    print(f'♣♠♦♥BUTIKK♥♦♠♣            Balanse: {penger}$')
    if glock in butikk:
        print(f'{glock.navn}: {glock.pris}$')
    if ammo in butikk:
        print(f'{ammo.navn}: {ammo.pris}$')
    if vitaminer in butikk:
        print(f'{vitaminer.navn}: {vitaminer.pris}$')
    if super_vitaminer in butikk:
        print(f'{super_vitaminer.navn}: {super_vitaminer.pris}$')
    if iq_tabletter in butikk:
        print(f'{iq_tabletter.navn}: {iq_tabletter.pris}$')
    if guds_velsignelse in butikk:
        print(f'{guds_velsignelse.navn}: {guds_velsignelse.pris}$')
    print("\n")
    print('[T]Tilbake')
    while True:
        gjenstand = input(f'Skriv inn tilsvarende symbol: ').lower()
        if gjenstand == "t":
            game()
        elif gjenstand == "g" and glock not in butikk:
            sjappe()
        elif gjenstand == "a" and ammo not in butikk:
            sjappe()
        elif gjenstand == "v" and vitaminer not in butikk:
            sjappe()
        elif gjenstand == "s" and super_vitaminer not in butikk:
            sjappe()
        elif gjenstand == "i" and iq_tabletter not in butikk:
            sjappe()
        elif gjenstand == "gv" and guds_velsignelse not in butikk:
            sjappe()
        elif gjenstand == "g" and penger >= int(glock.pris):
            items.append("Glock9")
            butikk.remove(glock)
            penger -= int(glock.pris)
            slow_type("Takk for kjøpet!\n")                        
            slow_type(f'Din nye balanse er: {penger}$                                                      \n')
            game()
            break
        elif gjenstand == "g" and penger < int(glock.pris):
            slow_type("Du har ikke råd ha deg ut av sjappa mi, fattiglus!                                  \n")
            game()
            break
        elif gjenstand == "a" and penger >= int(ammo.pris):
            items.append("Ammo")
            butikk.remove(ammo)
            penger -= int(ammo.pris)
            slow_type("Takk for kjøpet!\n")
            slow_type(f'Din nye balanse er: {penger}$                                                         \n')
            game()
            break
        elif gjenstand == "a" and penger < int(ammo.pris):
            slow_type("Du har ikke råd ha deg ut av sjappa mi, fattiglus!                                  \n")
            game()
            break
        elif gjenstand == "v" and penger >= int(vitaminer.pris):
            items.append("Vitaminer")
            butikk.remove(vitaminer)
            penger -= int(vitaminer.pris)
            bonus += int(vitaminer.bonus)
            slow_type("Takk for kjøpet!\n")
            slow_type(f'Din nye balanse er: {penger}$                                                         \n')
            game()
            break
        elif gjenstand == "v" and penger < int(vitaminer.pris):
            slow_type("Du har ikke råd ha deg ut av sjappa mi, fattiglus!                                  \n")
            game()
            break
        elif gjenstand == "s" and penger >= int(super_vitaminer.pris):
            items.append("Super Vitaminer")
            butikk.remove(super_vitaminer)
            penger -= int(super_vitaminer.pris)
            bonus += int(super_vitaminer.bonus)
            slow_type("Takk for kjøpet!\n")
            slow_type(f'Din nye balanse er: {penger}$                                                         \n')
            game()
            break
        elif gjenstand == "s" and penger < int(super_vitaminer.pris):
            slow_type("Du har ikke råd ha deg ut av sjappa mi, fattiglus!                                  \n")
            game()
            break
        elif gjenstand == "i" and penger >= int(iq_tabletter.pris):
            items.append("Super Vitaminer")
            butikk.remove(iq_tabletter)
            penger -= int(iq_tabletter.pris)
            arne.iq += int(iq_tabletter.iq)
            per.iq += int(iq_tabletter.iq)
            slow_type("Takk for kjøpet!\n")
            slow_type(f'Din nye balanse er: {penger}$                                                         \n')
            game()
            break
        elif gjenstand == "i" and penger < int(iq_tabletter.pris):
            slow_type("Du har ikke råd ha deg ut av sjappa mi, fattiglus!                                  \n")
            game()
            break
        elif gjenstand == "gv" and penger >= int(guds_velsignelse.pris):
            items.append("Guds Velsignelse")
            butikk.remove(guds_velsignelse)
            penger -= int(guds_velsignelse.pris)
            arne.flaks += int(guds_velsignelse.flaks)
            per.flaks += int(guds_velsignelse.flaks)                
            slow_type("Takk for kjøpet!\n")
            slow_type(f'Din nye balanse er: {penger}$                                                         \n')
            game()
            break
        elif gjenstand == "gv" and penger < int(guds_velsignelse.pris):
            slow_type("Du har ikke råd ha deg ut av sjappa mi, fattiglus!                                  \n")
            game()
            break
        else:
            slow_type("Du skrev ikke inn en bokstav som samsvarer med noen av alternativene :(                                           \n")
            sjappe()
        game()

def statistikk():
    clear()
    if karakter == "1":
        print(f'Navn: {arne.navn}\nIQ: {arne.iq}\nFlaks: {arne.flaks}\nBonus Multiplier: {1 + bonus/10}')
    elif karakter == "2":
        print(f'Navn: {per.navn}\nIQ: {per.iq}\nFlaks: {per.flaks}\nBonus Multiplier: {1 + bonus/10}')
    tilbake1 = input(f'Skriv inn et symbol for å gå tilbake: ')
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
    r = gamble * (1 + random.randint(0,bonus)/10)
    penger += r
    slow_type(f'Du vant: {r}$\n')
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
            o = (1.1 + (int(arne.flaks)/10)) * gamble
            penger += o
            slow_type(f'Du vant: {o}$\n')
        else:
            gevinst()
    if karakter == "2":
        n = random.randint(1,int(per.flaks))
        if n > 2:
            o = (1.1 + (int(per.flaks)/10)) * gamble
            penger += o
            slow_type(f'Du vant: {0}$+n')
        else:
            gevinst()


def iq():
    global penger
    global gamble
    global penger
    global gamble
    if karakter == "1":
        m = random.randint(1,int(arne.iq))
        if m > 100:
            penger -= (1 - (2 * int(arne.iq) / 1000)) * gamble
        else:
            tapepenger()
    if karakter == "2":
        m = random.randint(1,int(per.iq))
        if m > 100:
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
    starte_spill = input(f'Er du opp for utfordringen, eller trenger du kanskje litt regler til Monster-BlackJack først? [J]Ja / [N]Nei / [R]Regler: ').lower()
    if starte_spill == "j":
        break
    elif starte_spill == "n":
        slow_type(f'Vel jeg ville ikke gått unna denne sjansen om jeg var deg, men da får du vel bare kose deg i monsterverdenen haha')
        exit()
    elif starte_spill == "r":
        regler()
    else:
        slow_type(f'Du må skrive inn ett av alternativene :) \n')

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
    slow_type(f'Balanse: {penger}$     Seiere: {vinn}     Tap: {tap}\n')
    slow_type(f'[A]Avslutt      [B]Butikk      [S]Statistikk\n')
    print("Dine gjenstander:")
    for i in range(len(items)):
        print(items[i])
    print("\n")
    while True:
        gyldig = False
        while not gyldig:
            gamble = input(f'Skriv inn mengden $ du vil gamble: ').lower()
            if gamble == "b":
                sjappe()
            if gamble == "a":
                slow_type("Greven var vel for skummel!\n")
                exit()
            if gamble == "s":
                statistikk()
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
        clear()
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
        if choice == "s":
            if total(dealer_hand) >= 17:
                score(dealer_hand,player_hand)
                play_again()
            elif total(dealer_hand) < 17:
                while total(dealer_hand) < 17:
                    hit(dealer_hand)
                score(dealer_hand,player_hand)
                play_again()
            score(dealer_hand,player_hand)
            play_again()
        if choice == "a":
            slow_type("Greven var vel for skummel!\n")
            exit()
        elif choice == "g" and "Glock9" in items:
            DrepeGreven()

if __name__ == "__main__":
    game()


#Juksing kan gjøre at greven ikke gir tilbake den summen man skal ha
#legge til voicelines for Greven basert på randint genererte nummere, disse blir printa etter hvert game
#Man kan bruke glock og ammo for å gjøre skade, ikke nødvendigvis direkte drepe, men greven dør når han er tom for liv
