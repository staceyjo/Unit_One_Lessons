# Mady and Lesha made a great discovery! 

# Their local library had a journal written 
# by one of the greatest bug catchers ever known! 
# It claims to have a list of all known bugs in the area. 
# Mady and Lesha want to know how many are left for them to find!

# Assuming Mady and Lesha have caught the following bugs:

mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]

# And that the great bug catcher journal lists the following bugs:

journal_bugs = ["pill bug", "damselfly", "stag beetle", "ladybug", "honey bee", "monarch butterfly", "moth", "caterpillar", "earwig", "lightning bug", "dragonfly", "stag beetle", "millipede", "june bug", "carpenter ant"]

# Write a function left_to_catch that they can use 
# to find out which bugs each of them has left to catch.

# Was the great bug catcher journal correct? 
# Only time will tell! 
# Mady and Lesha are excited for their adventures to continue!

def left_to_catch(caught_list, all_list):
    # convert lists to sets
    caught_set = set(caught_list)
    # print(caught_set)
    complete_set = set(all_list)
    # print(complete_set)
    
    # compare caught set to complete set and return bugs left to find
    #  to do this, we can use difference from the complete set
    remaining_set = complete_set - caught_set
    #  returns a set
    print(remaining_set)
    return remaining_set


left_to_catch(mady_bugs, journal_bugs) # {'pill bug', 'earwig', 'dragonfly', 'millipede', 'damselfly', 'stag beetle', 'honey bee', 'moth'}
left_to_catch(lesha_bugs, journal_bugs) # {'damselfly', 'monarch butterfly', 'honey bee', 'carpenter ant', 'moth', 'ladybug', 'caterpillar'}

# # Mady List
# ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]

# #  Mady set
# {'june bug', 'caterpillar', 'carpenter ant', 'lightning bug', 'ladybug', 'monarch butterfly'}

# #  full_set
# {'june bug', 'caterpillar', 'carpenter ant', 'lightning bug', 'ladybug','monarch butterfly', 'pill bug', 'earwig','dragonfly','millipede', 'damselfly','stag beetle',   'honey bee', 'moth',  }

# # returned set
# {'pill bug', 'earwig', 'dragonfly', 'millipede', 'damselfly', 'stag beetle', 'honey bee', 'moth'}


# Learn example of a working implementation:
def left_to_catch(caught_list, all_list):
    # build a new unique set from each input
    # inputs are expected to be lists possibly containing duplicates
    caught_set = set(caught_list)
    all_set = set(all_list)

    # find result by removing the caught set from the all set
    # notice this is the same approach as for caught_only_by_first
    # the difference is the order
    result = all_set - caught_set

    # return the result set
    return result


