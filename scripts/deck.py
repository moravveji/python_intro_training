# -*- coding: utf-8 -*-

import random


def generate_deck():
    """Return a list containing the cards in a standard, 52-card deck."""
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King", "Ace"]
    deck = []
    for s in suits:
        for r in ranks:
            name = "%s of %s" % (r, s)
            deck.append(name)
    return deck


def draw_random(deck):
    """Draw a random card from the given deck."""
    n = len(deck)
    i = random.randint(0, n)
    k = draw_card(deck, i)
    return k


def draw_card(deck, x):
    """Return card no. x from the deck."""
    return deck[x]


def test_with_replacement():
    print("Generating deck")
    deck = generate_deck()

    number = 10
    print("Drawing", number, "random cards with replacement:")
    drawn = set()
    for x in range(number):
        card = draw_random(deck)
        print("  You drew", card)
        drawn.add(card)
    unique = len(drawn)
    print("Drew", unique, "different cards")


test_with_replacement()