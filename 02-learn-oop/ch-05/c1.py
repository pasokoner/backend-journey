import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # don't touch below this line

    def __eq__(self, other):
        return RANKS.index(self.rank) == RANKS.index(other.rank) and SUITS.index(
            self.suit
        ) == SUITS.index(other.suit)

    def __gt__(self, other):
        if RANKS.index(self.rank) > RANKS.index(other.rank):
            return True
        elif RANKS.index(self.rank) == RANKS.index(other.rank):
            return SUITS.index(self.suit) > SUITS.index(other.suit)

        return False

    def __lt__(self, other):
        if RANKS.index(self.rank) < RANKS.index(other.rank):
            return True
        elif RANKS.index(self.rank) == RANKS.index(other.rank):
            return SUITS.index(self.suit) < SUITS.index(other.suit)

        return False

    def __str__(self):
        return f"{self.rank} of {self.suit}"


def test(card1, card2):
    print(f"{card1} = {card2}: {card1 == card2}")
    print(f"{card1} > {card2}: {card1 > card2}")
    print(f"{card1} < {card2}: {card1 < card2}")
    print("------------------------------------------")


def main():
    test(Card("Ace", "Hearts"), Card("Queen", "Diamonds"))
    test(Card("2", "Spades"), Card("2", "Diamonds"))
    test(Card("King", "Hearts"), Card("Queen", "Diamonds"))
    test(Card("3", "Clubs"), Card("7", "Clubs"))


main()
