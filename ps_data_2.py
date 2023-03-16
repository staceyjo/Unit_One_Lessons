# Implement the function add_grocery(). 
# This function takes in a grocery_list and a new_item. 
# This function should append the new item 
# to the end of the grocery list, 
# and then return the grocery list.

def add_grocery(grocery_list, new_item):
    grocery_list.append(new_item)
    print(grocery_list)
    return grocery_list

add_grocery([], "Rice") # ["Rice"]
add_grocery(["Rice"], "Beans")  # ["Rice", "Beans"]

print("==================== #2 ===================")
def copy_top_item(my_groceries, their_groceries):
    new_list = their_groceries[0]
    # print(new_list)
    my_groceries[0] = new_list
    print(my_groceries)
    return my_groceries

copy_top_item(["Spinach", "Broccoli", "Eggplants", "Potatoes"], ["Avocados", "Oat Milk", "Mangoes"])
