# ========================================== PROBLEM STATEMENT ==========================================

# Problem Statement
# Imagine working on software that deals with restaurant reviews.

# Create a function named get_highest_rated 
# that is responsible for finding the highest-rated restaurant.

restaraunts = []
def get_highest_rated(restaraunts):
    pass

# This function should take in a list of dictionaries named restaurants as a parameter. 

# Each dictionary represents the data associated with a restaurant, including its rating. 

# This function should have a return value of the restaurant with the highest rating.


# ========================================== EXAMPLE INPUT/ OUTPUT ==========================================

# Example 1:

# Input: restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]
# restaurants = [
#     {"name": "Grillby's", "rating": 1}, 
#     {"name": "Crow's Nest", "rating": 5}
# ]

# Output: {"name": "Crow's Nest", "rating": 5}

# Example 2:

# Input: restaurants = [{"name": "Crow's Nest", "rating": 1}]

# Output: {"name": "Crow's Nest", "rating": 1}


# Example 3:
# Input: restaurants = []

# Output: None

# ========================================== CLARIFYING QUESTIONS-- MINE ==========================================

# Step 1- Clarifying questions: 
#  For each question, provide an answer which includes the effect your decision 
#  would have on how you would approach the problem.

# Question 1: What if a rating is higher than the scale? (included in test)
    # ---> set any rating greater than 5 to 5
    # ---> return invalid rating error for ratings greater than 5

# Question 2: What if the restaurant is listed with a name, but no rating? (included in test)
    # LEARN: How should the function handle restaurant dictionaries with missing data (name or rating)?
    # ---> set to 0 or 1, whatever the lowest rating is-- assuming 1 to be the lowest
    # ---> return invalid rating error for ratings greater than 5

# Question 3: What if more than one restaurant in the list both share the same highest rating? (included in test)
    # LEARN: What should the function return if there are multiple restaurants tied for the highest rating?
    # ---> either return both or return the first one listed

# Question 4: What's the scale? is 1 the lowest and 5 the highest? are all restaurant ratings 1 -5 ?
# --> set anything lower than 1 to 1, set anything higher than 5 to 5

# Question 5 :Should anything print to the console? or just return as a dictionary?
    # ---> just return for now, but will likely add a print statement commented out 

# Question 6: What if the rating the user entered was entered as a string instead of an integer ? (included in test)
    # LEARN # How should the function handle non-numerical values for "rating"?
    # ---> could stringify the values 

# Question 7: How does the function handle an invalid argument? (included in test)
    # ---> add an error message 


# ========================================== CLARIFYING QUESTIONS-- LEARN ==========================================

# Example clarifying questions from LEARN:
# How should the function handle restaurant dictionaries with keys in addition to "name" and "rating"?
# - did not think about this

# How should the function handle input that is a single dictionary (not a list)?
# - did not think about this

# What should the function return if there are multiple restaurants tied for the highest rating?
# - did think about this

# How should the function handle restaurant dictionaries with missing data (name or rating)?
# - did think about this

# How should the function handle non-numerical values for "rating"?
# - did think about this



# ========================================== WRITE UNIT TESTS ==========================================

# 1 Use the comments provided to write at least two example input/outputs:
    # Consider at least one nominal and one edge case.
    # What is the expected output for the given input?
    # You can use the examples provided in the prompt, or other examples.

# 2 Write unit tests for get_highest_rated for the nominal and edge cases you identified in the first step.
    # Note: Click the Run Tests button to save your tests for instructor feedback.
    # No real tests are actually run again your unit tests.
    # assert - state that something is true/ a true statement what we expect to be true


# ========================================== WRITE UNIT TESTS :PART 1 - NOMINAL CASE

# tests valid entries returns highest rated dictionary:
    # example input 1: [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]
    # expected output 1: {"name": "Crow's Nest", "rating": 5}

# tests single valid entry returns highest rated dictionary
    # example input 2: [{"name": "Crow's Nest", "rating": 1}]
    # expected output 2: {"name": "Crow's Nest", "rating": 1}


# ========================================== WRITE UNIT TESTS :PART 1 - EDGE CASE

