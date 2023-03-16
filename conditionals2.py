a_list = []

if len(a_list) == 0:
    print("The list is empty.")

if a_list == []:
    print("The list is empty.")


# Pythonic way, using the logical not operator
# syntax: 
#   if not value:
#       statement(s)

# the value can be a boolean, string, dictionary, list, set, tuple, etc.
# The statements inside of the if block will only execute IF the value
# is False or if the value is empty.

# not acts like a negation operator
# if the value of the variable is False, like in this case an empty list
# the value of an empty list does NOT have a positive value
# if NOT (positive)value, would check out and the statement would print
# we can use if not expression to conditionally execute a block of statements only if the value is not empty or not False.

# the pythonic way to write this conditional control structure
if not a_list:
    print("The list is empty.")

# if we change the value of the variable to include elements:
a_list = ["one element", "another element"]
if len(a_list) > 0:
    print("The list has at least one element.")

# The more pythonic way to write the above conditional:
if a_list:
    print("The list has at least one element.")