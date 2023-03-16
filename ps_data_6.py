# Mady and Lesha's bug excitement continues unabated! 
# They know which bugs they caught that were distinct from one another, 
# but would like to know which bugs they caught in common.


# Assuming Mady and Lesha have caught the following bugs:
mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]

# Write a function caught_by_both that they can use 
# to find out which bugs were caught both by Mady and by Lesha.

def caught_by_both(first_list, second_list):
    #  convert lists to sets
    set_one = set(first_list)
    set_two = set(second_list)
    
    # find the intersection
    intersected_set = set_one.intersection(set_two)
    # print(intersected_set)
    
    # returns a set
    return intersected_set
    

caught_by_both(mady_bugs, lesha_bugs)   # {'lightning bug', 'june bug'}
caught_by_both(lesha_bugs, mady_bugs)   # {'lightning bug', 'june bug'}


# Learn example of a working implementation:

def caught_by_both(first_list, second_list):
    # build a new unique set from each input
    # inputs are expected to be lists possibly containing duplicates
    first_set = set(first_list)
    second_set = set(second_list)

    # find result by finding where the sets intersect (overlap)
    result = first_set & second_set

    # return the result set
    return result