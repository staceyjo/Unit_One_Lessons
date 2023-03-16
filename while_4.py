# We can use a while-loop 
# that only checks if a variable is True or truthy!

import random
coin_is_tails = True

while coin_is_tails:
    print("The coin flip is tails!")
    print("Will we get heads in the next coin flip?")
    coin_is_tails = bool(random.randint(0, 1))

print("We finally got heads.")