from utils import is_even

def test_is_even_true():
    assert is_even(4) == True

def test_is_even_false():
    assert is_even(5) == False

def test_is_even_negative():
    assert is_even(-2) == True