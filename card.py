class Card:
    def __init__(self, rank, value):
        self.rank = rank
        self.value = value

    def __eq__(self, other):
        return True if (self.rank == other.rank) and (self.value == other.value) else False

    def __hash__(self):
        return hash((self.rank, self.value))

    def __str__(self):
        return "(" + self.rank + ", " + str(self.value) + ")"

    """
    Returns the value of the card according to the prima scoring scale: 
    Seven (sette) = 21 points
    Six (sei) = 18 points
    Ace (asso) = 16 points
    Five (cinque) = 15 points
    Four (quattro) = 14 points
    Three (tre) = 13 points
    Two (due) = 12 points
    Face cards = 10 points
    """
    def prima(self):
        prima = {
            7: 21,
            6: 18,
            1: 16,
            5: 15,
            4: 14,
            3: 13,
            2: 12,
            8: 10, 9: 10, 10: 10,
        }
        return prima.get(self.value)