# tests empty list returns None
    # example input 3: restaurants = []
    # example output 3: None
    
# tests rating higher than 5 returns invalid rating msg
    # example input 5: restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 6}]
    # example output 5: "Restaraunt(s) rating above 5. Please adjust rating, between 1 - 5."

# tests rating lower than 1 returns invalid rating msg
    # example input 4: restaurants = [{"name": "Grillby's", "rating": 0}, {"name": "Crow's Nest", "rating": 5}]
    # example output 4: "Restaraunt(s) rating below 1. Please adjust rating, between 1 - 5."

# tests no rating returns invalid rating msg
    # example input 6: restarants = [{"name" : "Gillby's"}, "rating": ]
    # example output 6: "Restaraunt(s) rating left blank. Please adjust rating, between 1 - 5."

# tests shared highest rating returns first listed
    # example input 7: restaurants = [{"name": "Grillby's", "rating": 5}, {"name": "Crow's Nest", "rating": 5}]
    # example output 7: {"name": "Grillby's", "rating": 5}

# tests non-numerical value returns invalid rating msg
    # example input 8: [{"name": "Grillby's", "rating": "5"}]
    # example output 8: "Restaraunt rating scale between 1 - 5. Please enter a single number"



# ========================================== WRITE UNIT TESTS :PART 2 - NOMINAL CASE

def test_valid_entries_returns_highest_rated(restaraunts):
    # arrange
    restaraunts = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]
    expected_result= {"name": "Crow's Nest", "rating": 5}

    # act
    actual_result = get_highest_rated(restaraunts)

    # assert
    assert expected_result == actual_result




def test_single_valid_entry_return_highest_rated(restaraunts):
    # arrange
    restaraunts = [{"name": "Crow's Nest", "rating": 1}]
    expected_result = {"name": "Crow's Nest", "rating": 1}

    # act
    actual_result = get_highest_rated(restaraunts)

    # assert
    assert expected_result == actual_result



# ========================================== WRITE UNIT TESTS :PART 2 - EDGE CASE

def empty_list_returns_none(restaraunts):
    # arrange
    restaraunts = []
    expected_result = None

    # act
    actual_result = get_highest_rated(restaraunts)

    # assert
    assert expected_result == actual_result


def test_rated_higher_than_5_returns_msg(restaraunts):
    # arrange
    restaraunts = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 6}]
    expected_result = "Restaraunt(s) rating above 5. Please adjust rating, between 1 - 5."

    # act
    actual_result = get_highest_rated(restaraunts)

    # assert
    assert expected_result == actual_result


def test_rated_lower_than_1_returns_msg(restaraunts):
    # arrange
    restaraunts =[{"name": "Grillby's", "rating": 0}, {"name": "Crow's Nest", "rating": 5}]
    expected_result = "Restaraunt(s) rating below 1. Please adjust rating, between 1 - 5."

    # act
    actual_result = get_highest_rated(restaraunts)

    # assert
    assert expected_result == actual_result


def test_no_rating_returns_msg(restaraunts):
    # arrange
    restaraunts =[{"name": "Grillby's", "rating": None}]
    expected_result = "Restaraunt(s) rating cannot be none. Please adjust rating, between 1 - 5."

    # act
    actual_result = get_highest_rated(restaraunts)

    # assert
    assert expected_result == actual_result


def test_multiple_highest_rating_returns_first_listed(restaraunts):
    # arrange
    restaraunts = [{"name": "Grillby's", "rating": 5}, {"name": "Crow's Nest", "rating": 5}]
    expected_result = {"name": "Grillby's", "rating": 5}

    # act
    actual_result = get_highest_rated(restaraunts)

    # assert
    assert expected_result == actual_result


    
def test_non_numerical_value_returns_msg(restaraunts):
    # arrange
    restaraunts = [{"name": "Grillby's", "rating": "5"}]
    expected_result = "Restaraunt rating scale between 1 - 5. Please enter a single number"

    # act
    actual_result = get_highest_rated(restaraunts)

    # assert
    assert expected_result == actual_result



# ========================================== LEARN RESULTS- WRITE UNIT TESTS ==========================================
# Example tests:

