import unittest
from scopa import *

class CardTest(unittest.TestCase):
    def test_can_create_card(self):
        card = Card('clubs', 4)
        self.assertEqual(card.rank, 'clubs')
        self.assertEqual(card.value, 4)

    def test_equals(self):
        card1 = Card('clubs', 4)
        card2 = Card('clubs', 5)
        card3 = Card('clubs', 4)
        card4 = Card('coins', 4)
        self.assertEqual(card1, card3)
        self.assertNotEqual(card1, card2)
        self.assertNotEqual(card1, card4)

class PlayerTest(unittest.TestCase):
    def test_can_create_player(self):
        player = Player('p1')
        self.assertEqual(player.name, 'p1')

class ScopaTest(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Player("p1")
        self.p2 = Player("p2")
        self.scopa = Scopa(self.p1, self.p2)

    def test_start(self):
        # make sure all cards are in the game
        allCards = set(self.scopa.deck).union(set(self.scopa.players[0].hand), set(self.scopa.players[1].hand), self.scopa.table)
        self.assertEqual(len(allCards), 40)

    def test_move(self):
        pass

    def test_score(self):
        pass