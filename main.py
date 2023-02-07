import random
import csv


class Card:
    values = {"A": 11, "K": 10, "Q": 10, "J": 10, "T": 10, "9": 9,
              "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.ace_low = False

    @property
    def value(self, ace_low=False):
        value = self.values[self.name]
        if self.name == "A" and self.ace_low:
            value = 1
        return value

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

    @property
    def length(self):
        return len(self.cards)

    @property
    def value(self):
        total = sum(cd.value for cd in self.cards)
        # Switch aces to have value 1 if necessary to get total value below 21
        while total > 21 and any((card := cd) for cd in self.cards if cd.name == 'A' and not cd.ace_low):
            card.ace_low = True
            total = sum(cd.value for cd in self.cards)
        return total


class BlackJackDeck(CardSet):

    def __init__(self):
        super().__init__()
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        self.cards = [Card(nm, st)
                      for nm in self.names
                      for st in self.suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def take_top(self):
        return self.cards.pop()

    def deal_cards(self, num_players):
        # to-do - dealer_hand is an instance of DealerHand other hands are instances of Hand (or PlayerHand)

        hands = [Hand() for _ in range(num_players)]
        for _ in range(2):
            for hand in hands:
                hand.cards.append(self.take_top())
        return hands


class Hand(CardSet):

    def __init__(self):
        super().__init__()
        self.stood = False

    def hit(self, deck):
        self.add_card(deck.take_top())

    def stand(self):
        self.stood = True

    @property
    def bust(self):
        return self.value > 21


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
        return my_data


class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = BlackJackDeck()
        self.dealer_hand, *self.player_hands = self.deck.deal_cards(self.num_players)
        self.current_player_number = 0
        # self.current_player_hand = self.player_hands[0]

    def next_player(self):
        self.current_player_number = self.current_player_number + 1

    def player_action(self, decision):
        current_player_hand = self.player_hands[self.current_player_number]
        if decision == "hit":
            current_player_hand.hit(self.deck)
        elif decision == "stand":
            current_player_hand.stand()

        if current_player_hand.bust or current_player_hand.stood:
            self.next_player()

        if self.current_player_number == self.num_players:
            self.dealer_turn()

    def dealer_turn(self):
        ...


if __name__ == "__main__":
    # my_cards = CardSet()
    # my_cards.add_card(Card('A', "♠"))
    # my_cards.add_card(Card('8', "♥"))
    # my_cards.add_card(Card('9', "♥"))
    # my_cards.add_card(Card('T', "♥"))

    # my_deck = BlackJackDeck()
    # dealer_hand, *player_hands = my_deck.deal_cards(3)
    my_game = Game(4)
# wiki check for when betting happens, how player rotation works.
