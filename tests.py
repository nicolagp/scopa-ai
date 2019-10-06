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

    """
    Game configuration with seed 40:
    Player 1: (clubs, 5) (spades, 9) (cups, 7) 
    Table: (coins, 2) (clubs, 3) (cups, 5) (coins, 8) 
    Player 2: (clubs, 10) (coins, 4) (cups, 1) 
    """
    def test_move1(self):
        self.assertEqual(self.scopa.move(self.scopa.players[0], 0, [2]), True)
        self.assertEqual(len(self.scopa.players[0].hand), 2)
        self.assertEqual(len(self.scopa.players[0].pile), 2)
        self.assertEqual(len(self.scopa.table), 3)

    def test_move2(self):
        self.assertEqual(self.scopa.move(self.scopa.players[1], 0, [0, 3]), True)
        self.assertEqual(len(self.scopa.players[1].hand), 2)
        self.assertEqual(len(self.scopa.players[1].pile), 3)
        self.assertEqual(len(self.scopa.table), 2)

    def test_move3(self):
        self.assertEqual(self.scopa.move(self.scopa.players[1], 0, [0, 2, 3]), False)
        self.assertEqual(len(self.scopa.players[1].hand), 3)
        self.assertEqual(len(self.scopa.players[1].pile), 0)
        self.assertEqual(len(self.scopa.table), 4)

    def test_score(self):
        pass