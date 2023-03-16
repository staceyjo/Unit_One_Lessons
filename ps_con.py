# Online-retailers often provide free shipping to members 
# if their cart total reaches at least $100. 

# Select the option that describes the logic to determine 
# if a customer will receive free shipping or not.

is_account_member = True
cart = 100

# Option 1
if is_account_member and cart >= 100:
    print("You are qualified for free shipping. Proceed to checkout.")
elif is_account_member is False and cart >= 100:
    print("Sign up today for free shipping on your next order.")
else: 
    print("Save on shipping by becoming a member and spending $100")


print("================ Boolean Practice 1 ================")
# customer_age = 60

# if customer_age < 0:
#     print("please enter a valid age")
# if customer_age <= 10:
#     ticket_price = 10.00
# if customer_age <= 17:
#     ticket_price = 13.00
# if customer_age < 60:
#     ticket_price = 15.00
# if customer_age >= 60:
#     ticket_price = 11.00
    
# print(ticket_price) # This prints 15.00 for everyone under 60


customer_age = 60

if customer_age < 0:
    print("please enter a valid age")
elif customer_age <= 10:
    ticket_price = 10.00
elif customer_age <= 17:
    ticket_price = 13.00
elif customer_age < 60:
    ticket_price = 15.00
else:
    ticket_price = 11.00
    
print(ticket_price) # This works perfectly


# Option 3
print("================ Boolean Practice 3 ================")

customer_age = -1

if customer_age >= 60:
    ticket_price = 11.00
elif customer_age < 60:
    ticket_price = 15.00
elif customer_age <= 17:
    ticket_price = 13.00
elif customer_age <= 10:
    ticket_price = 10.00
elif customer_age < 0:
    print("please enter a valid age")

print(ticket_price) 