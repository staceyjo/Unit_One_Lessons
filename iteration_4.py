lucky_charms_quantities = {
    "horseshoe": 4,
    "four-leaf clover": 0,
    "lucky coin": 10
}

for charm, quantity in lucky_charms_quantities.items():
    if quantity == 0:
        continue
    print(f"I found one more {charm}!")
    lucky_charms_quantities[charm] = quantity + 1

# =========================
for number in range(0, 6):
    print(number)


# ========================= 
print("Blast off in:")

for count in range(10, 0, -1):
    print(count, "...")

print("Blast off!")

for i in range(33):
    if i % 3 != 0:
        continue
    print(f"{i} is divisible by 3!")