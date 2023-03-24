import collections
from collections import Counter

def uses_available_letters(word, letter_bank):

    
    # loop through each letter in the word that the user provides
    # if the letter from that word is in the letter bank, return True
    # otherwise, return False
    for letter in word:
        
        # capitalize all letters
        word = word.upper()
        
        letter_bank_counter = Counter(letter_bank)
        print(f"================> Looping through letter: {letter}")
        print(f"ORIGINAL LETTER BANK {letter_bank_counter}")
        
        word_counter = Counter(word)
        print(f"====> WORD VALUES FOR {word} :")
        print(f"{word_counter=}")
        # ensure that letters in word are available in correct quantities in hand
        # if a user tries to enter a word that contains more of that letter
        # than the letter bank has
        
        if letter in letter_bank_counter:
        # subtracting values from counters
            letter_bank_counter.subtract(word_counter)
            print(f"LETTER BANK AFTER SUBTRACTION {letter_bank_counter}")
                        
            if letter_bank_counter[letter] < 0:
                # print(f" Only print if remaining is less than 0: {letter_bank_counter[letter]}")
                print(False) 
                return False
        
        # check if letter (from the word) is NOT in letter_bank/drawn hand
        if letter not in letter_bank:
            print(False)
            return False
        
    print(True)
    return True
        
        
        # if letter not in letter_bank or (word.count(letter) > letter_bank.count(letter)):



# Test 1: entering a word that is an anagram
# returns True
letters = ["D", "O", "G", "X", "X", "X", "X", "X", "X", "X"]
word = "DOG"
print("========= Test 1 =========")
uses_available_letters(word, letters)


# # Test 2: false word- including a letter not in letter bank
# # returns False
letters = ["D", "O", "X", "X", "X", "X", "X", "X", "X", "X"]
word = "DOG"
print("========= Test 2 =========")
uses_available_letters(word, letters)


# # Test 3: don't overuse letter
# # returns False
letters = ["A", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
word = "AAA"
print("========= Test 3 =========")
uses_available_letters(word, letters)


# # Test 4: doesn't change letter bank
# #     True
# #     letters == copy
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
letters_copy = letters[:]
word = "ABCD"
print("========= Test 4 =========")
uses_available_letters(word, letters)

# # Test 5: ignores case BUT doesn't allow user to enter more than whats in dict
