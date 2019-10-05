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

    def test_can_init_deck(self):
        self.scopa.init_deck()
        self.assertEqual(len(self.scopa.deck), 40)
        self.assertEqual(len(self.scopa.deck), len(set(self.scopa.deck)))

    def test_shuffle(self):
        self.scopa.init_deck()
        self.scopa.shuffle()
        scopa2 = Scopa(Player("a"), Player("b"))
        scopa2.init_deck()
        self.assertNotEqual(self.scopa.deck, scopa2.deck)
        self.assertEqual(set(self.scopa.deck), set(scopa2.deck))

    def test_deal(self):
        scopa2 = Scopa(Player("a"), Player("b"))
        scopa2.init_deck()
        self.scopa.init_deck()
        self.scopa.shuffle()
        self.scopa.deal()
        # Check that hands have three cards
        self.assertEqual(len(self.scopa.players[0].hand), 3)
        self.assertEqual(len(self.scopa.players[1].hand), 3)
        # Check that all cards are in the game
        self.assertEqual(set(self.scopa.deck).union(set(self.scopa.players[1].hand), set(self.scopa.players[0].hand)),
                         set(scopa2.deck))

    def test_start(self):
        self.scopa.start()
        scopa2 = Scopa(Player("a"), Player("b"))
        scopa2.init_deck()
        self.assertEqual(set(self.scopa.deck).union(set(self.scopa.players[0].hand), set(self.scopa.players[1].hand), set(self.scopa.table)),
                         set(scopa2.deck))
        self.assertEqual(len(self.scopa.deck) + len(self.scopa.players[0].hand) + len(self.scopa.players[1].hand) + len(self.scopa.table), 40)


    def test_move(self):
        pass

    def test_score(self):
        pass