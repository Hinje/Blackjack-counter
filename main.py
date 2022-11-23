#coding 😎


import csv


class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value
 
    def showcard(self):
        ...
        
        



class Deck_of_Cards:
    def __init__(self):
        self.card_list = []
        self.remake()
 
    def create_deck(self):
        self.cards_list.clear()
        names = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        suits = ["♣", "♠", "♦", "♥"]
           
    #    for i in range(len(names)):
           # for suit in suits:
           #     self.card_list.append
                
                
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


