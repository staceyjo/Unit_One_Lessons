# Create a function named sum_series 
# that takes one parameter max_value (an integer). 
# Starting with 1, 
# add each number in the range from 1 to max_value together. 
# Then return that total.

# Required: Use a for-loop and range().

def sum_series(max_value):
    sum = 0
    for num in range(1, max_value+1):
        sum = sum + num
    # print(sum)
    return sum

sum_series(3)
sum_series(5)
sum_series(10)

# Here is the test:

# def test_sum_series():
#     assert sum_series(3) == 6 # 1 + 2 + 3
#     assert sum_series(5) == 15 # 1 + 2 + 3 + 4 + 5
#     assert sum_series(10) == 55 # 1 + 2 + ... + 9 + 10

# Learn example of a working implementation:

def sum_series(max_value):
    sum = 0
    for i in range(max_value + 1):
        sum += i
    return sum