# Tests:

def test_returns_true_if_odd():
    number = 5
    result = is_odd(number)
    assert result


def test_returns_false_if_even():
    number = 6
    result = is_odd(number)
    assert not result


def test_returns_none_if_negative():
    number = -1000
    result = is_odd(number)
    assert result is None
    
def is_odd(num):
    if num < 0:
        return None
    elif num % 2 == 0:
        return False
    else:
        return True