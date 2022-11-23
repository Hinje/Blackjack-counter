from main import load_strategy_table, Card, CardSet


def test_load_strategy_table():
    hand_data = load_strategy_table()
    assert hand_data[0] == ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']


def test_add_card():
    my_card_set = CardSet()
    my_card_set.add_card(Card('A', "♦"))
    my_card_set.add_card(Card('4', "♠"))
    assert my_card_set.cards[1].suit == "♠"
    assert my_card_set.cards[1].name == "4"


def test_calc_value():
    my_card_set = CardSet()
    my_card_set.add_card(Card('A', "♦"))
    my_card_set.add_card(Card('4', "♠"))
    assert my_card_set.calc_value() == 15
