class Card:
    def __init__(self, rank, value):
        self.rank = rank
        self.value = value

    def __eq__(self, other):
        return True if self.rank == other.rank and self.value == other.value else False

    def __hash__(self):
        return hash((self.rank, self.value))