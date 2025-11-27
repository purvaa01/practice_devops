from fibonacci import fibonacci

def test_fib_zero():
    assert fibonacci(0) == 0

def test_fib_one():
    assert fibonacci(1) == 1

def test_fib_num():
    assert fibonacci(7) == 13