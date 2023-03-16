# Mady and Lesha would love to know which bugs each has caught 
# that the other hasn't!

# Assuming Mady and Lesha have caught the following bugs:

mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]

# Write a function caught_only_by_first 
# that they can use to compare the bugs each has caught, 
# so they can see the bugs that have only been caught 
# by the first one of their data passed to the function.

def caught_only_by_first(first_list, second_list):
    # turn a list into a set
    first_set = set(first_list)
    second_set = set(second_list)
    
    set_difference = first_set.difference(second_set)
    # print(set_difference)
    
    # returns a set
    return set_difference


caught_only_by_first(mady_bugs, lesha_bugs) # {'ladybug', 'monarch butterfly', 'carpenter ant', 'caterpillar'}
caught_only_by_first(lesha_bugs, mady_bugs) # {'millipede', 'stag beetle', 'earwig', 'pill bug', 'dragonfly'}

# Learn example of a working implementation:

def caught_only_by_first(first_list, second_list):
    # build a new unique set from each input
    # inputs are expected to be lists possibly containing duplicates
    first_set = set(first_list)
    second_set = set(second_list)

    # find result by removing anything from the second set from the first
    # notice this is order-dependent
    result = first_set - second_set

    # return the result set
    return result