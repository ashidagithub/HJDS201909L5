# -*- coding: UTF-8 -*-

# author by : Archier
# created:  2019.10.19
# Updated:  2019.10.20

# import some external moduls
import random
import codecs
import copy

# --------------------------------------------------------
# Phase 1:  make a new deck of playing cards
# --------------------------------------------------------
# initialize
#cardJokers = ('Red Joker','Black Joker')
#cardJokers = ('RJ','BJ')
cardJokers = ('♞', '♘')

#cardMarks = ('Heart','Spade','Club','Diamond')
#cardMarks = ('S','H','D','C')
cardMarks = ('♠', '♥', '♦','♣')

cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'J', 'Q', 'K', 'A')

# make a deck of playing card
deck = []

# add jokers first
'''
for c in cardJokers:
    deck.append(c)
'''

# add 4x13 cards
for cn in cardNumbers:
    for cm in cardMarks:
        card = cm + cn
        deck.append(card)

deck.remove('♠2')
deck.remove('♥2')
deck.remove('♦2')
deck.remove('♣A')

print(len(deck))
print(deck)

# record a new deck to a text file
file_name = "deck-new-54.txt"
f = codecs.open(file_name, "w", "utf-8")
#f = open(file_name, 'w')
for card in deck:
    f.write(card)
    f.write('\n')
f.close()

# start shuffle & deal
print('--- cutting line ----')

num_of_players = 3
cards_of_player = int((len(deck)-3) / num_of_players)
print('We have %d players, every one has %d cards.'
      % (num_of_players, cards_of_player))

player1_deck = []
player2_deck = []
player3_deck = []
remain_deck=[]

for times in range(3):
    picked_card = random.choice(deck)
    remain_deck.append(picked_card)
    deck.remove(picked_card)
print(remain_deck)

for times in range(cards_of_player):
    picked_card = random.choice(deck)
    player1_deck.append(picked_card)
    deck.remove(picked_card)

    picked_card = random.choice(deck)
    player2_deck.append(picked_card)
    deck.remove(picked_card)

    picked_card = random.choice(deck)
    player3_deck.append(picked_card)
    deck.remove(picked_card)

print('\nRemained-cards are :')
print(remain_deck)
print('\nPlayer 1-cards are :')
print(player1_deck)
print('\nPlayer 2-cards are :')
print(player2_deck)
print('\nPlayer 3-cards are :')
print(player3_deck)

landlord_deck = player1_deck + remain_deck
print('\nLandlord''s cards are :')
print(landlord_deck)
