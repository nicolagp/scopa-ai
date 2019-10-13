import random
from card import *
from player import *
from typing import List

class Scopa:
    def __init__(self, p1=Player("p1"), p2=Player("p2"), test=False):
        self.deck = []
        self.score = [0, 0]
        self.round = 0
        self.players = (p1, p2)
        self.table = []
        self.test = test
        # initialize game
        self.start_round()


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
    def start_round(self):
        # do cleanup and update round
        for player in self.players:
            player.cleanup()
            self.round += 1

        # shuffle deck, deal and update table
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
        if self.test:
            random.seed(40)

        # Shuffling
        for i in range(1, 40):
            j = random.randint(0, i)
            temp = self.deck[i]
            self.deck[i] = self.deck[j]
            self.deck[j] = temp

    """ Checks if a move is valid. p is the player's card and t is a list of cards to be taken """
    def valid_move(self, p: Card, t: List[Card]) -> bool:
        if len(t) == 0:
            return True
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
    Obs: to put card on table t_cards should have length 0
    Returns true if successful, false if not. """
    def move(self, player: Player, p_card: int, t_cards: List[int]) -> bool:
        table_cards = [self.table[i] for i in t_cards]
        if len(t_cards) == 0:
            self.table.append(player.hand[p_card])
            player.hand.pop(p_card)
            return True
        # check that the move is valid
        elif self.valid_move(player.hand[p_card], table_cards):
            # check settebello
            settebello = Card("coins", 7)
            if settebello in table_cards or player.hand[p_card] == settebello:
                player.settebello = True
            # put cards into player's pile
            player.pile.extend(table_cards)
            player.pile.append(player.hand[p_card])
            # remove cards from table and player's hand
            player.hand.pop(p_card)
            for card in table_cards:
                self.table.remove(card)
            # check scopa
            if len(self.table) == 0:
                player.scopas += 1
            return True
        else:
            return False

    """ Scores each player's pile of cards and returns a boolean indicating if the game ended. Also increments round """
    def score_round(self, p1: Player, p2: Player, verbose=True) -> bool:
        # number of cards
        p1_num_cards = len(p1.pile)
        p2_num_cards = len(p2.pile)
        if p1_num_cards > p2_num_cards:
            self.score[0] += 1
        elif p2_num_cards > p1_num_cards:
            self.score[1] += 1
        # number of coins
        p1_num_coins = p1.get_coins()
        p2_num_coins = p2.get_coins()
        if p1_num_coins > p2_num_coins:
            self.score[0] += 1
        elif p2_num_coins > p1_num_coins:
            self.score[1] += 1
        # scopas
        self.score[0] += p1.scopas
        self.score[1] += p2.scopas
        # settebello
        if p1.settebello:
            self.score[0] += 1
        else:
            self.score[1] += 1
        # prima
        suits = ["spades", "clubs", "cups", "coins"]
        p1_prima = sum([p1.get_primas(suit) for suit in suits])
        p2_prima = sum([p2.get_primas(suit) for suit in suits])
        if p1_prima > p2_prima:
            self.score[0] += 1
        elif p2_prima > p1_prima:
            self.score[1] += 1
        # check score to see if game ended
        if (max(self.score) > 10) and (self.score[0] != self.score[1]):
            return True
        else:
            if verbose:
                self.round_summary([p1_num_cards, p2_num_cards],
                                   [p1_num_coins, p2_num_coins],
                                   [p1.settebello, p2.settebello],
                                   [p1_prima, p2_prima],
                                   [p1.scopas, p2.scopas])
            return False

    def __str__(self):
        out = ""
        # print player 1 hand
        out += "{}: ".format(self.players[0].name)
        for card in self.players[0].hand:
            out += str(card) + " "
        out += "\n"

        # print table
        out += "Table: "
        for card in self.table:
            out += str(card) + " "
        out += "\n"

        # print player 1 hand
        out += "{}: ".format(self.players[1].name)
        for card in self.players[1].hand:
            out += str(card) + " "
        out += "\n"

        return out

    """
    Outputs a summary of points for the round
    """
    def round_summary(self, cards: List[int], coins: List[int], settebello: List[bool], prima: List[int], scopas: List[int]):
        print("----------- Round Summary -----------")
        print("({}, {})".format(self.players[0], self.players[1]))
        print("Cards: {}, {}".format(cards[0], cards[1]))
        print("Coins: {}, {}".format(coins[0], coins[1]))
        print("Settebello: {}, {}".format(settebello[0], settebello[1]))
        print("Prima: {}, {}".format(prima[0], prima[1]))
        print("Scopas: {}, {}".format(scopas[0], scopas[1]))
        print("Score: {}, {}".format(self.score[0], self.score[1]))
        print("-------------------------------------")
