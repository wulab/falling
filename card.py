class Card(object):
    def __str__(self):
        return self.__class__.__name__ + ' card'

class Skip(Card):
    pass

class Hit(Card):
    pass

class Split(Card):
    pass

class Extra(Card):
    pass

class Push(Card):
    pass

class Grab(Card):
    pass

class Stop(Card):
    pass

class Ground(Card):
    pass