# example input 1:     
# restaurants = [
#    {"name": "Grillby's", "rating": 1},
#    {"name": "Crow's Nest", "rating": 5}
# ]
# expected output 1: {"name": "Crow's Nest", "rating": 5}

# example input 2: [{"name": "Crow's Nest", "rating": 1}]
# expected output 2: {"name": "Crow's Nest", "rating": 1}

def test_picks_highest_rated_from_list():
    # nominal test case

    # arrange
    restaurants = [
            {"name": "Grillby's", "rating": 1},
            {"name": "Crow's Nest", "rating": 5}
        ]

    # act
    output = get_highest_rated(restaurants)
    
    # assert
    assert output == {"name": "Crow's Nest", "rating": 5}



def test_picks_from_list_of_one():
    # edge test case

    # arrange
    restaurants = [{"name": "Crow's Nest", "rating": 1}]

    # act
    output = get_highest_rated(restaurants)
    
    # assert
    assert output == {"name": "Crow's Nest", "rating": 1}



def test_returns_none_with_zero_restaurants(self):
    # edge test case

    # arrange
    restaurants = []

    # act
    output = get_highest_rated(restaurants)
    
    # assert
    assert output is None
    
    
# ========================================== CREATE LOGICAL STEPS ==========================================

# Without writing code, describe how you would implement get_highest_rating 
# in enough detail that someone else could write the code.

# It may be helpful to break up the problem/algorithm into smaller subproblems/algorithms. For example, 
    # 1. Handle invalid input, 
    # 2. Given valid input, perform the computation/solve the problem/etc.

# Your logical steps could take the form of:
    # a numbered list, 
    # pseudo code, 
    # or anywhere inbetween. 

# What's important at this stage is to think through and outline the implementation before writing code.

# 1. define the function get_highest_rated() 
#    that takes in one parameter, restaurants

# 2. restaraunts will be a list of dictionaries
#    example argument for restaraunts when passed in the function : 
#    restaraunts = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}] 

# 3. set variable for highest_rated_value: --------------------------> didn't need this
#    highest_rated = 5


# 4.  set variable for rating to ensure the value is a number --------> didn't need this
#     if no value is entered int() will return 0
#     rating_int = int()

# 5.  check if list contains only one element
#    if only one element, return that dictionary

# 4. else, we need to loop through the list of elements
#    in order to determine the highest rated, 
    #    since the list supplied isn't an undefined amount, 
    #    using a for loop makes sense
    
    #    for each element in the list of restaraunts, 
    #    for restaraunt in restaraunts:


#    we need to get the rating from the dictionary
#    loop through the list of elements


# 5. restaraunt is now the dictionary
#    we now need to loop through keys in the dictionary - inner loop
#    
#    get the value for the rating key of that restaraunt dict
#    for value in restaraunt.get("rating") : -----------------------------------> better way to do this

# 6. check if the value is between 1 and 5--------------------------------------> didn't need this
#    check  between 1 and 5

#  7 if the value if less than 1 or more than 5 ---------------------------------> didn't need this
#  return error message


#    the final result will need the key and the value of the highest rated
#    so the best way to do this is to get both at the same time is
#    for key, value in restaraunt.items():

# ========================================== TEST  ==========================================

# function takes in the parameter is restaurants
# restaraunts is list of dictionaries
def get_highest_rated(restaurants):

    # Check if restaurants is empty
    # tests no restaurants/ empty list [] 
    # if it's empty, return None
    # 2. Handle invalid input
    if len(restaurants) == 0:
        # print(None)
        return None

    # Set highest_rated to the first element in restaurants
    highest_rated_restaurant = restaraunts[0]

    # Loop through restaurants 
    # tests multiple restaurant values
    for restaurant_elem in restaraunts:
        # and compare the current resturant rating to the highest_restaurant rating.
        if restaraunts["rating"] > highest_rated_restaurant["rating"]:
            # If the current restaurant rating is higher, 
            # reassign the current restaurant element to highest_restaurant
            highest_rated_restaurant = restaurant_elem

    # Return highest_rated
    # return value is restaurant with the highest rating
    # the return value is a dictionary, the entire restaurant
    return highest_rated_restaurant
