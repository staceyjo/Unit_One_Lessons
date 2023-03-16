# Carmelo has a way to get the first and last elements of 
# any of their sequences. 

# They wonder whether it would be interesting 
# if they found the product of each of those pairs.         [0] * [-1]

# They'd like to store the results in a dictionary          
# so that they can keep track of the products 
# of all of the first and last elements from all of their sequences.


# They start with an empty dictionary for the product table:
product_table = {}

# Then they'll use the get_first_and_last function 
# we wrote for them to get the first and last element 
# of each of their very interesting sequences. 

# Then they'll pass the product_table 
# and the first and last elements into a new function 
# they'd like us to write.

# Write a function store_product_of_pairs 
# that Carmelo can use to build up their product_table 
# using each of the pairs. 

# Consider the following examples. 
# Notice that the call returns the product as the return value, 
# and also stores it in the product_table 
# using the pair of input numbers as the dictionary key.

# The previous examples would be the result of calling something like the following code:

def store_product_of_pairs(product_table, first, last):
    # set a variable to hold the product of each sequence's first and last element
    product_results = first * last
    
    new_key = (first, last)
    
    product_table[new_key] = product_results
    
    return product_results
    
# Learn solution: 
 
# An example of a working implementation:

def store_product_of_pairs(product_table, first, last):
    # product_table is expected to be a dictionary mapping number pairs to numeric products
    # first and last are expected to be numbers

    # calculate the product
    product = first * last

    # store the product in the product_table under the pair made from first and last
    product_table[first, last] = product

    # finally, return the product
    return product

store_product_of_pairs(product_table, 1, 21)
store_product_of_pairs(product_table, 2, 16)
store_product_of_pairs(product_table, 2, 19)
store_product_of_pairs(product_table, 1, 36)