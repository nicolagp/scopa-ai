from typing import List
from card import Card
from computer.computer import Computer
import random

class Randomized(Computer):
    """
    Analyzes hand and randomly tries moves, if no move is found puts random card on the table
    Out: card_on_hand: Card, cards_on_table: List[Card]
    """
    def move(self):
        hand = self.shuffle()
        table_combs = self.get_combinations()
        for card in hand:
            for comb in table_combs:
                if self.valid_move(card, list(comb)):
                    return card, list(comb)

        return hand[random.randint(0, len(hand)-1)], [0]

    def shuffle(self):
        random_hand = list(self.hand)
        for i in range(1, len(random_hand)):
            j = random.randint(0, i)
            temp = random_hand[i]
            random_hand[i] = random_hand[j]
            random_hand[j] = temp
        return random_hand