# Example 1
menu = {
    "appetizer": "Brussels Sprouts",
    "beverage": "Fancy Lemonade"
}

for dish, food in menu.items():
    print(f"The special {dish} for tonight is the {food}.")

# Follow these steps for each example:

# 1. Read through the code and identify:
    # What is the dictionary? menu

    # What is each key and value? 
        #   key = appetizer: value = Brussel Sprouts
        #   key = beverage: value = Fancy Lemonade

    # What do we name each key and value?
        # key = dish
        # value = food

    # How do we use each key and value in the loop?
        #  for each key and value in the dictionary we print 
        #  The special {dish} for tonight is the {food}.

# 2. Predict what will print
# The special appetizer for tonight is the Brussels Sprouts.
# The special beverage for tonight is the Fancy Lemonade.

# 3. Run the code and check your prediction
# The special appetizer for tonight is the Brussels Sprouts.
# The special beverage for tonight is the Fancy Lemonade.

# Example 2
menu = {
    "Brussels Sprouts": 18.99,
    "Fancy Lemonade": 56.00
    }

for food, price in menu.items():
    taxed_price = price * 1.101
    print(f"The cost of {food} is {taxed_price}")

print("That sure was a meal!")

# Follow these steps for each example:

# 1. Read through the code and identify:
    # What is the dictionary? menu

    # What is each key and value?
    # key = Brussels Sprouts value = 18.99
    # key = Fancy Lemonade value = 56.00

    # What do we name each key and value?
    # key = food
    # value = price

    # How do we use each key and value in the loop?
    # for each key and value in menu items, 
    # we take the price(value) of the food item
    # for each food item in the menu 
    # and multiply the price x 1.101 to get the taxed_price
    #  then we print: 
    # "The cost of {food} is {taxed_price}" for each item in the dictionary 
    #  then print "That sure was a meal!"

# 2. Predict what will print
# The cost of Brussels Sprouts is 20.90799
# The cost of Fancy Lemonade is 61.656

# 3. Run the code and check your prediction
# The cost of Brussels Sprouts is 20.907989999999998
# The cost of Fancy Lemonade is 61.656
# That sure was a meal!

def consider_specials(specials):
    for dish, special in specials.items():
        print(f"For the special {dish}, why not consider the {special} tonight?")

menu = {
    "appetizer": "Brussels Sprouts",
    "beverage": "Fancy Lemonade"
}

consider_specials(menu)

menu = {
    "appetizer": "Brussels Sprouts",
    "beverage": "Fancy Lemonade"
}

for dish in menu:
    print(f"The special {dish} for tonight is the {menu[dish]}.")
    
#  using .keys()
menu = {
    "appetizer": "Brussels Sprouts",
    "beverage": "Fancy Lemonade"
}

print("What are the categories on the menu tonight?")
categories = []

for category in menu.keys():
    categories.append(category)

print(categories)

#  using .values()
menu = {
    "appetizer": "Brussels Sprouts",
    "beverage": "Fancy Lemonade"
}

print("What are the special dishes on the menu tonight?")
special_dishes = []

for special_dish in menu.values():
    special_dishes.append(special_dish)

print(special_dishes)

drink_menu = {
    "hot": "coffee",
    "cold": "iced tea"
}
