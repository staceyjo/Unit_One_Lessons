# Create a function named sum_series that takes two parameters: 
# min_value and max_value. 

# Starting with min_value, 
# add each number in the range from min_value to max_value together. 
# Then return that total.

# Required: Use a for-loop and range().

# Assume that min_value and max_value are positive integers, 
# where min_value is less than max_value

def sum_series(min_value, max_value):
    sum = 0
    
    for num in range(min_value, max_value + 1):
        sum = sum + num
    # print(sum)
    return sum

sum_series(1, 3) # 6  # 1 + 2 + 3
sum_series(2, 4) # 9  # 2 + 3 + 4
sum_series(0, 5) # 15  # 1 + 2 + 3 + 4 + 5
sum_series(3, 7) # 25  # 3 + 4 + 5 + 6 + 7

# Here is the test:
# def test_sum_series_with_min_max_vals():
#     assert sum_series(1, 3) == 6  # 1 + 2 + 3
#     assert sum_series(2, 4) == 9  # 2 + 3 + 4
#     assert sum_series(0, 5) == 15  # 1 + 2 + 3 + 4 + 5
#     assert sum_series(3, 7) == 25  # 3 + 4 + 5 + 6 + 7

# Learn example of a working implementation:
def sum_series(min_value, max_value):
    sum = 0
    for i in range(min_value, max_value + 1):
        sum += i
    return sum