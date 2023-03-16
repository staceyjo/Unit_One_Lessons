# function find_with_pos takes in two parameters: items & item

def find_with_pos(items, item):
    
    # if the item is one of the items in the list

    if item in items:
        
        #  return True, and the index position of the item/ where the item was found
        return True, items.index(item)
    
    #  if the item isn't in the items list, return False and None

    return False, None

#  found is a variable
#  pos is a variable
#  we assign the result to found, pos, Python assigns the returned values in order, so found receives the value that was at position 0 in the returned tuple, and pos gets the value that was at position 1.
found, pos = find_with_pos([1, 2, 3], 3)
print(f"found: {found}, pos: {pos}")