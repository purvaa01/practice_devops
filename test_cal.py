from calculator import add,subtract,multiply,div

def test_add():
    assert add(2,3) == 5

def test_sub():
    assert subtract(5,2) == 3

def test_multiply():
    assert multiply(2, 4) == 8

def test_div():
    assert div(10,2) == 5

def test_div_by_zero():
    try:
        div(5, 0)
    except ValueError:
        assert True