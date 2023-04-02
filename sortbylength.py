
# sort_by_length is a function that takes in one string. 
# It returns a list of strings, 
# where the items are the words from the string, 

# ordered by length. 
# Words with shorter length are placed before words with longer length.

# When words are tied for length, 
# maintain the order they appeared in the original string.

# ================================ First attempt- not working
def sort_by_length(sentence):
    
    # .split() returns a list with each word as a string in the word
    words = sentence.split()
    # print(words)
    
    i = 1

    while i < len(words):
        word_to_insert = words[i]
        insertion_index = i
        # Search in the sorted portion of the words
        # for the correct position to insert words[i]
        while insertion_index > 0 and len(words[insertion_index-1]) > len(word_to_insert):
            words[insertion_index] = words[insertion_index-1]
            insertion_index -= 1
        words[insertion_index] = word_to_insert
        i += 1
    # print(words)
        


sort_by_length("")
# # == []

sort_by_length("I love great awesome words")
# # == [
# #         "I", "love", "great", "words", "awesome"]

sort_by_length("love great awesome words I")
# # == [
# #         "I", "love", "great", "words", "awesome"]

sort_by_length("words of equal length")
# # == [
# #         "of", "words", "equal", "length"]


# ================================ second attempt- not working

# def sort_by_length(sentence):
#     # split the words in the sentence
#     # .split() returns a list with each word as a string in the word
#     words = sentence.split()
#     # print(words)
    
#     i = 1
    
#     # Traverse through 1 to len(arr)
#     for i in range(1, len(words)):
#         key = words[i]
        
#         # Move elements of words[0..i-1], that are
#         # greater than key, to one position ahead
#         # of their current position
#         j = i-1
#         while j >= 0 and key < words[j] :
#                 words[j + 1] = words[j]
#                 j -= 1
#         words[j + 1] = key
    
#     print(words)
    
# sort_by_length("")
# # == []

# sort_by_length("I love great awesome words")
# # == [
# #         "I", "love", "great", "words", "awesome"]

# sort_by_length("love great awesome words I")
# # == [
# #         "I", "love", "great", "words", "awesome"]


# sort_by_length("words of equal length")
# # == [
# #         "of", "words", "equal", "length"]



