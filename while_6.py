def demonstrate_continue():
    i = 3

    while i < 10:
        i += 1
        if i == 7:
            print("i is seven!")
            print("Let's print this special message, and then move on")
            print("*~*~*~* \o/ *~*~*~*")
            continue
        print(f"Counting: i is {i}")

demonstrate_continue()

Output: 
