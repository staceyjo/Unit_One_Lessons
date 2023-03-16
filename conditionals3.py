# The following examples all evaluate to True:
not False
not 0
True and not False
not False or False
not None

# The following examples all evaluate to False:
not True
not 1
True and not True
not True or False

# Order of Operations and Operator Precedence
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. in, not in, is, is not, <, <=, >, >=, !=, ==
# 6. not
# 7. and
# 8. or

# Consider these examples that all evaluate to True:
not 6 - 2 * 3   # 2*3 = 6, not 6 - 6, not 0 = TRUE

not 3 > 100 # 3 is NOT less that 100 which makes it falsy, not falsy makes it a double negative, which evaluates to true 

5 * 5 > 20 + 4  # 25 > 20 + 4, 10 > 24 is truthy, which evaluates to True 

not True != True    # True != True is False, not False evaluates to True

not 3 > 100 or False    # 3>100 is False, not False or False means True or False, which is True

3 > 100 or not False or False # 3> 100 is False, (False or not False) or False -> (False or True) or False  -> True or False -> True



