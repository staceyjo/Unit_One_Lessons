# Create a function named sum_list 
# that takes a parameter list (a list of integers). 

# Iterate through the list and sum up each integer. 

# Then return the total.

def sum_list(list):
    # Note: the word "list" may be highlighted because the Learn platform believes it's reserved
    # This should not affect our code
    sum = 0
    for num in list:
        sum = sum + num
    # print(sum)
    return sum

sum_list([1, 2, 3, 4, 5])
sum_list([3,5,7,9])

# Learn example of a working implementation:

def sum_list(list):
    sum = 0
    for item in list:
        sum += item
    return sum