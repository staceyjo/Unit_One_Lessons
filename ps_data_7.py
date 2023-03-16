# Mady and Lesha are really enjoying comparing their adventures! But now they'd love to know how many kinds of bugs they've caught in combination. They're pretty sure that they've caught a lot more bugs together than they have individually!

# Assuming Mady and Lesha have caught the following bugs:

mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]

# Write a function caught_together that they can use 
# to find all the bugs that they've caught: 
# either only by Mady, only by Lesha, or by both of them!

def caught_together(first_list, second_list):
    # convert lists to sets
    set_one = set(first_list)
    set_two = set(second_list)
    
    #  combine all the sets to one set
    final_set = set_one.union(set_two)
    #  returns a set
    # print(final_set)
    return final_set

caught_together(mady_bugs, lesha_bugs) # {'pill bug', 'stag beetle', 'ladybug', 'monarch butterfly', 'caterpillar', 'earwig', 'lightning bug', 'dragonfly', 'millipede', 'june bug', 'carpenter ant'}
caught_together(lesha_bugs, mady_bugs) # {'pill bug', 'stag beetle', 'ladybug', 'monarch butterfly', 'caterpillar', 'earwig', 'lightning bug', 'dragonfly', 'millipede', 'june bug', 'carpenter ant'}

# Learn example of a working implementation:

def caught_together(first_list, second_list):
    # build a new unique set from each input
    # inputs are expected to be lists possibly containing duplicates
    first_set = set(first_list)
    second_set = set(second_list)

    # find result by finding the contents of both sets combined
    result = first_set | second_set

    # return the result set
    return result