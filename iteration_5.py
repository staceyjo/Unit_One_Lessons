# Create a function named listify_series 
# that takes one parameter max_value (an integer). 
# Append each number in the range from 1 to max_value to a list. 
# Then return that list.

# Required: Use a for-loop and range().

def listify_series(max_value):
    list = []
    
    for item in range(1, max_value+1):
        list.append(item)
    # print(list)
    return list

listify_series(3)
listify_series(5)
listify_series(10)

# Here is the test:
# def test_listify_series():
#     assert listify_series(3) == [1, 2, 3]
#     assert listify_series(5) == [1, 2, 3, 4, 5]
#     assert listify_series(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
# Learn example of a working implementation:

def listify_series(max_value):
    my_very_good_list = []
    for i in range(max_value):
        my_very_good_list.append(i + 1)
    return my_very_good_list