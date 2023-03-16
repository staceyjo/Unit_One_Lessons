# Create a function named sum_even_nums_series 
# that takes two parameters: min_value and max_value. 

# Starting with min_value, 
# add each even number in the range 
# from min_value to max_value together. 
# Then return that total.

# Required: Use a for-loop.

# Assume that min_value and max_value are positive integers, where min_value is less than max_value

def sum_even_nums_series(min_value, max_value):
    sum = 0
    for num in range(min_value, max_value+1):
        if num % 2 ==0: 
            sum = sum + num
    # print(sum)
    return sum

sum_even_nums_series(1, 3)  # 2  # 2
sum_even_nums_series(2, 4)  # 6  # 2 + 4
sum_even_nums_series(0, 5)  # 6  # 0 + 2 + 4
sum_even_nums_series(3, 7)  # 10  # 4 + 6

# Here is the test:
# def test_sum_even_nums_in_series():
#     assert sum_even_nums_series(1, 3) == 2  # 2
#     assert sum_even_nums_series(2, 4) == 6  # 2 + 4
#     assert sum_even_nums_series(0, 5) == 6  # 0 + 2 + 4
#     assert sum_even_nums_series(3, 7) == 10  # 4 + 6

# An example of a working implementation:

def sum_even_nums_series(min_value, max_value):
    sum = 0
    for i in range(min_value, max_value + 1):
        if i % 2 == 0:
            sum += i
    return sum

# Another example of a working implementation:

def sum_even_nums_series(min_value, max_value):
    sum = 0
    if min_value % 2 == 0:
        start_value = min_value
    else:
        start_value = min_value + 1

    for i in range(start_value, max_value + 1, 2):
        sum += i
    return sum