# Let's implement a function called sidewinder.

# This function is responsible for
# finding the index in a list that has the value 0 
# by following the imaginary "sidewinder algorithm."

# In order to find the correct index, the function:

# Takes a parameter number_list 
# which is a list of "next" indices to visit

# The function always starts at index 0

# The function will look in the current position,
# get the value stored there. 

# Then, it will use that value as the next 
# position to visit

# The function continues doing this until 
# we find a value of 0, 
# which means we have found the end of the index 
# chain. 

# Then we'll return the position (index) where we found the 0.

# For example, if we received [2, 0, 1] as our number_list, 
# starting from position 0 we find a 2. 

# We look in position 2 and find a 1. 

# So we look in position 1 and find 0. 

# 0 marks the end of the chain, 
# so we return 1, 
# the position we just looked in.

def sidewinder(number_list):
    # find index in list with the value 0
    # number_list is a list of next indices to visit
    # start at index 0 --> number_list[0]
    # get the value stored there, which will be next position
    next_index = number_list[0]
    

    