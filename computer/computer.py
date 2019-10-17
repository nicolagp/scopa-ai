from typing import List
from card import Card
from player import Player
from itertools import chain, combinations

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.table = []
        self.seen_cards = []

    def valid_move(self, p: Card, t: List[Card]) -> bool:
        # check if values add up
        count = 0
        for card in t:
            count += card.value
        if count != p.value:
            return False
        # check if there isn't a card of same value in table
        if len(t) > 1:
            for i in self.table:
                if i.value == p.value:
                    return False
        return True

    def set_table(self, table: List[Card]):
        self.table = table

    def append_seen(self, cards: List[Card]):
        self.seen_cards += cards

    def get_combinations(self):
        s = list(self.table)
        return list(chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1)))