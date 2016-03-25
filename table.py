class Table(object):
    def __init__(self, name):
        self.name = name
        self.players = []

    def getName(self):
        return self.name

    def getPlayers(self):
        return self.players

    def setDealer(self, dealer):
        self.dealer = dealer
        dealer.join(self)

    def addPlayer(self, player):
        self.players.append(player)
        player.join(self)
