counter = 0
cats = ['Grumpy Cat', 'Garfield', 'Lil Bub', 'Maru', 'Keyboard Cat', 'Hello Kitty']
while counter < len(cats):
    print(cats[counter])
    counter += 1
    
# The while loop iterates over the contents of the list of famous cats in order, printing each out, one by one. The correct for loop does the same thing, but notice how much clearer it is. We don't have to set up the counter. We don't have to compare it to the length of the list. We don't have to index into the list values. And we don't have to advance the counter. while loops are very flexible, but for some tasks, like iterating over lists and dictionaries in order, a for loop is usually more appropriate.


# Compare the correct for loop to the other answers and try explaining why they don't work. Try running them in the Python interpreter and notice the errors it reports for each.

cats = ['Grumpy Cat', 'Garfield', 'Lil Bub', 'Maru', 'Keyboard Cat', 'Hello Kitty']
for cat in cats:
    print(cat)
