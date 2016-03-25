from person import *
from deck import *

def main():
    dealer = Dealer('Dylan')

    player1 = Player('Vlad')
    player2 = Player('Ing')
    player3 = Player('Ches')
    player4 = Player('Bot')

    table = Table('Kitchen Table')
    table.setDealer(dealer)
    assert(dealer.table == table)

    for player in [player1, player2, player3, player4]:
        table.addPlayer(player)
        assert(player.table == table)

    dealer.setupCards()
    assert(len(dealer.deck.cards) == 54)
    assert(all(isinstance(card, Ground) for card in dealer.deck.cards[:5]))

    while dealer.remainingCards() > 0:
        dealer.dealCard()

if __name__ == '__main__':
    main()
