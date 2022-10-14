#coding 😎


import csv


def black_jack():
    ...


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


