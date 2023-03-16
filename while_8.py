# How many times will the body of this while loop run?

counter = 4
while counter >= 0:
    print('in the loop body')
    counter -= 1
    
# A loop like this, running from some value all the way down to 0, might be used to access the entries in a list in reverse order. This loop iterates from 4 down to 0, which are the indices of a list with 5 items.


# Because this "off by one" can be confusing, we often prefer for loops in a situation like this rather than a while loop.