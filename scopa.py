import random
from card import *
from player import *
from typing import List

class Scopa:
    def __init__(self, p1: Player, p2: Player):
        self.deck = []
        self.score = (0, 0)
        self.round = 0
        self.players = (p1, p2)
        self.table = []

    """ Deals 3 cards to players from the remaining cards in deck """
    def deal(self):
        if self.round % 2 == 0:
            first = self.players[0]
            second = self.players[1]
        else:
            first = self.players[1]
            second = self.players[0]

        for i in range(0, 6, 2):
            first.hand.append(self.deck[i])
            second.hand.append(self.deck[i+1])

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

    """ Checks if a move is valid. p is the player's card and t is a list of cards on the table """
    def valid_move(self, p: Card, t: List[Card]) -> bool:
        # check if values add up
        count = 0
        for i in t:
            count += i.value
        if count != p.value:
            return False
        # check if there isn't a card of same value in table
        if len(t) > 1:
            for i in self.table:
                if i.value == p.value:
                    return False

        return True

    """ Updates game state with move, p is the index of the card int the player's hand and
    t is a list with the indices of the cards in the table to be taken """
    def move(self, player: Player, p: int, t: List[int]):
        pass

    """ Scores each player's pile of cards and returns score for round, also increments round """

    def score(self, p1: Player, p2: Player) -> (int, int):
        pass
