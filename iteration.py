# Iterating through data: 
#  Example 1: Dining Out
    
options = [
    "the place I'm craving but is too far away",
    "the place we always go to",
    "that place that just opened but looks too fancy"
    ]

for option in options:
    print(f"What about getting food from {option} tonight?")
    

# 1. Read through the code and identify:
#     - What is the list? options
    
#     - What is each element? string
    
#     - What do we name each element? option
    
#     - How do we use each element in the loop? to cycle through the list of options
    
# 2. Predict what will print:
    # first loop: "What about getting food from the place I'm craving but is too far away tonight?"
    # second loop: "What about getting food from the place we always go to tonight?"
    # third loop: "What about getting food from that place that just opened but looks too fancy tonight?"

# 3. Run the code and check your prediction
# What about getting food from the place I'm craving but is too far away tonight?
# What about getting food from the place we always go to tonight?
# What about getting food from that place that just opened but looks too fancy tonight?



# Example: Calculating Taxes
prices = [18.99, 56.00, 48.50, 18.50]

for price in prices:
    taxed_price = price * 1.101
    print(f"The cost of one item is {taxed_price}")

print("That sure was a meal!")

# 1. Read through the code and identify:
#     - What is the list? prices
    
#     - What is each element? a float 
    
#     - What do we name each element? price
    
#     - How do we use each element in the loop? take the price and  multiply is by 1.101 to get the taxed price and then print the taxed price
    
# 2. Predict what will print
"The cost of one item is 20.91"
"The cost of one item is 61.66"
"The cost of one item is 53.40"
"The cost of one item is 20.37"
"That sure was a meal!"
# 3. Run the code and check your prediction
# The cost of one item is 20.907989999999998
# The cost of one item is 61.656
# The cost of one item is 53.3985
# The cost of one item is 20.3685
# That sure was a meal!

#  Floats do not round up automatically!!

def consider_options(options):
    for option in options:
        print(f"What about getting food from {option} tonight?")

pizza_places = ["your favorite pizza place", "my favorite pizza place"]
consider_options(pizza_places)