import random
from card import *

class Deck(object):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        '''
        Remove and return the top card from the deck.
        '''
        return self.cards.pop()

    def addCard(self, card):
        self.cards.append(card)

    def countCards(self):
        return len(self.cards)

class FallingDeck(Deck):
    def __init__(self, name):
        Deck.__init__(self, name)

        for i in range(12):
            self.cards.append(Skip())
            self.cards.append(Hit())

        for i in range(5):
            self.cards.append(Split())
            self.cards.append(Extra())
            self.cards.append(Grab())
            self.cards.append(Ground())

        for i in range(4):
            self.cards.append(Push())

        for i in range(6):
            self.cards.append(Stop())

    def shuffle(self):
        '''
        Separate the Ground cards from the deck.
        Shuffle the rest of the cards, and put the Grounds at the bottom.
        '''
        Deck.shuffle(self)
        self.cards = sorted(self.cards, key=lambda card: isinstance(card, Ground), reverse=True)
