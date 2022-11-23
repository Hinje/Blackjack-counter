# coding 😎


import csv


class Card:
    values = {"A": 11, "K": 10, "Q": 10, "J": 10, "T": 10, "9": 9,
             "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.value = self.values[name]

    def showcard(self):
        ...

    def __str__(self):
        return f'{self.suit}{self.name}'


class CardSet:
    names = list("AKQJT98765432")
    suits = ["♣", "♠", "♦", "♥"]

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calc_value(self):
        # TODO must account for Aces
        return sum(card.value for card in self.cards)


class BlackJackDeck(CardSet):

    def __init__(self):
        self.card_list = []
        self.create_deck()

    def create_deck(self):
        self.card_list = [Card(nm, st)
                          for nm in self.names
                          for st in self.suits]

    # for i in range(len(names)):
    # for suit in suits:
    # self.card_list.append


class Bot:
    def __init__(self):
        self.hand = []
        self.chips = 10000

    def print_hand(self):
        number_of_cards = len(self.hand)

    def calculate_hand(self):
        value = 0
        for card in self.hand:
            value += card.value


def load_strategy_table():
    my_file = "Strategy.csv"
    my_data = []
    with open(my_file, newline='') as csvfile:
        my_reader = csv.reader(csvfile, delimiter=",")
        for row in my_reader:
            my_data.append(row)
        return (my_data)


if __name__ == "__main__":
    hand_data = load_strategy_table()
    print(hand_data[0])
