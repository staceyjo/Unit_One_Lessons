# Sandra is having a party and has three recipes she wants to make. 
# She has created a list of ingredients for each recipe:

# Write a function shopping_list 
# that Sandra can use to create a shopping list 
# of all of the ingredients that she will need 
# to purchase. 

# She wants each item to show up only once in the list.
bruschetta = ["bread", "olive oil", "garlic", "tomato", "basil", "balsamic vinegar", "salt"]
pesto_pasta = ["pasta", "olive oil", "garlic", "basil", "parmesan", "pine nuts"]
salsa = ["tomato", "onion", "garlic", "salt", "green onion", "cilantro", "jalapeno"]

def shopping_list(recipe1, recipe2, recipe3):  

    # change 3 list arguments to sets
    set_one = set(recipe1)
    # print(set_one)
    
    set_two = set(recipe2) 
    # print(set_two)
    
    set_three = set(recipe3)
    # print(set_three)
    
    # union of two sets
    # shopping_set = set_one.union(set_two)
    # print(shopping_set)
    
    # will union join 3? yep, it works
    # shopping_set = set_one.union(set_two).union(set_three)
    
    # syntax to unify more than two sets
    shopping_set = set_one.union(set_two, set_three)
    # print(shopping_set)

    # change set back to list, and return the list
    final_list = list(shopping_set)
    # print(final_list)
    return final_list

shopping_list(bruschetta, pesto_pasta, salsa)
shopping_list([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])


# Their solution: 
#     def shopping_list(recipe1, recipe2, recipe3):
#     # build a unique set from each input (inputs are expected to be lists)
#     set1 = set(recipe1)
#     set2 = set(recipe2)
#     set3 = set(recipe3)

#     # find the union of all three sets
#     result = set1 | set2 | set3

#     # build a list from the result set to return
#     return list(result)