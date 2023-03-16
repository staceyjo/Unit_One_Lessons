print("=========== Example 1 ===========")  

for fruit in ["apples", "oranges", "bananas"]:
    print("I'm in the for loop! The value of fruit is:", fruit)
    break
    print("This message will never print, because the for loop saw break before it saw me...")
    
    
print("=========== Example 2 ===========")  
    
print("I'm looking for a four leaf clover in the field...")

for field_item in ["grass", "grass", "more grass", "four-leaf clover", "rocks", "rocks", "more rocks"]:
    print("...")
    if field_item == "four-leaf clover":
        print("I found a four-leaf clover!")
        print("My hunt is over! I can leave now")
        break
    print(f"I found {field_item} in the field...")
    print("Better keep looking.")


print("=========== Example 3 ===========")  

for field_item in ["grass", "grass", "more grass", "rocks", "rocks", "more rocks"]:
    print("...")
    if field_item == "four-leaf clover":
        print("I found a four-leaf clover!")
        print("My hunt is over! I can leave now")
        break
    print(f"I found {field_item} in the field...")
    print("Better keep looking.")
else:
    print("I didn't find a four-leaf clover today.")
