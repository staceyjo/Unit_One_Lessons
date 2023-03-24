def calculate_bill(items):
    subtotal = 0
    # changed sales tax to 8%
    sales_tax = 0.08
    tip = 0.2

    # changed range from 1 to 0
    for i in range(0, len(items)):
        subtotal += items[i]["price"]

# (1 + tip) will multiply total by 1.2
# (1 + sales_tax) will multiply by 1.8
    total = subtotal * (1+ sales_tax) * (1 + tip)

    return total

items = [ {
    "name": "Pasta",
    "price": 14.99,
    },
    {
    "name": "Dumplings",
    "price": 9.99,
    },
    {
    "name": "Diet Coke",
    "price": 2.99,
    },
    {
    "name": "Ice T",
    "price": 0.89,
    },
    {
    "name": "Green Curry Chicken",
    "price": 18.39,
    },
]

bill = calculate_bill(items)
print(f"{bill=}")