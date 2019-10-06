import random
from itertools import combinations
from card import *
from player import *
from typing import List

class Scopa:
    def __init__(self, p1=Player("p1"), p2=Player("p2")):
        self.deck = []
        self.score = (0, 0)
        self.round = 0
        self.players = (p1, p2)
        self.table = []
        # initialize game
        self.start()


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
        while True:
            self.init_deck()
            self.shuffle()
            self.deal()
            numKings = 0

            for i in self.deck[:4]:
                if i.value == 10:
                    numKings += 1
                self.table.append(i)

            # need to check that there aren't three or four kings in starting table
            if numKings < 3:
                break
            # undo deal
            else:
                for i in range(3):
                    self.deck.append(self.players[0].hand[i])
                    self.deck.append(self.players[1].hand[i])
                self.players[0].hand = []
                self.players[1].hand = []

        self.deck = self.deck[4:]

    """ Initializes deck with all cards """
    def init_deck(self) -> None:
        self.deck = []
        # Initializing
        ranks = ["spades", "clubs", "cups", "coins"]
        for i in ranks:
            for j in range(1, 11):
                self.deck.append(Card(i, j))

    """ Shuffles deck using the Fisher-Yates algorithm """
    def shuffle(self):
        # Seed for testing purposes
        random.seed(40)

        # Shuffling
        for i in range(1, 40):
            j = random.randint(0, i)
            temp = self.deck[i]
            self.deck[i] = self.deck[j]
            self.deck[j] = temp

    """ Checks if a move is valid. p is the player's card and t is a list of cards to be taken """
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

    """ Updates game state with move, p is the player's card index and
    t is a list with the indices in the table to be taken 
    Returns true if successful, false if not. """
    def move(self, player: Player, p_card: int, t_cards: List[int]) -> bool:
        table_cards = [self.table[i] for i in t_cards]
        # check that the move is valid
        if self.valid_move(player.hand[p_card], table_cards):
            # put cards into player's pile
            player.pile.extend(table_cards)
            player.pile.append(player.hand[p_card])
            # remove cards from table and player's hand
            player.hand.pop(p_card)
            for card in table_cards:
                self.table.remove(card)
            return True
        else:
            return False

    """ Scores each player's pile of cards and returns score """
    def score(self, p: Player) -> int:
        pass

    """ print game """
    def print(self):
        # print player 1 hand
        print("Player 1: ", end="")
        for card in self.players[0].hand:
            print(card, end=" ")
        print("")

        # print table
        print("Table: ", end="")
        for card in self.table:
            print(card, end=" ")
        print("")

        # print player 1 hand
        print("Player 2: ", end="")
        for card in self.players[1].hand:
            print(card, end=" ")
        print("")