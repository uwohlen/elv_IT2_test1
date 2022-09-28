import random
import os
import sys, time, random

def slow_type(t):
    typing_speed = 1500 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

class Monster:
    def __init__(self,navn,iq,juks):
        self.navn = navn
        self.iq = iq
        self.juks = juks
    def __str__(self):
        return(f'Din motstander er {self.navn} som ikke liker å tape, og med sin iq på {self.iq}, \nvil han knuse deg! Han kan muligens jukse litt, men {self.navn} er et monster,\nhva skal du gjøre?                                                                                                          .')


class Spiller:
    def __init__(self,navn,iq,flaks):
        self.navn = navn
        self.iq = iq
        self.flaks = flaks
    
    def __str__(self):
        return(slow_type(f'Karakteren {self.navn} har en iq på hele {self.iq}.'))
    
arne = Spiller("Arne", "140","0")
per = Spiller("Per", "70","1")
greven = Monster("Greven","350","1")

slow_type('Dette spillet går ut på å spille blackjack mot et monster, er du klar?\n')

slow_type(f'Karakteren Arne har en iq på hele 140!\n')
slow_type(f'Karakteren Per har en iq på bare 70, men Per har til gjengjeld super mye flaks!\n')
karakter = input('Velg hvilken karakter du vil bruke:\nFor Arne trykk 1, og for Per trykk 2:')

if karakter := 1:
    slow_type(' Du valgte Arne, han er min favoritt :)\n')
    slow_type(f'{greven}\n')
elif karakter := 2:
    slow_type('Du valgte Per, han er en flink gutt :)\n')
    slow_type(f'{greven}\n')


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
    hand = [0,0,0,0,0,0]
    for i in range(2):
        random.shuffle(deck)
        kort = deck.pop()
        if kort == 11:kort = "J"
        if kort == 12:kort = "Q"
        if kort == 13:kort = "K"
        if kort == 14:kort = "A"
        hand[1] = kort
    return hand

def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    else:
        print("Bye!")
        exit()

def total(hand):
    total = 0
    if hand[0] == "J" or hand[0] == "Q" or hand[0] == "K":
        total = total + 10
    elif hand[0] == "A":
            total = total + 11
    elif hand[1]== "J" or hand[1] == "Q" or hand[1] == "K":
        total = total + 10
    elif hand[1] == "A":
        if total >= 11:
                total = total + 1
        elif total < 11: 
                total = total + 11
    elif hand[2]== "J" or hand[2] == "Q" or hand[2] == "K":
        total = total + 10
    elif hand[2] == "A":
        if total >= 11:
                total = total + 1
        elif total < 11: 
                total = total + 11
    elif hand[3]== "J" or hand[3] == "Q" or hand[3] == "K":
        total = total + 10
    elif hand[3] == "A":
        if total >= 11:
                total = total + 1
        elif total < 11: 
                total = total + 11
    else:
        total = hand[0] + hand[1]
    return total


def hit(hand):
	kort = deck.pop()
	if kort == 11:kort = "J"
	if kort == 12:kort = "Q"
	if kort == 13:kort = "K"
	if kort == 14:kort = "A"
	if "0" in hand:
        
	return hand

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def print_results(dealer_hand, player_hand):
	clear()
	print("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
	print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print ("Congratulations! You got a Blackjack!\n")
		play_again()
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		print ("Sorry, you lose. The dealer got a blackjack.\n")
		play_again()

def score(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print ("Congratulations! You got a Blackjack!\n")
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		print ("Sorry, you lose. The dealer got a blackjack.\n")
	elif total(player_hand) > 21:
		print_results(dealer_hand, player_hand)
		print ("Sorry. You busted. You lose.\n")
	elif total(dealer_hand) > 21:
		print_results(dealer_hand, player_hand)			   
		print ("Dealer busts. You win!\n")
	elif total(player_hand) < total(dealer_hand):
		print_results(dealer_hand, player_hand)
		print(f' Beklager, hånden din er lavere enn Greven sin, og du taper!\n')
	elif total(player_hand) > total(dealer_hand):
		print_results(dealer_hand, player_hand)			   
		print ("Congratulations. Your score is higher than the dealer. You win\n")

def game():
    choice = 0
    clear()
    print ("VELKOMMEN TIL BLACKJACK!\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print ("The dealer is showing a " + str(dealer_hand[0]))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)
    quit=False
    while not quit:
        choice = input("Vil du: [H]it, [S]tand, eller [Q]uit: ").lower()
        if choice == 'h':
            hit(player_hand)
            print(player_hand)
            if total(player_hand)>21:
                print('You busted')
                play_again()
        elif choice=='s':
            while total(dealer_hand)<17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand)>21:
                    print('Dealer busts, you win!')
                    play_again()
            score(dealer_hand,player_hand)
            play_again()
        elif choice == "q":
            print("Bye!")
            quit=True
            exit()
if __name__ == "__main__":
   game()