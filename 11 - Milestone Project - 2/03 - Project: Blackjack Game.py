import random

from numpy import r_

# Tuples
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Dictionary
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank)) # objects are appended to the array

    def __str__(self):
        deck_com = ''
        for card in self.deck:
            deck_com += '\n' + card.__str__()
        return "The deck has: "+deck_com

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop() # returns the popped object

# deck = Deck()
# print(deck)
# deck.shuffle()
# print('-')
# print(deck)
# print('-')
# print(deck.deal())
# print('-')
# print(deck)


class Hand: # Player
    def __init__(self):
        self.cards = [] 
        self.value = 0   
        self.aces = 0   
    
    def add_card(self, card): # card object in deck class
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# test_deck = Deck()
# test_deck.shuffle()
# test_player = Hand()
# pulled_card = test_deck.deal()
# print(pulled_card)
# test_player.add_card(pulled_card)
# print(test_player.value)
# print(test_player.cards)


class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips): #chips is an object of Chips class 
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet ? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry you don't have enough chips. You have {}".format(chips.total))
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing  
    
    while True:
        x = input('Hit or Stand ? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck, hand)
        
        elif x[0].lower() == 's':
            print("Player stands. Dealer's Turn")
            playing = False

        else:
            print("Sorry, I didnt get it, enter h or s")
            continue
        break


def show_some(player, dealer):
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    

def show_all(player, dealer):
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's hand is: {dealer.value}")
    
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")


def player_busts(chips):
    print('Bust Player!')
    chips.lose_bet()


def player_wins(chips):
    print('Player Wins!')
    chips.win_bet()


def dealer_busts(chips):
    print('Dealer Busted, Player Wins')
    chips.win_bet()


def dealer_wins(chips):
    print('Dealer Wins!')
    chips.lose_bet()


def push():
    print('Dealer and player tie! Push')


playing = True

while True:
    # Print an opening statement
    print('Welcome to BlackJack!')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)

        else:
            push()        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break

