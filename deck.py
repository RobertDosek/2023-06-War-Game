import card
import random


class Deck:
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in card.suits:
            for rank in card.ranks:
                # Create the Card Object, this assumes the Card class has already been defined!
                created_card = card.Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()



