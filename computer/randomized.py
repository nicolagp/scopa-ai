from typing import List
from card import Card
from computer.computer import Computer
import random

class Randomized(Computer):
    """
    Analyzes hand and randomly tries moves, if no move is found puts random card on the table
    Out: card_on_hand: Card, cards_on_table: List[Card]
    """
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        hand = random.sample(list(self.hand), len(self.hand))
        table_combs = self.get_combinations()
        for card in hand:
            for comb in table_combs:
                if self.valid_move(card, list(comb)):
                    return hand.index(card), [self.table.index(i) for i in comb]

        return random.randint(0, len(hand)-1), [0]