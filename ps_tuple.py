# Carmelo has built a set of tuples, 
# where each tuple holds the first eight values in a sequence. 

# They need our help to write a function 
# that can tell them whether a new sequence is one they've already seen. 

# (Take a moment and think about why they used tuples to store 
# their sequences in the set!)

# Assuming Carmelo has the following sequences 
# in their collection of sequences:

carmelo_sequences = {
    (1, 2, 3, 4, 5, 6, 7, 8),
    (2, 4, 6, 8, 10, 12, 14, 16),
    (1, 1, 2, 3, 5, 8, 13, 21),
    (1, 3, 6, 10, 15, 21, 28, 36),
}

# And that we have the following sequences defined:

fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21]
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# Write a function is_known_sequence that Carmelo 
# can use to find out whether they've seen this 
# sequence before.

def is_known_sequence(sequence, known_sequences):
    
    # carmelos known sequences are tuples, 
    # the sequences (fibonacci & prime) are lists
    
    #  want to chek if a sequence is in the known_squences
    
    sequence_tuple = tuple(sequence)
    # print(sequence_tuple)
    
    if sequence_tuple in known_sequences:
        # print(True) 
        return True
    
    else: 
        return False
    
    
    #  From Rountable: 
    # changing to a tuple or a list is the simpliest version
    # sequence_tuple = tuple(sequence)
    
    # if tuple(sequence) in known_sequences:
    #     return True
    # else: 
    #     return False
    
    
    #  Solution from Learn

is_known_sequence(fibonacci_sequence, carmelo_sequences) # True
# is_known_sequence(prime_numbers, carmelo_sequences) # False