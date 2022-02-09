from operator import le
import random
from unicodedata import name


# Tuples
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Dictionary
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


my_card = Card("Hearts", "Two")
#print(type(my_card))
#print(my_card.suit)


class Deck():
    def __init__(self):
        self.all_cards = [] # list

        for s in suits:
            for r in ranks:
                # Create a Card object
                created_card = Card(s, r)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


new_deck = Deck()
first_card = new_deck.all_cards[-1]
#print(new_deck.all_cards)
#print(first_card)
new_deck.shuffle()
first_card = new_deck.all_cards[-1]
#print(first_card)
my_card = new_deck.deal_one()
#print(my_card)
#print(len(new_deck.all_cards))


class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards)==type([]): # List of multiple card objects
            self.all_cards.extend(new_cards)
        else: # For a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


new_player = Player("Oben")
print(my_card)
new_player.add_cards(my_card)
print(new_player)
print(new_player.all_cards[0])
x = [my_card, my_card, my_card]
for a in x:
    print(a)
new_player.add_cards([my_card, my_card, my_card])
print(new_player.all_cards)
print(new_player)
new_player.remove_one()
print(new_player)


