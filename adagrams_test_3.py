# 1
    # function takes in a word as a parameter
    # word, which is a string of characters

# 2
    # score_chart
    # using a dictionary - the key is immutable
    # but-- you can loop through both the keys and the values
    # and return the key, which is an integer in this case.


# 3
    # Each letter within word has a point value.
    # so the variable total_points_scored helps us hold a value
    
# 4
    # Loop through each of the letters in the word that's provided as an argument
    # for each word, if the user enters a word that's lowercase,
    # using .upper() will capitalize it so it matches the 
    # elements that are contained in the list, as the values in the dictionary

# 5
    # In order to loop through the dictionary's values-- which are a list
    # there's a syntax to follow to get both elements: 
    # Loop through both keys and values, by using the items() method:
    # for x, y in thisdict.items():
    #   print(x, y)
    
# 6
    # each time you iterate through the list of dictionary's values
    # if that letter is in the dictionary's value, 
    
# 7
    # then you add the dictionary's key- which is an integer
    # to the total points scored
    # each dicionary key is an integer- which is the pointvalue, 
    # associated with each letter

# 8 
    # if the length of the word is 7, 8, 9, or 10
    # then add 10 additional points
    

# 9
    # the function returns an integer,
    # representing the number of the total points scored


def score_word(word):                                           # 1
    
    score_chart = {                                             # 2
    1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"], 
    5: ["K"], 
    8: ["J", "X"], 
    10: ["Q" "Z"]   
}
    
    total_points_scored = 0                                     # 3
    

    for letter in word.upper():                                 # 4
        for dict_key, dict_value in score_chart.items():        # 5
            if letter in dict_value:                            # 6
                # print(letter)
                # print(dict_value)
                total_points_scored += dict_key                 # 7
        
    if len(word) > 6:                                           # 8 
        total_points_scored += 8
        
    print(total_points_scored)
    return total_points_scored
    


#  Tests
print("========= Test 1: test_score_word_accurate =========")
# def test_score_word_accurate():
    # Assert
score_word("A") #== 1
score_word("DOG") #== 5
score_word("WHIMSY") #== 17


print("========= Test 2: test_score_word_accurate_ignores_case =========")

# # def test_score_word_accurate_ignores_case():
#     # Assert
score_word("a") #== 1
score_word("dog") #== 5
score_word("wHiMsY") #== 17


print("========= Test 3: test_score_zero_for_empty =========")

# # def test_score_zero_for_empty():
#     # Assert
score_word("") #== 0


print("========= Test 4: test_score_extra_points_for_seven_or_longer =========")

# # def test_score_extra_points_for_seven_or_longer():
#     # Assert
score_word("XXXXXXX") #== 64
score_word("XXXXXXXX") #== 72
score_word("XXXXXXXXX") #== 80