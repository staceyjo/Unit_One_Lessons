# Create a function named find_adults. 
# This function...

# Has one parameter, people, which is a dictionary.

# Each key is a string that holds the name of a person.

# Each value is an integer that is the age of that person.

# The function should return a list of all the names of people 
# that are 18 or older. The list can be in any order. 
# If there are no adults in the dictionary, 
# the function should return an empty list.
people = {
    "Jane": 23,
    "Mateo": 2,
    "Eduardo": 18,
    "Elsa": 1,
    "Alba": 66
}

def find_adults(people):
    adult_list = []
    
    for name, age in people.items():
        if age >= 18:
            adult_list.append(name)
    # print(adult_list)
    return adult_list

find_adults(people) # ["Jane", "Eduardo", "Alba"]
    
