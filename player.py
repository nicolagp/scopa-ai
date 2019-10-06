from typing import List
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.pile = []
        self.scopas = 0
        self.settebello = False

    def get_primas(self, suit: str) -> List[int]:
        cards = []
        for card in self.pile:
            if card.rank == suit:
                cards.append(card.prima())
        if len(cards) == 0:
            return [0]
        else:
            return cards

    def get_coins(self):
        num_coins = 0
        for card in self.pile:
            if card.rank == "coins":
                num_coins += 1
        return num_coins

    def cleanup(self):
        self.hand = []
        self.pile = []
        self.scopas = []
        self.settebello = False