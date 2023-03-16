# Write a function to make the test pass. 

# Use the information from the test 
# to help determine what needs to be in the function body, 

# trying to write as minimal an implementation as possible,
# even if it's not the most robust implementation.

# def test_returns_true_if_odd():
#     number = 5
#     result = is_odd(number)
#     assert result

# def is_odd(number):
#     # takes in a number
    
#     #  define an odd number
#     if number %2 != 0:
#         result = True
#         # print(result)
#         return result
#     else:
#         result = False
#         # print(result)
#         return result

# Learn example of a working implementation:

# modified
# def is_odd(num):
#     result = True
#     print(result)
#     return result 

# original: 
def is_odd(num):
    return True
    
is_odd(5)
is_odd(6)
