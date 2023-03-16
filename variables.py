def display_breakfast(breakfast_of_champions):
    # The parameter breakfast_of_champions exists in this function!
    print(f"This function call has the parameter breakfast_of_champions with the value {breakfast_of_champions}")

    # The local variable breakfast_message exists in this function!
    breakfast_message = f"My breakfast today is {breakfast_of_champions}"
    print(breakfast_message)

    # After the return statement, the function will end, and breakfast_of_champions AND breakfast_message will no longer exist...
    return breakfast_message

display_breakfast("waffles and syrup")
# print(f"Uncommenting this line and trying to access breakfast_of_champions will create a NameError: {breakfast_of_champions}")
# print(f"Uncommenting this line and trying to access breakfast_message will create a NameError: {breakfast_message}")
display_breakfast("rice and soup")
display_breakfast("coffee and toast")
# print(f"Uncommenting this line and trying to access breakfast_of_champions will create a NameError: {breakfast_of_champions}")
# print(f"Uncommenting this line and trying to access breakfast_message will create a NameError: {breakfast_message}")
