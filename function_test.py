# ToRun
# pytest .\function_test.py

from function import minimum_coins_required
from function import capitalise_even_letters


def test_capitalise_even_letters():
    assert capitalise_even_letters("test") == "tEsT"    
    assert capitalise_even_letters("test two") == "tEsT tWo"

def test_minimum_coins():
    assert minimum_coins_required(5) == 1
    assert minimum_coins_required(13) == 3
    assert minimum_coins_required(150) == 2
    assert minimum_coins_required(50000) == 250