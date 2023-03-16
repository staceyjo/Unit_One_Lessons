def demonstrate_break():
    i = 3

    while i < 10:
        if i == 7:
            print("i is seven! Let's get out of here!")
            break
        print(f"Counting: i is {i}")
        i += 1

demonstrate_break()