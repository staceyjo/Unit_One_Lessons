

# 2. restaraunts will be a list of dictionaries
#    example argument for restaraunts when passed in the function : 
#    restaraunts = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}] 

# 3. set variable for highest_rated_value:
#    highest_rated = 5


# 4.  set variable for rating to ensure the value is a number
#     if no value is entered int() will return 0
#     rating_int = int()



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
#    for value in restaraunt.get("rating") :

# 6. check if the value is between 1 and 5
#    check  between 1 and 5

#  7 if the value if less than 1 or more than 5
#  return error message



#    the final result will need the key and the value of the highest rated
#    so the best way to do this is to get both at the same time is
#    for key, value in restaraunt.items():

#  5. 

# [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]


# 1. define the function get_highest_rated() 
#    that takes in one parameter, restaurants
def get_highest_rated(restaurants):
    
    # 2. Handle invalid input
    if len(restaurants) == 0:
        # print(None)
        return None
    
    # 3.  Given valid input, perform the computation/solve the problem/etc.
    # check if list contains only one element
    # if only one element, return that dictionary
    elif len(restaurants) == 1:
        # print(restaurants[0])
        return restaurants[0]
    
    # checks if list containts more than one element:
    elif len(restaurants) > 1:
        # loop through each restaraunt element in restaraunts list:
        for restaraunt_elem in restaurants:
            highest_rated = {}
            # so now we have two dictionarys and 
            # i want to compare the value of the second key in each dictionary
            for rest_key, rest_val in restaraunt_elem.items():
                # print(f"{rest_key=}")
                # print(f"{rest_val=}")
                if rest_val == 5:
                    highest_rated=restaraunt_elem
                    print(highest_rated)
                    return highest_rated



# Passes
get_highest_rated([])
# expected_result = None  

# Passes
get_highest_rated([{"name": "Crow's Nest", "rating": 1}])
# expected_result = {"name": "Crow's Nest", "rating": 1}


# Passes
get_highest_rated([{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}])
# expected_result= {"name": "Crow's Nest", "rating": 5}

# rating higher than 5
# get_highest_rated([{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 6}])

# # loop through list elements in restaurants
# for restaurant_elem in restaurants:
#     print(f" looping through list: {restaurant_elem=}")
#     highest_rated = {}
#     #  if list only contains 1 element, return that element
#     if len(restaurants) == 1:
#         print(f" single dictionary element in list {restaurant_elem}")
#         # update the dictionary with the single element
#         highest_rated = restaurant_elem
#         print(f"{highest_rated=}")
        
#     else:
#         # loops through each restaurant element in restaurants list if the list is longer than 1
        
#         # then loops through each key, value pair for each dictionary
#         for restaurant_key, restaurant_value in restaurant_elem.items():
#             print(f"{restaurant_key=}")
#             print(f"{restaurant_value=}")
            
#             # checks if restaurant value is equal to 5, 
#             if restaurant_value == 5:
#                 # if it is, reassigns the key for highest rated to 5
#                 highest_rated[restaurant_key] = restaurant_value
#                 # highest_rated[restaurant_value] = restaurant_value
#                 print(f"{highest_rated=}")
                        
            # for key, value in restaurant_dict.items():
            #     print(f"{key=}")
            #     print(f"{value=}")
                
        # for key, value in restaurant_elem.items():
        #     print(f"{value=}")
        #     print(f"{key=}")
        #     for key in restaurant_elem.get("rating"):
        #         print(f"{key=}")
        
        # for restaurant_dict_key in restaurants: 
        #     print(restaurant_dict_key)
            
            # for rest_key in restaurant_dict["rating"]:
                # print(rest_key)
                # rating = restaurant_elem.get("rating")
                # print(rating)


    
    # # print(int(rating))
    # rating_int = int(rating)
    # print(rating_int)
    
    # if rating_int == 5:
    #     print(restaurant_dict)
