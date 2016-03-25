import config
from deck import *
from table import *

class Person(object):
    def __init__(self, name):
        self.name = name

    def join(self, table):
        self.table = table
        if config.debug:
            print self.name + ' joined ' + table.getName()

class Player(Person):
    def __init__(self, name):
        Person.__init__(self, name)
        self.hand = Deck('Hand')
        self.riders = Deck('Riders')
        self.stacks = [Deck('Stack')]

    def getStacks(self):
        return self.stacks

class Dealer(Person):
    def __init__(self, name):
        Person.__init__(self, name)
        self.currentPass = 0

    def setupCards(self):
        '''
        Before you deal, separate the Ground cards from the deck.
        Shuffle the rest of the cards, and put the Grounds at the bottom.
        Hold the deck face down, and deal from the top.
        The Grounds will be the last cards you deal.
        '''
        self.deck = FallingDeck('The Deck')
        self.deck.shuffle()

    def dealCard(self):
        '''
        Draw a card from the deck and deal it to the next player in line.
        If a player has more than one stack, you deal one card into each.
        If a player has no stacks at all, you start a new one.
        '''
        players = self.table.getPlayers()
        nextPlayer = players[self.currentPass % len(players)]
        nextStacks = nextPlayer.getStacks()

        for stack in nextStacks:
            card = self.deck.drawCard()
            stack.addCard(card)
            if config.debug:
                print self.name + ' dealt ' + str(card) + ' to ' + nextPlayer.name

        self.currentPass += 1

    def remainingCards(self):
        return self.deck.countCards()
