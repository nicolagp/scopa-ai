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
        p1 = Player("p1")
        p2 = Player("p2")
        self.scopa = Scopa(p1, p2)

    def test_can_init_deck(self):
        self.scopa.init_deck()
        self.assertEqual(len(self.scopa.deck), 40)
        self.assertEqual(len(self.scopa.deck), len(set(self.scopa.deck)))