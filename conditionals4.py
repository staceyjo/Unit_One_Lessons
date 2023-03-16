var1 = None     # False
var2 = 1        # True    
var3 = {}       # False
var4 = [0, 0]   # True
var5 = "None"   # True

# Which evaluate to True?
var1 or var2                # False or True, evaluates to True

var3 or (var1 and var2)     # False or (False and True) -> False or False, evaluates to False

var5 and var2               # True and True, evaluates to True

var4 or var3                # True or False, evaluates to True

not var5 and var2           # True and True, evaluates to True. not True, evaluates to False

var5 or var3                # True or False, evaluates to True

var2 or not var5            # True or not True, True or False, evaluates to True

not (var3 or var1)          # not ( True or False) -> False or True, evaluates to True