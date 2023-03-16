def challenge_01():
    apples = 1729
    oranges = 42
    papaya = apples
    # 1
    print("============ Challnege 01: #1 =============")
    print(f"apples: ", apples,"ID: " ,id(apples))
    print(f"oranges: ", oranges, "ID: " ,id(oranges))
    print(f"papaya: ", papaya, "ID: " ,id(papaya))

    # 2
    print("============= Challnege 01: #2 =============")
    apples = apples + oranges
    print(f"apples: ", apples,"ID: " ,id(apples))
    print(f"oranges: ", oranges, "ID: " ,id(oranges))
    print(f"papaya: ", papaya, "ID: " ,id(papaya))
challenge_01()


print("============= Challnege 02: #1 =============")

def challenge_02():
    apples = 1729
    oranges = 42
    bananas = [apples, oranges]
    
    print(f"apples: ", apples,"ID: " ,id(apples))
    print(f"oranges: ", oranges, "ID: " ,id(oranges))
    print(f"bananas:", bananas, "ID: ", id(bananas))
challenge_02()
    
    
print("============= Challnege 03: #1 =============")
    # 3

def challenge_03():
    apples = 1729
    oranges = 42
    bananas = [apples, oranges]
    print(f"apples: ", apples,"ID: " ,id(apples))
    print(f"oranges: ", oranges, "ID: " ,id(oranges))
    print(f"bananas: ", bananas, "ID: " ,id(bananas))

    challenge_03_helper(bananas)



print("============= Challnege 03: #2 =============")

def challenge_03_helper(kiwis):
    mangos = 315
    kiwis.append(mangos)
    # 4
    print(f"mangos: ", mangos,   " ", "ID: " ,id(mangos))
    print(f"kiwis: ",  kiwis,  " ", "ID: " ,id(kiwis))

challenge_03()

