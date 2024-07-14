#app.py
#This is a first commit
def subtract(a, b):
    return a - b

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2
