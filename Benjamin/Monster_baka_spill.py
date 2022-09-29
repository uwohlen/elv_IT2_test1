import random
import os
import sys, time

def slow_type(t):
    typing_speed = 15000 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

class Monster: #konstruktør for monstere
    def __init__(self,navn,iq,juks):
        self.navn = navn
        self.iq = iq
        self.juks = juks
    def __str__(self):
        return(f'Din motstander er {self.navn} som ikke liker å tape, og med sin iq på {self.iq}, \nvil han knuse deg! Han kan muligens jukse litt, men {self.navn} er et monster,\nhva skal du gjøre?                                                                                                          .')


class Spiller: #konstruktør for karakterer
    def __init__(self,navn,iq,flaks):
        self.navn = navn
        self.iq = iq
        self.flaks = flaks
    
    def __str__(self):
        return(slow_type(f'Karakteren {self.navn} har en iq på hele {self.iq}.'))
    
arne = Spiller("Arne", "140","0")
per = Spiller("Per", "70","1")
greven = Monster("Greven","100","1")

slow_type('Dette spillet går ut på å spille blackjack mot et monster, er du klar?\n')

slow_type(f'Karakteren Arne har en iq på hele 140!\n')
slow_type(f'Karakteren Per har en iq på bare 70, men Per har til gjengjeld super mye flaks!\n')
karakter = input('Velg hvilken karakter du vil bruke:\nFor Arne trykk 1, og for Per trykk 2:')

if karakter == "1":
    slow_type(' Du valgte Arne, han er min favoritt :)\n')
    slow_type(f'{greven}\n')
elif karakter == "2":
    slow_type('Du valgte Per, han er en flink gutt :)\n')
    slow_type(f'{greven}\n')


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
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
    again = input("Vil du spille igjen? (Y/N) : ").lower()
    if again == "y":
        clear()
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    else:
        print("Greven var vel for skummel!\n")
        exit()

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

def clear(): #Definerer funksjonen for å fjerne tekst i terminalen
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand): #Definerer funksjonen for å printe ut midlertidlige resultater til terminalen
	'''clear()'''
	slow_type(f'Greven fikk: {str(dealer_hand)}, som tilsvarer: {str(total(dealer_hand))}\n')
	slow_type(f'Du har: {str(player_hand)}, som tilsvarer: {str(total(player_hand))}\n')

def blackjack(dealer_hand, player_hand): #Definerer funksjonen for å oppgi dersom noen har fått blackjack
    global vinn
    global tap
    global penger
    global gamble
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        slow_type("Gratulerer! Du fikk Blackjack!\n")
        play_again()
        vinn += 1
        penger += gamble * 2
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)		
        slow_type("Desverre var Greven bare bedre enn deg og fikk Blackjack.\n")
        play_again()
        tap += 1

def score(dealer_hand, player_hand): #Definerer funksjonen for å printe ut endelige resultater til terminalen
    global vinn
    global tap
    global penger
    global gamble
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        slow_type("Gratulerer! Du fikk Blackjack!\n")
        vinn += 1
        penger += gamble * 2
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)		
        slow_type("Desverre var Greven bare bedre enn deg og fikk Blackjack.\n")
        tap += 1
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        slow_type("Desverre busta du, altså gikk over 21, og dermed tapte :(\n")
        tap += 1
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)			   
        slow_type("Greven busta, altså gikk over 21, og dermed vant du!\n")
        vinn += 1
        penger += gamble * 2
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        slow_type("Beklager, hånden din er lavere enn Greven sin, og du taper!\n")
        tap += 1
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)			   
        slow_type("Gratulerer, hånden din er høyere enn Greven sin, og dermed vant du!\n")
        vinn += 1
        penger += gamble * 2
    

def game(): #Definerer spillets gang :)
    global vinn
    global tap
    global penger
    global gamble
    choice = 0
    clear()
    print("♣♠♦♥GREVENS BLACKJACK♥♦♠♣\n")
    slow_type(f'     seiere: {vinn}       tap: {tap}\n')
    slow_type(f'Balanse: {penger}$\n')
    gamble = int(input(f'Skriv inn mengden $ du vil gamble: '))
    if int(gamble) > int(penger):
        slow_type(f'Skulle ønske du hadde så mye penger lmao\n')
        play_again()
    elif int(gamble) < 0:
        slow_type(f'Ayo? Du vil at Greven skal spandere betten for deg?\n')
        play_again()
    elif gamble <= penger:
        penger = penger - gamble
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    if blackjack(dealer_hand, player_hand) == True:
        blackjack(dealer_hand, player_hand)
        vinn += 1
        penger += gamble * 2
        play_again()
    slow_type(f'Du fikk kortene: {(player_hand)} som betyr at du har summen: {(total(player_hand))}\n')
    while choice != "a":
        choice = input("Vil du: [H]Slå, [S]stå, eller [A]Avslutte: ").lower()
        '''clear()'''
        if choice == "h":
            hit(player_hand)
            if total(player_hand) == 21:
                blackjack(dealer_hand, player_hand)
                play_again()
            slow_type(f'Du har: {str(player_hand)}, som tilsvarer: {str(total(player_hand))}\n')
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            if total(player_hand)>21:
                slow_type("Desverre busta du, altså gikk over 21, og dermed tapte :(\n")
                tap += 1
                play_again()
        elif choice == "s":
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                score(dealer_hand, player_hand)
                play_again()
            if total(dealer_hand) > 17:
                score(dealer_hand,player_hand)
                play_again()
            else:
                score(dealer_hand,player_hand)
                play_again()
        elif choice == "a":
            slow_type("Greven var vel for skummel!\n")
            exit()
if __name__ == "__main__":
    game()

#I fremtiden skal det legges til:
#oversikt over tap og seiere xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#Valuta xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#Valuta kan brukes for å drepe Greven
#Juks, flaks og iq skal spille en rolle
#Flaks skal gjøre at noen ganger så mister man ikke penger siden greven glemmer å ta dem
#Iq skal gjøre at man får ekstra bonuser/multipliers for gevinstene sine
#Juksing kan gjøre at greven ikke gir tilbake den summen man skal ha