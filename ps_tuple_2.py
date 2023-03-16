# Carmelo is always looking for new, interesting properties of their sequences.

# They've recently been wondering whether the first and last values they stored 
# in each of their sequences has anything interesting about them.

# Assuming Carmelo is currently interested in the following sequences:

fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21]
positive_even_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
triangular_numbers = [1, 3, 6, 10, 15, 21, 28, 36]

# They would like to get the first and last value 
# returned as two values.

# Write a function get_first_and_last 
# that Carmelo can use to retrieve the pair of values 
# from the start and end of the sequence. 



def get_first_and_last(sequence):
    # convert sequence from a list to a tuple
    tuple_seq= tuple(sequence)
    
    # first index , last index
    # print((tuple_seq[0], tuple_seq[-1]))
    return (tuple_seq[0], tuple_seq[-1])
    

# Note that they would like to be able to use the function as follows:
first, last = get_first_and_last(fibonacci_sequence)
# print(f"first: {first}, last {last}")

# output returns a tuple of first index position and last index position [0] [-1]

# get_first_and_last(fibonacci_sequence)  # (1, 21)
# get_first_and_last(positive_even_numbers)   # (2, 16)
# get_first_and_last(prime_numbers)   #((2, 19)
# get_first_and_last(triangular_numbers) # (1, 36)

# Learn solution: example of a working implementation:

def get_first_and_last(sequence):
    # we expect sequence to be a non-empty list (Carmelo always stores 8 values)
    
    # return the first (position 0) and last (position -1) values from the sequence
    # Python treats bare comma-separated values as a tuple!
    return sequence[0], sequence[-1]


