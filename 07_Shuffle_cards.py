import easygui
import random

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
deck = []
draw = []

while true:
    deck = [random.choice(cards), random.choice(suits)]
    deck.append([cards, suits])
    random.shuffle(deck)
    for item in draw:
        show_cards = f"\n* ".join(draw)
    easygui.


