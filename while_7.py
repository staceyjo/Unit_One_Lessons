# Fix this loop so it loops while i is less than 5 

def loop_until_five():
    i = 0

    while i < 5:
        i += 1
        # print(i)

    print(i)
    return i

result = loop_until_five()

# version from Learn: 
# An example of a working implementation:

def loop_until_five():
    i = 0

    while i < 5:
        i += 1

    return i

# Here are the tests:

# def test_loop_until_five():
#     assert loop_until_five() == 5

# Even though the loop only ran while i was less than five, when i was the value 4, it incremented to 5.

# Prove this to yourself by running this code!

def loop_until_five():
    i = 0

    while i < 5:
        print("new loop")
        print("before inc, aka i < 5 is true:", i)
        i += 1
        print("after inc:", i)

    return i