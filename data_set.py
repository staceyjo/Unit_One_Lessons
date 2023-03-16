# set_a = {1, 2, 3}
# random_element = set_a.pop()
# print(set_a)


editors = {"Lorraine", "Colin", "Aedan"}
authors = {"Lorraine", "Colin", "Aedan", "Ajwa", "Ciara"}

editors.issubset(authors) # evaluates to True
print(editors.issubset(authors))

editors <= authors # evaluates to True
print(editors <= authors)