# Write a function to make the test pass. 

# TEST
def test_returns_true_if_odd():
    number = 5
    result = is_odd(number)
    assert result


def test_returns_false_if_even():
    number = 6
    result = is_odd(number)
    assert not result

# Use the information from the test to help determine 
# what needs to be in the function body.

def is_odd(number):
    # takes in a number
    
    #  define an odd number
    if number %2 != 0:
        return True
    else:
        return False
    
#  Learn solution 
def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True