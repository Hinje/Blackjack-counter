from main import load_strategy_table


def test_load_strategy_table():
    hand_data = load_strategy_table()
    assert hand_data[0] == ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
