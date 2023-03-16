# Mady and Lesha track their bug information in lists. 

# They would love to know which unique bugs each has caught.

# They'd like to get some sort of insect index, 
# sort of an InsectDex containing that unique information.

# Assuming Mady and Lesha have caught the following bugs:
mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]

def make_insect_dex(bug_list):
    # lists to a sets, set will remove the duplicates
    set_of_bugs = set(bug_list)
    
    #  returning a set
    # print(set_of_bugs)
    return set_of_bugs

make_insect_dex(mady_bugs) # return {'lightning bug', 'caterpillar', 'ladybug', 'monarch butterfly', 'june bug', 'carpenter ant'}
make_insect_dex(lesha_bugs) # return {'stag beetle', 'earwig', 'millipede', 'pill bug', 'june bug', 'lightning bug', 'dragonfly'}

# Learn solution
def make_insect_dex(bug_list):
    # build a new unique set from the input
    # bug_list is expected to be a list possibly containing duplicates
    return set(bug_list)