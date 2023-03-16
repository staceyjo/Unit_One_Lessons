this_expression_is_truthy = True
a_different_expression_is_truthy = True
this_is_a_false_expression = []



# this conditional expression will only execute for this_expression_is_truthy 
# if this_expression_is_truthy:
#     print("The expression is truthy!")
#     print("We will run all code in the if clause.")
# elif a_different_expression_is_truthy:
#     print("The above if clause did NOT run...")
#     print("AND this different expression IS truthy")
#     print("So now we run the code is in this clause.")
# else:
#     print("The expression is falsy!")
#     print("We will run all code in the else clause.")

# this conditional expression will only execute for a_different_expression_is_truthy 
if a_different_expression_is_truthy:
    print("The above if clause did NOT run...")
    print("AND this different expression IS truthy")
    print("So now we run the code is in this clause.")

elif this_expression_is_truthy:
    print("The expression is truthy!")
    print("We will run all code in the if clause.")

else:
    print("The expression is falsy!")
    print("We will run all code in the else clause.")