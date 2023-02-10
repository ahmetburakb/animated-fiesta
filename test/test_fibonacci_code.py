from ..code.fibonacci_code import fib

def test_1():
    assert fib(2) == 1

def test_2():
    assert fib(5) == 5

def test_3():
    assert fib(12) == 144
    