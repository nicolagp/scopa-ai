from typing import List
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.pile = []
        self.scopas = 0
        self.settebello = False

    def __str__(self):
        return self.name

    def get_primas(self, suit: str) -> int:
        cards = []
        for card in self.pile:
            if card.rank == suit:
                cards.append(card.prima())
        if len(cards) == 0:
            return 0
        else:
            return max(cards)

    def get_coins(self):
        num_coins = 0
        for card in self.pile:
            if card.rank == "coins":
                num_coins += 1
        return num_coins

    def cleanup(self):
        self.hand = []
        self.pile = []
        self.scopas = 0
        self.settebello = False

    def move(self):
        pass