import random
import os

class Monster:
    def __init__(self,navn,iq,juks):
        self.navn = navn
        self.iq = iq
        self.juks = juks
    def __str__(self):
        return(f'Din motstander er {self.navn} som ikke liker å tape, og med sin iq på {self.iq}, vil han knuse deg! Han kan muligens jukse litt, men {self.navn} er et monster, hva skal du gjøre?')


class Spiller:
    def __init__(self,navn,iq,flaks):
        self.navn = navn
        self.iq = iq
        self.flaks = flaks
    
    def __str__(self):
        return(f'Karakteren {self.navn} har en iq på hele {self.iq}!')
    
arne = Spiller("Arne", 140,0)
per = Spiller("Per", 110,1)

print('Dette spillet går ut på å spille blackjack mot en monster, er du klar?')

print(arne)
print(f'{per}, men Per har til gjengjeld super mye flaks!')
karakter = input(f'Velg hvilken karakter du vil ha: For Arne trykk 1, og for Per trykk 2: ')

if karakter == 1:
    print(f' Du valgte Arne, han er min favoritt :)')
else:
    print(f'Du valgte Per, han er en flink gutt :)')

greven = Monster("Greven",350,1)

print(greven)

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
    else:
        print("Hade!")
        exit()

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
        else: total+= 11
        total += card
    return total

def hit(hand):
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
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