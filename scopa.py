import random
from card import *
from player import *

class Scopa:
    def __init__(self, p1: Player, p2: Player):
        self.deck = []
        self.score = (0, 0)
        self.round = 0
        self.players = (p1, p2)
        self.table = []

    """ Deals 3 cards to players from the remaining cards in deck """
    def deal(self) -> None:
        if self.round % 2 == 0:
            first = self.players[0]
            second = self.players[1]
        else:
            first = self.players[1]
            second = self.players[0]

        for i in self.deck[:6:2]:
            first.hand += self.deck[i]
            second.hand += self.deck[i+1]
        self.deck = self.deck[6:]

    """ Starts game by initializing deck, dealing cards and putting cards on the table """
    def start(self):
        self.init_deck()
        self.shuffle()
        self.deal()
        for i in self.deck[:4]:
            self.table.append(i)
        self.deck = self.deck[4:]


    """ Initializes deck with all cards """
    def init_deck(self) -> None:
        # Initializing
        ranks = ["spades", "clubs", "cups", "coins"]
        for i in ranks:
            for j in range(1, 11):
                self.deck.append(Card(i, j))

    """ Shuffles deck using the Fisher-Yates algorithm """
    def shuffle(self):
        # Shuffling
        for i in range(1, 40):
            j = random.randint(0, i)
            temp = self.deck[i]
            self.deck[i] = self.deck[j]
            self.deck[j] = temp

    """ Scores each player's pile of cards and returns score for round, also increments round """
    def score(self, p1: Player, p2: Player) -> (int, int):
        pass

