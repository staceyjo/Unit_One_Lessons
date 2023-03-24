import random

# LETTER_POOL  = [ 
#                 "A", "A", "A","A", "A", "A", "A", "A", "A", 
#                 "B", "B", 
#                 "C", "C", 
#                 "D", "D", "D", "D", 
#                 "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
#                 "F", "F", 
#                 "G", "G", "G", 
#                 "H", "H", 
#                 "I", "I", "I", "I", "I", "I", "I", "I", "I", 
#                 "J", 
#                 "K", 
#                 "L", "L", "L", "L", 
#                 "M", "M", 
#                 "N", "N", "N", "N", "N", "N", 
#                 "O", "O", "O", "O", "O", "O", "O", "O", 
#                 "P", "P", 
#                 "Q", 
#                 "R", "R", "R", "R", "R", "R", 
#                 "S", "S", "S", "S", 
#                 "T", "T", "T", "T", "T", "T", 
#                 "U", "U", "U", "U", 
#                 "V", "V", 
#                 "W", "W", 
#                 "X", 
#                 "Y", "Y", 
#                 "Z"]

# def draw_letters():
#     letters = []

#     random_letter_index = random.randint(0,len(LETTER_POOL)-1)

#     while len(letters) < 10: 
#         print(random_letter_index)
#         letters.append(random_letter_index)
    
#     print(letters)

# draw_letters()



# LETTER_POOL = [
#     'A', 
#     'B', 
#     'C', 
#     'D', 
#     'E', 
#     'F', 
#     'G', 
#     'H', 
#     'I', 
#     'J', 
#     'K', 
#     'L', 
#     'M', 
#     'N', 
#     'O', 
#     'P', 
#     'Q', 
#     'R', 
#     'S', 
#     'T', 
#     'U', 
#     'V', 
#     'W', 
#     'X', 
#     'Y', 
#     'Z'
#     ]

# def draw_letters():
#     hand_of_letters = [] 
#     counter = 0
#     while counter < 10:
#         # random_letter = random.choice(LETTER_POOL)
#         hand_of_letters = random.choices(LETTER_POOL, weights=(9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1), k=10)
#         counter +=1
        
#     print(hand_of_letters)
#     return hand_of_letters
# draw_letters()

LETTER_POOL = {
    'A': 9,
    'B': 2,
    'C': 2,
    'D': 4,
    'E': 12,
    'F': 2,
    'G': 3,
    'H': 2,
    'I': 9,
    'J': 1,
    'K': 1,
    'L': 4,
    'M': 2,
    'N': 6,
    'O': 8,
    'P': 2,
    'Q': 1,
    'R': 6,
    'S': 4,
    'T': 6,
    'U': 4,
    'V': 2,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1
}

# to get only the keys from the dictionary and return the values as a list
# https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
# letter_dict_keys = list(LETTER_POOL.keys())
# print(letter_dict_keys)
# returns every key in the dictionary, which is every letter
# can now use this to replace the LETTER POOL in random.choice(),
# which will then assign weights to each letter

def draw_letters():
    random_letters = []     # 1
    counter = 0             # 2
    letter_dict_keys = list(LETTER_POOL.keys())
    
    while counter < 1:     # 3
        
        # 4
        random_letters = random.choices(
            letter_dict_keys,
            weights=(9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2,
                    6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1),
            k=10
        )
        counter += 1
    
    # freq of random letters
    random_letter_freq_dict = {}
    
    for letter in random_letters:
        # print(letter)
        
        if (letter in random_letter_freq_dict):
            random_letter_freq_dict[letter] += 1
            # print(random_letter_dict)
        else:
            random_letter_freq_dict[letter] = 1
            
            # letter value in random_letter_dict <= letter value of same letter in LETTER POOL
            # for letter in LETTER_POOL[letter] and random_letter_freq_dict[letter]:
            #     updated_letter_pool = LETTER_POOL[letter] - random_letter_freq_dict[letter]
            #     print(updated_letter_pool)
                
            
            
    # if random_letter_freq_dict[letter] <= LETTER_POOL[key]    
    
    print(random_letter_freq_dict)
    print(random_letters)
    return random_letters


draw_letters()