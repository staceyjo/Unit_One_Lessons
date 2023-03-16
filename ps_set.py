my_set = {"apple", "orange", "banana"} < {"apple", "orange", "banana", "melon", "peach"}
print(my_set)
# True because it is a proper subset, set b contains all of the elements in the first set and they are not equal

my_set = {"apple", "orange", "banana"} > {"apple", "orange", "banana", "melon", "peach"}
print(my_set)
# False because ...

my_set = {"apple", "orange", "banana"}.isdisjoint({"melon", "peach"})
# True because...they don't have anything overlapping
print(my_set)

my_set = {"apple", "orange", "banana"}.isdisjoint({"apple", "orange", "banana", "melon", "peach"})
# True because...
