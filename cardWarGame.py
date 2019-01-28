# importing the libraries for card selection and allocation
from random import shuffle

# Variables for creating cards:
suite = "H D S C".split()
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()
# mycards = [(s,r) for s in suite for r in ranks]

# Class denoting the deck of cards
class Deck:
    """
    This is the deck class. Initialises the play. This is used to split
    the cards in half and given to the players. Uses Suite and Ranks to
    create a deck. Contains a method to split the deck in half and
    shuffling the deck.
    """
    def __init__(self):
        print("Creating newp ordered deck.")
        self.allcards = [(s,r) for s in suite for r in ranks]

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)

    def split_in_half(self):
        return(self.allcards[:26],self.allcards[26:])

# class denoting player hands
class Hand:
    """
    Each player has a hand, and we can remove cards from that hand or
    put the cards in that hand
    """
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

# Class denoting a player:
class Player:
    """
    This is the player class, which takes the name of the player and an
    instance of Hand class object.
    """
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Return true if the player still has cards left
        """
        return len(self.hand.cards) != 0


print("Welcome to the WAR OF CARDS: ")

# Create a new deck and split in half
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

# Create both players
comp = Player("computer", Hand(half1))

name = input("What is your name? ")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round")
    print("here are the current standings: ")
    print(user.name + "has count of: " + str(len(user.hand.cards)))
    print(comp.name + "has count of: " + str(len(comp.hand.cards)))
    print("play a card!")
    print('\n')

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()
    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:                    # Comparing index 1 because we need to compare ranking [(s,r) for s in ...]
        war_count += 1
        print("war!")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("Game over, number of rounds: " + str(total_rounds))
print("A war happened " + str(war_count) + " times")
